#!/bin/bash
deactivate
module load conda
cd /home/ben2002chou/code/cav-mae
source cavmae1017/bin/activate
cd /home/ben2002chou/code/cav-mae/src/preprocess


python3 create_csv_eval.py

python extract_video_frame.py -input_file_list /home/ben2002chou/code/cav-mae/data/video_path_eval.csv -target_fold /grand/EVITA/ben/AudioSet/eval/video_frames 
python extract_audio.py -input_file_list /home/ben2002chou/code/cav-mae/data/video_path_eval.csv -target_fold /grand/EVITA/ben/AudioSet/eval/audio_samples 

# Deactivate the Conda environment once the script completes
conda deactivate

#find . -type f 2>/dev/null | wc -l