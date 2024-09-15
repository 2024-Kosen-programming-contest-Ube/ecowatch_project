import os
import shutil
import subprocess
import common

SRC_PATH = f"{common.BASE_PATH}/nginx/default"
AVAILABLE = "/etc/nginx/sites-available/procon"
ENABLED = "/etc/nginx/sites-enabled/default"

def setup_nginx():
    common.remove_exists(AVAILABLE)
    shutil.copy(SRC_PATH, AVAILABLE)
    if os.path.islink(ENABLED):
        os.unlink(ENABLED)
    os.symlink(AVAILABLE, ENABLED)

    subprocess.call(["sudo", "systemctl", "restart", "nginx"])