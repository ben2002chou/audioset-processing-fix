cd /home/ben2002chou/code/audioset-processing-fix/utils
python combine_json.py /home/ben2002chou/code/cav-mae/data/audioset_2m_filtered_piano_roll.json /home/ben2002chou/code/cav-mae/data/cocochorals/cocochorals_train.json /home/ben2002chou/code/cav-mae/data/cocochorals/audioset_2m_cocochorals_train.json
python combine_json.py /home/ben2002chou/code/cav-mae/data/audioset_eval_filtered_piano_roll.json /home/ben2002chou/code/cav-mae/data/cocochorals/cocochorals_valid.json /home/ben2002chou/code/cav-mae/data/cocochorals/audioset_eval_cocochorals_valid.json
python combine_json.py /home/ben2002chou/code/cav-mae/data/audioset_20k_filtered_piano_roll.json /home/ben2002chou/code/cav-mae/data/cocochorals/cocochorals_test.json /home/ben2002chou/code/cav-mae/data/cocochorals/audioset_20k_cocochorals_test.json