import spotipy
import pandas as pd

from knn import feature_select, train, test
from get_tracks import login, get_full_playlist, normalize, update_training

# load training data
sw = pd.read_csv('data/Train.csv', encoding='ISO-8859-1')

# credentials
token = login()
sp = spotipy.Spotify(auth=token)

# discover weekly tracks
tracks = normalize(get_full_playlist('Spotify', '37i9dQZEVXcF9FYy68tj1G', sp))

# cleaning 
ignore = (['analysis_url', 
           'id', 
           'track_href', 
           'uri', 
           'type', 
           'album', 
           'name', 
           'duration_ms',
          ])

sw.drop(ignore, axis=1, inplace=True)
clean_tracks = tracks.drop(ignore, axis=1)

# select most significant features
cols = feature_select(sw.loc[:, sw.columns != 'class'], sw['class'])

# train using the selected features
knn = train(sw[cols], sw['class'])

# classify songs in the test playlist
predictions, prob = test(knn, clean_tracks, cols)
tracks['predict'] = predictions

# probability that a song is 0 (different from wilson)
# or 1 (similar or identical to wilson)
tracks['prob0'] = [p[0] for p in prob]
tracks['prob1'] = [p[1] for p in prob]

# print results
print(tracks[['name', 'predict', 'prob0', 'prob1']])
