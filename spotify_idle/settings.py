import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
# 環境変数の読み込み
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
