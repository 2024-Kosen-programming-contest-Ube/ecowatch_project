import os
import sys
import shutil
import subprocess
import common

SRC_PATH = f"{common.BASE_PATH}/services/ecowatch.service"
SRC_damy_PATH = f"{common.BASE_PATH}/services/ecowatch_damy.service"
DEST_PATH = f"/usr/lib/systemd/system/ecowatch.service"
DEST_damy_PATH = f"/usr/lib/systemd/system/ecowatch_damy.service"


def setup_nginx():
    os.chmod(f"{common.BASE_PATH}/scripts/start.sh", 0o755)
    os.chmod(f"{common.BASE_PATH}/scripts/start_with_damy.sh", 0o755)

    args = sys.argv
    common.remove_exists(DEST_PATH)
    common.remove_exists(DEST_damy_PATH)

    shutil.copy(SRC_PATH, DEST_PATH)
    shutil.copy(SRC_damy_PATH, DEST_damy_PATH)

    if args[1] == "damy":
        print("Enabled damy servie")
        subprocess.call(["sudo", "systemctl", "stop", "ecowatch.service"])
        subprocess.call(["sudo", "systemctl", "disable", "ecowatch.service"])
        subprocess.call(["sudo", "systemctl", "enable",
                        "ecowatch_damy.service"])
        subprocess.call(["sudo", "systemctl", "start",
                        "ecowatch_damy.service"])
    else:
        print("Enabled servie")
        subprocess.call(["sudo", "systemctl", "stop",
                        "ecowatch_damy.service"])
        subprocess.call(["sudo", "systemctl", "disable",
                        "ecowatch_damy.service"])
        subprocess.call(["sudo", "systemctl", "enable", "ecowatch.service"])
        subprocess.call(["sudo", "systemctl", "start", "ecowatch.service"])


setup_nginx()
