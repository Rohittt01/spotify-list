from bs4 import BeautifulSoup
import requests
year = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{year}/"

response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")

# Find the song title using the appropriate selector (you may need to inspect the HTML source to find the correct selector):
songs = soup.select(selector="li ul li h3")

songs_list = []
for song in songs:
    songs_list.append(song.get_text().strip())
# print(songs_list)
# You might need to adjust the class name "your-correct-class-name" to match the actual class name in the current HTML structure.
