import json
import os
import time

from retrying import retry

from utils.connect import connet_spotify


def main():
    spotify = connet_spotify()
    artist_id = "2DUhXuCbn5RWAkRaKh8qaA"  # フィロソフィーのダンス
    # アルバムの一覧を取得20以上あるときは注意
    res = spotify.artist_albums(artist_id=artist_id, country="JP")
    for album in res["items"]:
        album_name = album["name"]
        tracks = spotify.album_tracks(album_id=album["id"])
        # アルバム+trackをで曲を取得
        for track in tracks["items"]:
            title = track["name"]
            # fileの存在チェック(再ラン用)
            file_path = f"../datas/フィロソフィーのダンス/{album_name}/{title}.json"
            if os.path.exists(file_path):
                continue
            try:
                res = get_analysis(spotify, track["id"])
                # ディレクトリを作っておく
                os.makedirs(f"../datas/フィロソフィーのダンス/{album_name}", exist_ok=True)
                with open(file_path, "w") as file:
                    json.dump(res, file)
                # お行儀
                time.sleep(3)
            except Exception as e:
                continue


@retry(stop_max_delay=10000)
def get_analysis(spotify, track_id):
    return spotify.audio_analysis(track_id)


if __name__ == '__main__':
    main()
