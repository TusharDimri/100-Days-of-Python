import requests
from bs4 import BeautifulSoup

def get_song_list(date):
    # date = input("Enter the date for which you want to create the playlist for. Format-YYYY-MM-DD: ")
    url = f"https://www.billboard.com/charts/hot-100/{date}"

    response=requests.get(url)
    page = response.text

    soup = BeautifulSoup(page, 'html.parser')
    # print(soup.title)

    song_list = []

    songs = soup.select(selector=".o-chart-results-list__item h3")

    for song in songs:
        # print(song.getText().strip())
        song_list.append(song.getText().strip())

    # print(song_list)
    return song_list

if __name__=="__main__":
    print(get_song_list())