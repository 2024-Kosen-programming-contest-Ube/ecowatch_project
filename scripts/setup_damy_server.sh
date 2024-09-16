#!/bin/sh
if [ `id -u` -ne 0 ]; then
  # rootユーザーにしか実行させない
  echo "Please run as root"
  exit 1
fi

cd ./damy_server

python -m venv ./.venv

./.venv/bin/pip install fastapi uvicorn