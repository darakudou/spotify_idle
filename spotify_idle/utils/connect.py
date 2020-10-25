import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import settings


def connet_spotify():
    """
    spotifyとの接続をするクラス
    :return: Spotify instance
    """
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=settings.SPOTIFY_CLIENT_ID,
                                                           client_secret=settings.SPOTIFY_CLIENT_SECRET))
    return sp
