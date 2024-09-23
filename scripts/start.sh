#!/bin/sh
if [ `id -u` -ne 0 ]; then
  # rootユーザーにしか実行させない
  echo "Please run as root"
  exit 1
fi

{
  cd ./Device_GetInfoPy
  ./.venv/bin/python main.py
} &
PID2=$!
echo ${PID2}

trap 'kill ${PID2}' 2 3 15

# 終了待ち
wait