#!/bin/bash

while true; do
    socat -dd TCP4-LISTEN:20000,reuseaddr,fork,keepalive exec:./run.sh,end-close
    sleep 5
done