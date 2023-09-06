from spotipy.oauth2 import SpotifyOAuth
import spotipy



class PlayList:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="user-library-read playlist-read-private playlist-modify-private playlist-modify-public"))  # Adjust the scope for your needs
        
    def user_playlists(self, user_id, date):
        self.user = self.sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, collaborative=False, description="Billboard 100 Songs")
        return self.user