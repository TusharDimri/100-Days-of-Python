from bs4 import BeautifulSoup
import requests

url = "https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(url)
page = response.text

soup = BeautifulSoup(page)

movie_list = []

movies = soup.select(selector=".listicleItem_listicle-item__title__BfenH")
for movie in movies:
    # print(movie.getText())
    movie_list.append(movie.getText())
movie_list.reverse()

with open("100 movies that you must watch.txt", "w") as f:
    for movie in movie_list:
        print(movie)
        f.write(movie)
        f.write("\n")

