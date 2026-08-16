#!/bin/sh

stdbuf -i0 -o0 -e0 timeout 120 ./simple_calc
#strace -f ./rabbit.elf
