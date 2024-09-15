#!/bin/sh
if [ `id -u` -ne 0 ]; then
  # rootユーザーにしか実行させない
  echo "Please run as root"
  exit 1
fi

apt-get update
apt-get install -y python git nginx

sh ./scripts/setup_python.sh
sh ./scripts/setup_sensor.sh

python ./scripts/dl_backend.py
python ./scripts/dl_frontend.py
python ./scripts/setup_nginx.py