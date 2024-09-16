import os
import shutil
import requests
import common

FILENAME = f"{common.BASE_PATH}/tmp/ecowatch_backend.zip"

def get_url_from_assets(assets):
    try:
        for asset in assets:
            if asset["name"] == "ecowatch_backend-aarch64-unknown-linux-gnu.zip":
                return asset["browser_download_url"]
    except KeyError as e:
        print(f"データ構造が不一致: {e}")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")

def download(url):
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(FILENAME, 'wb') as file:
            for chunk in res.iter_content(chunk_size=1024):
                file.write(chunk)

def download_backend():
    res = requests.get("https://api.github.com/repos/2024-Kosen-programming-contest-Ube/ecowatch_backend/releases/latest")
    if res.status_code != 200:
        return
    data = res.json()
    assets: list = data["assets"]
    url = get_url_from_assets(assets)
    print(url)

    common.remove_exists(FILENAME)
    common.remove_exists(f"{common.BASE_PATH}/tmp/ecowatch_backend-aarch64-unknown-linux-gnu")
    common.remove_exists(f"{common.BASE_PATH}/ecowatch_backend")
    download(url)
    shutil.unpack_archive(FILENAME, f"{common.BASE_PATH}/tmp")
    os.rename(f"{common.BASE_PATH}/tmp/ecowatch_backend-aarch64-unknown-linux-gnu", f"{common.BASE_PATH}/ecowatch_backend")
    shutil.copy(f"{common.BASE_PATH}/ecowatch_backend/example.env", f"{common.BASE_PATH}/ecowatch_backend/.env")
    os.chmod(f"{common.BASE_PATH}/ecowatch_backend/ecowatch_backend", 0o755)

common.create_dir(f"{common.BASE_PATH}/tmp")
download_backend()
common.remove_exists(f"{common.BASE_PATH}/tmp/ecowatch_backend.zip")
