#!/bin/bash
deactivate
module load conda
# Activate the Conda environment
conda activate youtubedl
cd /home/ben2002chou/code/audioset-processing-fix
# Run your Python script within the activated environment
python3 process.py download-all
