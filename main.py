from bs4 import BeautifulSoup
import requests

WEBSITE = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

#get the website data/soup

response = requests.get(WEBSITE)
mtw_page = response.text
soup = BeautifulSoup(mtw_page, "html.parser")

#get the movie headings

movies = soup.find_all(name="h3")
movies_list = [movie.get_text() for movie in reversed(movies)]
print(movies_list)

#write the list

with open(file="movies.txt", mode="w", encoding="utf8") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")

