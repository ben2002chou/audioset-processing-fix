#!/bin/bash
set -x
deactivate
module load conda
cd /home/ben2002chou/code/cav-mae
source cavmae1017/bin/activate
module load ffmpeg

cd /home/ben2002chou/code/cav-mae/src/preprocess

python extract_video_frame.py -input_file_list /home/ben2002chou/code/cav-mae/data/video_path_unbalanced.csv -target_fold /grand/EVITA/ben/AudioSet/unbalanced/video_frames 

# Deactivate the Conda environment once the script completes
conda deactivate

#find . -type f 2>/dev/null | wc -l

