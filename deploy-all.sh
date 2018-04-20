#!/bin/bash

if [ "$#" != 1 ]; then
  echo >&2 "Deploys srcomp-kiosk to hostnames given in filename (- for stdin)"
  echo >&2 "Usage: $0 <filename>"
  exit 1
fi

filename="$1"

if [ "$filename" = "-" ]; then
  filename=/dev/stdin
fi

while read -r line; do
  ssh pi@"$line" './srcomp-kiosk/scripts/update && echo Done || echo Failed'
done < "$filename"
