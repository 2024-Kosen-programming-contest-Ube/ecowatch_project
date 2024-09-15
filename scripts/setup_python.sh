#!/bin/sh
if [ `id -u` -ne 0 ]; then
  # rootユーザーにしか実行させない
  echo "Please run as root"
  exit 1
fi

pip install --break-system-packages requests