# Change the current directory to the specified path where the utility scripts are located.
cd /home/ben2002chou/code/audioset-processing-fix/utils

python modify_json_midi.py /home/ben2002chou/code/cav-mae/data/audioset_2m_filtered.json

python modify_json_midi.py /home/ben2002chou/code/cav-mae/data/audioset_20k_filtered.json

python modify_json_midi.py /home/ben2002chou/code/cav-mae/data/audioset_eval_filtered.json