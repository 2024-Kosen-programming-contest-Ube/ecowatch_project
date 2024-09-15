import shutil
import requests
import common

def get_urls_from_assets(assets):
    urls = []
    try:
        for asset in assets:
            if asset["name"] == "ecowatch_classroom.zip" or asset["name"] == "ecowatch_student.zip" or asset["name"] == "ecowatch_teacher.zip":
                urls.append((asset["name"], asset["browser_download_url"]))
        return urls
    except KeyError as e:
        print(f"データ構造が不一致: {e}")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")

def download(file_url):
    filename = f"{common.BASE_PATH}/tmp/{file_url[0]}"
    common.remove_exists(filename)

    res = requests.get(file_url[1], stream=True)
    if res.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in res.iter_content(chunk_size=1024):
                file.write(chunk)

        shutil.unpack_archive(filename, f"{common.BASE_PATH}/tmp")
        unziped = file_url[0].replace(".zip", "")
        shutil.move(f"{common.BASE_PATH}/tmp/{unziped}", f"/var/www/html/{unziped}")
        common.remove_exists(filename)


def download_frontend():
    res = requests.get("https://api.github.com/repos/2024-Kosen-programming-contest-Ube/ecowatch/releases/latest")
    if res.status_code != 200:
        return
    data = res.json()
    # print(data)
    assets: list = data["assets"]
    urls = get_urls_from_assets(assets)

    common.create_dir(f"{common.BASE_PATH}/tmp")
    common.remove_exists("/var/www/html")
    common.create_dir(f"/var/www/html")
    for file_url in urls:
        download(file_url)
    # print(urls)
    return

download_frontend()