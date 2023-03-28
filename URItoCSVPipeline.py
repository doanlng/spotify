from TrackManager import TrackManager
from PlaylistSandbox import PlaylistSandbox
import pandas as pd


class URItoCSVPipeline():
    def __init__(self):
        self.tm = TrackManager()
        self.ps = PlaylistSandbox()

    def uri_to_csv(self, uri, name, label, playlist_names):
        '''
            Takes a list of uris, the name of the csv, and the labels
            produces a csv with songs information from the uri labeled with label with name name
        '''
        csv_name = name + '.csv'

        playlist_tids = [self.ps.get_playlist_from_uri(u) for u in uri]
        # from a list of track ids for each playlist, get the song info

        dfs = []
        for i in range(len(playlist_tids)):
            # now we make this list into a dataframe
            names = self.tm.get_names(playlist_tids[i])
            list_of_stats = self.tm.get_info_list(playlist_tids[i])
            df = self.ps.tracklist_to_df(list_of_stats)
            df['genre'] = label[i]
            df['track_ids'] = names
            df['playlist_name'] = playlist_names[i]
            df.set_index("track_ids", inplace=True)
            dfs.append(df)
        try:
            csv = pd.concat(dfs)
            csv.to_csv(csv_name)
        except Exception as e:
            print(e)
