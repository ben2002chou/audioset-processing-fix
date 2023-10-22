#!/bin/bash
deactivate
module load conda
# Activate the Conda environment
conda activate youtubedl
cd /home/ben2002chou/code/audioset-processing-fix
# Run your Python script within the activated environment
python3 process_unbalanced_1M.py download-all-multithreaded --offset 9 
conda deactivate
cd /home/ben2002chou/code/cav-mae
source cavmae1017/bin/activate
cd /home/ben2002chou/code/cav-mae/src/preprocess


python3 create_csv.py

python extract_video_frame.py -input_file_list ../../data/video_path.csv -target_fold /grand/EVITA/ben/AudioSet/unbalanced/video_frames 
python extract_audio.py -input_file_list ../../data/video_path.csv -target_fold /grand/EVITA/ben/AudioSet/unbalanced/audio_samples 

# Deactivate the Conda environment once the script completes
conda deactivate
