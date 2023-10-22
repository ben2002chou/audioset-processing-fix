#!/bin/bash
cd /grand/EVITA/ben/AudioSet/balanced/videos

for file in /grand/EVITA/ben/AudioSet/eval/videos*; do
    if [ -f "$file" ]; then
        rm -f "${file##*/}"
    fi
done
