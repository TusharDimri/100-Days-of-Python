import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import billboard

load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URL = os.environ.get("REDIRECT_URL")



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path=".cache", 
    )
)
'''
# Alternative Method:
o_auth = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL, scope="playlist-modify-private", cache_path=".cache")
sp=spotipy.Spotify(auth_manager=o_auth)
# print(sp.current_user())
'''

def get_song_uri(date):
    spotify_song_list = []
    year = date.split("-")[0]
    songs = billboard.get_song_list(date)
    for song in songs:
        spotify_search=sp.search(q=f"track:{song} year:{year}", type="track")
        try:
            uri = spotify_search["tracks"]["items"][0]["uri"]
            spotify_song_list.append(uri)
            print(f"{uri} added to the list. Song Name: {song}")
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
    return spotify_song_list

def add_to_playlist(date="2012-07-19"):
    id = sp.current_user()["id"]
    song_list = get_song_uri(date)
    playlist = sp.user_playlist_create(user=id, name=f"{date} Billboard Hot 100", public=False)
    sp.user_playlist_add_tracks(user=id, playlist_id=playlist["id"], tracks=song_list) 
    print("Playlist Created")
