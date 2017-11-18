import pandas as pd
import lyricwikia 

sw = pd.read_csv('Steven Wilson.csv')
pt = pd.read_csv('Porcupine Tree.csv')

sw_songs = sw['name']
pt_songs = pt['name']

sw_lyrics = []
pt_lyrics = []

for song in sw_songs:
    try:
        lyrics = lyricwikia.get_lyrics('Steven Wilson', song)
        clean = lyrics.replace('\n', ' ').replace('spoken:', '').strip().lower()
        sw_lyrics.append(clean)
    except:
        sw_lyrics.append('')

for song in pt_songs:
    try:
        lyrics = lyricwikia.get_lyrics('Porcupine Tree', song)
        clean = lyrics.replace('\n', ' ').strip().lower()
        pt_lyrics.append(clean)
        print(pt_lyrics)
    except:
        pt_lyrics.append('')

sw['lyrics'] = sw_lyrics
pt['lyrics'] = pt_lyrics
sw.to_csv('SW Ly.csv', index=False)
pt.to_csv('PT Ly.csv', index=False)