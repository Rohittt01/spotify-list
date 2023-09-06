from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/2018-10-13/"

response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")

# Find the song title using the appropriate selector (you may need to inspect the HTML source to find the correct selector):
song = soup.find_all("h3", class_="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")

if song:
    print(song.text)
else:
    print("Song not found")

# You might need to adjust the class name "your-correct-class-name" to match the actual class name in the current HTML structure.
