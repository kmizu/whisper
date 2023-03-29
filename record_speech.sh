#!/bin/sh

target_file=$1

arecord -r 16000 -d 30 -f S16_LE $target_file
