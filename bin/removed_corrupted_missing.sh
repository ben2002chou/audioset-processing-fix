# Change the current directory to the specified path where the utility scripts are located.
cd /home/ben2002chou/code/audioset-processing-fix/utils

# Run the 'find_missing_files.py' script to identify missing .mp4 video files.
# Arguments:
# 1. Path to the input CSV file containing data about the segments.
# 2. Path to the output CSV file where missing segments will be listed.
# 3. Directory where the video files are supposed to be located.
# 4. File extension to look for, in this case, .mp4 for video files.
python find_missing_files.py data/unbalanced_train_segments.csv data/unbalanced_train_segments_missing.csv /grand/EVITA/ben/AudioSet/unbalanced/videos .mp4

# Run the 'find_missing_files.py' script to identify missing .wav audio files.
# Arguments are similar to the previous command, but this time for audio samples.
python find_missing_files.py data/unbalanced_train_segments.csv data/unbalanced_train_segments_missing_extraction.csv /grand/EVITA/ben/AudioSet/unbalanced/audio_samples .wav

# Run the 'remove_union.py' script. This script creates a csv file containing the difference of two csv files.
# 1. Path to the first CSV file (possibly with entries to be removed).
# 2. Path to the second CSV file (entries here will be used for comparison).
# 3. Path to the output CSV file where the difference of the first two will be saved.
python remove_union.py /home/ben2002chou/code/audioset-processing-fix/data/unbalanced_train_segments_missing.csv /home/ben2002chou/code/audioset-processing-fix/data/unbalanced_train_segments_missing_extraction.csv /home/ben2002chou/code/audioset-processing-fix/data/unbalanced_train_segments_missing_extraction_dif.csv

# Run the 'remove_corrupted_files.py' script. This script removes corrupted files that were not extracted properly. 
# 1. Path to the CSV file generated from "remove_union.py" script.
# 2. Directory where the files are located and from where corrupted files will be removed.
python remove_corrupted_files.py /home/ben2002chou/code/audioset-processing-fix/data/unbalanced_train_segments_missing_extraction_dif.csv /grand/EVITA/ben/AudioSet/unbalanced/videos

# update training datafiles (json format) after corrrupted files are removed
# 1. Path to the original json file
# 2. Path to the output json file
# 3. Directory where the files are located
python update_datafiles.py /home/ben2002chou/code/cav-mae/data/audioset_2m_cleaned_2023.json /home/ben2002chou/code/cav-mae/data/audioset_2m_filtered.json /grand/EVITA/ben/AudioSet/unbalanced/videos