import requests
from bs4 import BeautifulSoup

url = "https://tmdb-imdb-ultimate-1-million-movies.p.rapidapi.com/list"

payload = {}
headers = {
	"x-rapidapi-key": "aac6f1acddmsh79b3521592e753ep17d289jsn909d67c3187f",
	"x-rapidapi-host": "tmdb-imdb-ultimate-1-million-movies.p.rapidapi.com",
	"Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=payload, headers=headers)


soup=BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())