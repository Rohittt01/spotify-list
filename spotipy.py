import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

# Your Spotify API credentials
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
redirect_uri = "http://example.com"  # Should match the one in your Spotify Developer Dashboard

# Create a Spotipy instance with authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="user-library-read"))  # Adjust the scope for your needs

# Example: Print the display name of the current user
current_user = sp.current_user()
print("Logged in as:", current_user['display_name'])
