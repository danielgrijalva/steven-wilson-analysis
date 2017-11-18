# steven-wilson-analysis
Using machine learning to find songs that are identical to Steven Wilson's style.

### Context

I'm going straight to the point: I'm obsessed with Steven Wilson. I can't help it, I love his music. And I *need* more music with similar (almost identical) style. So, what I'm trying to solve here is, **how to find songs that match SW's style with almost zero error?**

![][1]

I'm aware that Spotify gives you recommendations, like similar artists and such. But that's not enough -- Spotify always gives you varied music. Progressive rock is a very broad genre, and I just want those songs that sound very, **very** similar to Steven Wilson or Porcupine Tree.
  
BTW, Porcupine Tree was Steven Wilson's band, and they both sound practically the same. [I made an analysis](https://www.kaggle.com/danielgrijalvas/comparing-steven-wilson-and-porcupine-tree) where I checked their musical similarities.

### Content

I'm using the Spotify web API to get the data. They have an amazingly rich amount of information, especially the [audio features](https://developer.spotify.com/web-api/get-audio-features/).  
  
This repository has **5** datasets: 

 - `StevenWilson.csv`: contains Steven Wilson discography (65 songs)
 - `PorcupineTree.csv`:  65 Porcupine Tree songs
 - `Complete Steven Wilson.csv`: a merge between the past two datasets (Steven Wilson + Porcupine Tree)
 - `Train.csv`: 200 songs used to train KNN. 100 are Steven Wilson songs and the rest are totally different songs
 - `Test.csv`: 100 songs that may or may not be like Steven Wilson's. I picked this songs from various prog rock playlists and my Discover Weekly from Spotify.  
  
Also, so far I've made two kernels: 

 - [Comparing Steven Wilson and Porcupine Tree](https://www.kaggle.com/danielgrijalvas/comparing-steven-wilson-and-porcupine-tree) 
 - [Finding songs that match SW's style using K-Nearest Neighbors](https://www.kaggle.com/danielgrijalvas/finding-songs-that-match-sw-s-style-using-knn)

### Data
There are **21** columns in the datasets. 

**Numerical**: this columns were scraped using [get_audio_features](https://developer.spotify.com/web-api/get-audio-features/) from the Spotify API. 

 - `acousticness`: a confidence measure from 0.0 to 1.0 of whether the track is acoustic; 1.0 represents high confidence the track is acoustic
 - `danceability`: it describes how suitable a track is for dancing; a value of 0.0 is least danceable and 1.0 is most danceable
 - `duration_ms`: the duration of the track in milliseconds
 - `energy`: a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity
 - `instrumentalness`: predicts whether a track contains no vocals; values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0
 - `liveness`: detects the presence of an audience in the recording; 1.0 represents high confidence that the track was performed live
 - `loudness`: the overall loudness of a track in decibels (dB)
 - `speechiness`: detects the presence of spoken words in a track; the more exclusively speech-like the recording (e.g. talk show), the closer to 1.0 the attribute value
 - `tempo`: the overall estimated tempo of a track in beats per minute (BPM)
 - `valence`: a measure from 0.0 to 1.0 describing the musical positiveness; tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry)  

**Categorical**: these features are categories represented as numbers. 

 - `key`: the musical key the track is in. e.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on
 - `mode`: mode indicates the modality (major or minor); major is represented by 1 and minor is 0
 - `time_signature`: an estimated overall [time signature](https://en.wikipedia.org/wiki/Time_signature) of a track; it is a notational convention to specify how many beats are in each bar (or measure). e.g. 4/4, 4/3, 3/4, 8/4 etc.

**Strings**: these fields are mostly useless (except for name, album, artist and lyrics) 
 
 - `id`: the Spotify ID of the song
 - `name`: name of the song
 - `album`: album of the song
 - `artist`: artist of the song
 - `uri`: the Spotify URI of the song
 - `type`: the type of the Spotify object
 - `track_href`: the Spotify API link of the song
 - `analysis_url`: the URL used for getting the audio features
 - `lyrics`: lyrics of the song in lower case

### Contribute
I made a [Kaggle repository](https://www.kaggle.com/danielgrijalvas/steven-wilson-analysis). The datasets are there and you can create an IPython/R notebook easily.

### Future
Ever been obsessed with a song? an album? an artist? I'm planning on building a web app that solves this. It will help you find music extremely similar to other. 


  [1]: https://38.media.tumblr.com/b358910974f6582d49fc526c2e774c2e/tumblr_msq6s8LEij1s75866o1_500.gif
