## spotify-onediomusic-to-playlist
Onedio müziğin günlük olarak paylaştığı şarkı listelerini spotify playlistine atan ufak bir araç

## Kullanım
```sh
# Repoyu klonla
$ git clone github.com/w1ckj0hn/spotify-onediomusic-to-playlist

# Reponun dizinine git
$ cd spotify-onediomusic-to-playlist

# requirements.txt'yi indir
$ pip install -r requirements.txt
```

```python
# Bu değişkenleri kendine göre ayarla
client_id = ""
client_secret = ""
redirect_uri = ""
playlist_id = ""
```

```sh
# Aracı kullanmaya başla
$ python onedio.py
```