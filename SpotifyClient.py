import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyClient:

    def __init__(self, scope):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id="c194470635e140618aebf4fd2ae02eed",
            client_secret="c825a79915c4468c95a2873a53613c2e",
            redirect_uri="http://localhost:5000/",
            scope=scope
        ))
