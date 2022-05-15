#!/bin/sh

file="$(dirname "$0")/target"
#file="/home/parrot/.config/bin/target"

if [ -s $file ]; then
    echo "%{F#ff0000}什 %{F#ffffff}$(head -n 1 $file)"
else
    echo "%{F#ff0000}ﲅ%{F#ffffff} No target"
fi
