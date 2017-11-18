import os
import time
import pandas as pd
from decouple import config 
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# spotify credentials
os.environ['SPOTIPY_CLIENT_ID'] = config('CLIENT_ID')
os.environ['SPOTIPY_CLIENT_SECRET'] = config('CLIENT_SECRET')
os.environ['SPOTIPY_REDIRECT_URI'] = config('REDIRECT_URI')
token = util.prompt_for_user_token('jdgs.gt','playlist-modify-public')

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth=token)

def get_artist_id(name):
    '''Get an artist ID.'''
    artist = sp.search(q='artist:'+name, type='artist')

    return artist['artists']['items'][0]['id']

def get_albums(artist_id):
    '''Get an artist discography (full songs with features).'''
    albums = sp.artist_albums(artist_id, album_type='album', country='US')['items']
    discography = []
    for album in albums:
        tracks = get_album_tracks(album['id'], album['name'])
        features = get_track_features(tracks)
        full = merge_tracks_features(tracks, features)
        discography.append(full)
        time.sleep(1)

    return discography

def get_album_tracks(album_id, album_name):
    '''Get all tracks from an album.'''
    album_tracks = sp.album_tracks(album_id)['items']

    return [{'id': t['id'], 'name': t['name'], 'album': album_name, 'artist': t['artists'][0]['name']} 
    for t in album_tracks]

def get_track_features(tracks):
    '''Get features of a track.'''
    track_ids = [track['id'] for track in tracks]
    features = sp.audio_features(tracks=track_ids)

    return features

def merge_tracks_features(tracks, features):
    '''Merge track info and track features.'''
    merged = [{**track, **features[i]} for i, track in enumerate(tracks)]

    return merged

def to_dataframe(data):
    '''List of tracks into Pandas dataframe.'''
    dataframes = [pd.DataFrame(album) for album in data]

    return pd.concat(dataframes)

def normalize(df):
    '''Normalize features to avoid bias.'''
    df[['tempo']]= df[['tempo']] / df[['tempo']].max()
    df[['loudness']] = df[['loudness']] / df[['loudness']].min()
    df[['duration_ms']] = df[['duration_ms']] / df[['duration_ms']].max()

    return df

def to_csv(df, name):
    '''Pandas dataframe to csv file.'''
    df.to_csv(name, index=False)

def get_test_tracks(user, playlist_id):
    '''Get tracks (with features) from a playlist, and turn it into a dataframe.'''
    t =  get_playlist_tracks(user, playlist_id)
    t_ids = [track['track']['id'] for track in t]
    t_info = [{'album': track['track']['album']['name'], 'name': track['track']['name']} for track in t]
    t_features = get_test_features(t_ids)

    tracks = [{**track, **t_features[i]} for i, track in enumerate(t_info)]

    return pd.DataFrame(tracks)

def get_test_features(track_ids):
    '''Get features (in chunks) of a playlist songs.'''
    features = []
    batch = 50

    for i in range(0, len(track_ids), batch):
        features = features + sp.audio_features(tracks=track_ids[i:i+batch])

    return features
        
def get_playlist_tracks(username, playlist_id):
    '''Get tracks from a playlist.'''
    results = sp.user_playlist_tracks(username, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    return tracks

def add_songs(playlist_id, track_ids):
    '''Add songs to a playlist (usually the "Results" playlist).'''
    sp.user_playlist_add_tracks('jdgs.gt', playlist_id, track_ids)


# don't run locally.
# when run locally (directly from the command line), this will create the datasets for SW and PT.
# if you want those datasets, go to /data/ or the kaggle repository.
if __name__ == '__main__':
    # steven wilson
    sw_discography = get_albums(get_artist_id('Steven Wilson'))
    sw_dataframe = to_dataframe(sw_discography)
    steven_wilson = normalize(sw_dataframe)
    to_csv(steven_wilson, 'Steven Wilson.csv')

    # porcupine tree
    pt_discography = get_albums(get_artist_id('Porcupine Tree'))
    pt_dataframe = to_dataframe(pt_discography)
    porcupine_tree = normalize(pt_dataframe)
    to_csv(porcupine_tree, 'Porcupine Tree.csv')