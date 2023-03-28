from SpotifyClient import SpotifyClient


class TrackManager:
    '''
        Manages properties from tracks, allows retrieval of all informations associated with the track
    '''

    def __init__(self):
        pass

    def get_info(self, tid):
        '''
            Given the id of a track 
            returns audio info on a single track
        '''
        spotify = SpotifyClient('')
        return list(spotify.sp.audio_features(tid)[0].values())[0:11]

    def get_info_list(self, tids):
        '''
            Given the ids of multiple tracks
            returns a list info from each of the songs
        '''
        audio_feature_list = []

        for tid in tids:
            audio_feature_list.append(self.get_info(tid))

        return audio_feature_list

    def get_names(self, tids):
        spotify = SpotifyClient('')
        return [spotify.sp.track(tid)['name'] for tid in tids]
