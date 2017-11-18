import pandas as pd
from knn import train, test, feature_select
from get_tracks import get_test_tracks, add_songs

# songs by steven wilson + songs different to steven wilson as training data 
train_data = pd.read_csv('data/Train.csv')

# progressive rock playlist for testing
test_data = get_test_tracks('thesoundsofspotify', '1sYzsb7P37XzNZoUR2GGdm')

# useless columns
ignore = (['analysis_url', 
           'id', 
           'track_href', 
           'uri', 
           'type', 
           'album', 
           'name', 
           'duration_ms',
          ])

train_data.drop(ignore, axis=1, inplace=True)
clean_test_data = test_data.drop(ignore, axis=1)

# select most significant features
cols = feature_select(train_data.loc[:, train_data.columns != 'class'], train_data['class'])

# train using the selected features
knn = train(train_data[cols], train_data['class'])

# classify songs in the test playlist
predictions, prob = test(knn, test_data, cols)
test_data['predict'] = predictions

# probability that a song is 0 (different from wilson)
# or 1 (similar or identical to wilson)
test_data['prob0'] = [p[0] for p in prob]
test_data['prob1'] = [p[1] for p in prob]

# save songs that are more likely to be like steven wilson
# i'm using a > 80% treshold
add_songs('446Ms3T2bxMWwHUEoL64kF', test_data[test_data.prob1 > 0.8]['id'])
