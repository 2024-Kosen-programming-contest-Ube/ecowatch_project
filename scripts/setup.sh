#!/bin/sh
if [ `id -u` -ne 0 ]; then
  # rootユーザーにしか実行させない
  echo "Please run as root"
  exit 1
fi



apt-get update
apt-get install -y python git nginx



sh ./scripts/setup_python.sh