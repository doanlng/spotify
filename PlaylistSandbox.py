from SpotifyClient import SpotifyClient
import datetime
import re
import pandas as pd


class PlaylistSandbox:
    '''
        The purpose of playlist sandbox is to play around with spotipy docs to automate a playlist creation and updates
        As it stands, we have a playlist that holds the top short term songs that constantly updates itself with a new date
        Everytime a new date is added, new songs will replace the old ones.

        Replacement happens when:
            - a song is in the new top tracks for that date
            - said song is not already in the playlist


    '''

    def __init__(self):
        pass

    def update_currents(self):
        '''
            updates the currents_* playlist in spotify with the short term top tracks
        '''
        try:
            # open spotify gateway
            spotify = SpotifyClient(
                ['user-top-read', 'playlist-modify-public', 'playlist-read-private', 'playlist-modify-private'])
            results = spotify.sp.current_user_top_tracks(
                time_range='short_term', limit=15)
            songs_to_add = []
            for i, item in enumerate(results['items']):
                # print(i, item['name'], 'by', item['artists'][0]['name'])
                songs_to_add.append(item['id'])
                # print(item['id'])

            date = datetime.date.today().strftime("%B%Y")
            playlist_name = "currents_" + date
            user_id = spotify.sp.me()['id']

            # Find the playlist we are going to be updating if it exists
            pid = None
            for item in spotify.sp.current_user_playlists()['items']:

                # Playlist is found among other user playlists
                if (re.search("^currents", item['name']) is not None):
                    # print(item['name'])
                    pid = item['id']
                    spotify.sp.playlist_change_details(pid, name=playlist_name)
                    break

            if pid is None:
                spotify.sp.user_playlist_create(user_id, name=playlist_name)
            else:
                current_songs_in_playlist = [
                    song['track']['id'] for song in spotify.sp.playlist_items(pid)['items']]
                # print(current_songs_in_playlist)

                songs_to_remove = [
                    tid for tid in current_songs_in_playlist if tid not in songs_to_add]

                spotify.sp.playlist_remove_all_occurrences_of_items(
                    pid, songs_to_remove)

                print(str(len(songs_to_remove)) + ' song(s) removed')

                songs_to_add = [
                    tid for tid in songs_to_add if tid not in current_songs_in_playlist]

            print(str(len(songs_to_add)) + ' song(s) added')

            if len(songs_to_add) > 0:
                spotify.sp.playlist_add_items(pid, songs_to_add)

        except Exception as e:
            print(e)

    def get_currents(self):
        '''
            Returns a list of track ids that are associated with the currents_ playlist
        '''
        try:
            spotify = SpotifyClient(['playlist-read-private'])
            for playlist in spotify.sp.current_user_playlists()['items']:
                if (re.search("^currents", playlist['name']) is not None):
                    songs = [song['track']['id']
                             for song in spotify.sp.playlist_items(playlist['id'])['items']]
                    break
            return songs if len(songs) > 0 else None

        except Exception as e:
            print(e)

    def get_playlist_from_uri(self, uri):
        '''
            Returns a list of track ids that are associated the playlist from a uri
        '''
        try:
            spotify = SpotifyClient([''])
            playlist_uri = uri.split("/")[-1].split('?')[0]
            tids = [x["track"]["id"]
                    for x in spotify.sp.playlist_tracks(playlist_uri)['items']]
            return tids

        except Exception as e:
            print(e)

    def tracklist_to_df(self, list):
        return pd.DataFrame(list, columns=['danceability', 'energy', 'key', 'loudness', 'mode',
                                           'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'])
