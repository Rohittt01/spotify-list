from bs4 import BeautifulSoup
import requests
import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()



date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")

# Find the song title using the appropriate selector (you may need to inspect the HTML source to find the correct selector):
songs = soup.select(selector="li ul li h3")

songs_list = []
for song in songs:
    songs_list.append(song.get_text().strip())
# print(songs_list)



# Your Spotify API credentials
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
redirect_uri = "http://example.com"  # Should match the one in your Spotify Developer Dashboard

# Create a Spotipy instance with authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="user-library-read playlist-read-private playlist-modify-private playlist-modify-public"))  # Adjust the scope for your needs

# Example: Print the display name of the current user
current_user = sp.current_user()
print("Logged in as:", current_user['display_name'])
user_id = sp.current_user()["id"]

year = date.split("-")[0]

# Create a playlist
user_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, collaborative=False, description="Billboard 100 Songs")

# Get the playlist ID
playlist_id = user_playlist['id']

# Add tracks to the playlist
track_uris = []  # Store the track URIs to add to the playlist
for song_name in songs_list:
    results = sp.search(q=f"track:{song_name} year:{year}", type='track', limit=1)
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        track_uris.append(track_uri)

# Add the tracks to the playlist
if track_uris:
    sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)
