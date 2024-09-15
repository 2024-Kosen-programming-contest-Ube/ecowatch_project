#!/bin/sh
if [ `id -u` -ne 0 ]; then
  # rootユーザーにしか実行させない
  echo "Please run as root"
  exit 1
fi

TOKEN=`cat ./scripts/token`

git clone https://${TOKEN}@github.com/2024-Kosen-programming-contest-Ube/Device_GetInfoPy.git

cd ./Device_GetInfoPy

python -m venv ./.venv

./.venv/bin/pip install schedule docopt smbus2 gpiozero