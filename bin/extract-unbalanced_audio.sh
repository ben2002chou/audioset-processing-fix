#!/bin/bash
set -x
deactivate
module load conda
conda activate youtubedl
module load ffmpeg

cd /home/ben2002chou/code/cav-mae/src/preprocess

python extract_audio.py -input_file_list /home/ben2002chou/code/cav-mae/data/video_path_unbalanced.csv -target_fold /grand/EVITA/ben/AudioSet/unbalanced/audio_samples 

# Deactivate the Conda environment once the script completes
conda deactivate

#find . -type f 2>/dev/null | wc -l

