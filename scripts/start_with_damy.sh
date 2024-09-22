#!/bin/sh
if [ `id -u` -ne 0 ]; then
  # rootユーザーにしか実行させない
  echo "Please run as root"
  exit 1
fi

{
  cd ./damy_server
  ./.venv/bin/uvicorn server:app --port 5000
} &
PID2=$!
echo ${PID2}

trap 'kill -2 ${PID2}' 2 3 15

# 終了待ち
wait