cd /home/ben2002chou/code/audioset-processing-fix/utils

python modify_json_entries.py --file_path /home/ben2002chou/code/cav-mae/data/audioset_20k_filtered_midi.json --data_name wav2 --new_value /some/arbitrary/path --output /home/ben2002chou/code/cav-mae/data/audioset_20k_filtered_piano_roll.json

python modify_json_entries.py --file_path /home/ben2002chou/code/cav-mae/data/audioset_eval_filtered_midi.json --data_name wav2 --new_value /some/arbitrary/path --output /home/ben2002chou/code/cav-mae/data/audioset_eval_filtered_piano_roll.json

python modify_json_entries.py --file_path /home/ben2002chou/code/cav-mae/data/audioset_2m_filtered_midi.json --data_name wav2 --new_value /some/arbitrary/path --output /home/ben2002chou/code/cav-mae/data/audioset_2m_filtered_piano_roll.json
