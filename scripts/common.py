import os
import shutil

import os
if os.getuid() != 0:
    print("must be excuted in root")
    exit()

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
GITHUB_TOKEN = ""

with open(f"{BASE_PATH}/scripts/token",'r') as file:
    GITHUB_TOKEN = file.readline()
if not GITHUB_TOKEN.startswith("github"):
    print("Must be set GitHub token in the file named token in scripts dir.")
    exit()


def create_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def remove_exists(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)