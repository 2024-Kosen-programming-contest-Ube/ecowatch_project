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
PID=$!
echo ${PID}

trap 'kill ${PID}' 2 3 15

# 終了待ち
wait ${PID}