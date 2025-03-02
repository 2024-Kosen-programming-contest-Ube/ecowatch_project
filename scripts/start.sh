#!/bin/sh
if [ `id -u` -ne 0 ]; then
  # rootユーザーにしか実行させない
  echo "Please run as root"
  exit 1
fi

CURRENT=$(cd $(dirname $0);pwd)
cd ${CURRENT}/..

{
  cd ./ecowatch_backend
  ./ecowatch_backend
} &
PID1=$!
echo ${PID1}

{
  cd ./Device_GetInfoPy
  ./.venv/bin/python main.py
} &
PID2=$!
echo ${PID2}

trap 'kill ${PID1};kill ${PID2}' 2 3 15

# 終了待ち
wait