from PlaylistSandbox import PlaylistSandbox
from TrackManager import TrackManager
import pandas as pd
from MDSVisualizer import MDSVisualizer
from SpotifyClient import SpotifyClient
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from numpy.linalg import norm


def main():
    '''
    {'danceability': 0.852, 'energy': 0.762, 'key': 6, 'loudness': -4.448, 'mode': 0, 'speechiness': 0.0487, 'acousticness': 0.333, 'instrumentalness': 1.66e-06, 'liveness': 0.159, 'valence': 0.907, 'tempo': 131.958, 
    'type': 'audio_features', 'id': '2xeaHUnzzT5Kc974OQt1kA', 'uri': 'spotify:track:2xeaHUnzzT5Kc974OQt1kA', 'track_href': 'https://api.spotify.com/v1/tracks/2xeaHUnzzT5Kc974OQt1kA', 
    'analysis_url': 'https://api.spotify.com/v1/audio-analysis/2xeaHUnzzT5Kc974OQt1kA', 'duration_ms': 139213, 'time_signature': 4}
    '''

    playlist_obj = PlaylistSandbox()
    tm = TrackManager()
    spotify = SpotifyClient('')

    '''
    # playlist_obj.update_currents()

    currents = playlist_obj.get_currents()

    # dummy_track_id = '2xeaHUnzzT5Kc974OQt1kA'
    '''

    # print(tm.get_info(dummy_track_id))
    # print(tm.get_info_list(currents))
    '''
    currents_song_info = tm.get_info_list(currents)
    df = pd.DataFrame(currents_song_info, columns=['danceability', 'energy', 'key', 'loudness', 'mode',
                                                   'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'])
    df['track_ids'] = currents
    df.set_index("track_ids", inplace=True)
    df.to_csv('currents_info')
    '''

    #df = pd.read_csv('currents_info.csv')

    # print(spotify.sp.track('2xeaHUnzzT5Kc974OQt1kA')['name'])
    #print(df.iloc[:, 1:])
    #print((df.iloc[:, 0]))
    #labels = tm.get_names(df.iloc[:, 0])
    # print(labels)
    #vis = MDSVisualizer(df.iloc[:, 1:], labels)
    # vis.mds()

    #t1 = df.iloc[0, 1:]
    #t2 = df.iloc[1, 1:]
    #print('t1 is ' + labels[0])
    #print('t2 is ' + labels[1])
    # print('Cosine similarity between the 2 ' +
    #      cosine_similarity(, ))
    #t1_stats = np.array(t1)
    #t2_stats = np.array(t2)
    #cosine = np.dot(t1_stats, t2_stats)/(norm(t1_stats)*norm(t2_stats))
    # print(cosine)


if __name__ == "__main__":
    main()
