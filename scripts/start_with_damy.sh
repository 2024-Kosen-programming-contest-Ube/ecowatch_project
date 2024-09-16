#!/bin/sh
if [ `id -u` -ne 0 ]; then
  # rootユーザーにしか実行させない
  echo "Please run as root"
  exit 1
fi

{
  cd ./ecowatch_backend
  ./ecowatch_backend
} &
PID1=$!
echo ${PID1}

{
  cd ./damy_server
  ./.venv/bin/uvicorn server:app --port 5000
} &
PID2=$!
echo ${PID2}

trap 'kill ${PID1};kill -2 ${PID2}' 2 3 15

# 終了待ち
wait