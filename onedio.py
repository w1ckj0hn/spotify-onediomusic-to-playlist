import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def has_int(string):
    return any(char.isdigit() for char in string)


def main():
    r = requests.get("https://onedio.com/genel-kultur/muzik")
    bs = BeautifulSoup(r.text, features="html.parser")
    title = "https://onedio.com"
    for content in bs({"h3": "o-linkbox__overlay"}):
        if "şarkı" in content["title"].lower() and has_int(content["title"]):
            title += content.parent["href"]
            break

    r = requests.get(title)
    bs = BeautifulSoup(r.text, features="html.parser")
    songs = []
    for content in bs({"h2": ""}):
        content = content.get_text()
        content = content.replace("ft.", "ft")
        content = content.split(". ")[1]

        songs.append(content)

    print(songs)

    client_id = ""
    client_secret = ""
    redirect_uri = ""
    playlist_id = ""

    scope = "playlist-modify-public"

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
        )
    )
    playlist = []
    for song in songs:
        results = sp.search(q=song, limit=5)
        result = results["tracks"]["items"]
        if result != []:
            for item in result:

                playlist.append(item["uri"])
                break
        else:
            print(song + " - not found ")

    sp.playlist_add_items(playlist_id, playlist)


if __name__ == "__main__":
    main()
