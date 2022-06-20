#!/usr/bin/env sh

URL="127.0.0.1:3000"

curl "${URL}"

curl -d "@form_data1.json" -H "Content-Type: application/json" "${URL}"

curl -d "@form_data2.json" -X PUT -H "Content-Type: application/json" "${URL}"
