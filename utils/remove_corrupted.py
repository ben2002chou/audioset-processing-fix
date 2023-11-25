import pandas as pd
import os

# Load the data from the CSV file into a pandas DataFrame
csv_data = pd.read_csv('/home/ben2002chou/code/audioset-processing-fix/data/unbalanced_train_segments_missing_extraction_dif.csv', header=None, names=['ytid', 'start', 'end', 'labels'])

# Specify the directory where the files are located
directory_path = '/grand/EVITA/ben/AudioSet/unbalanced/videos'

# Iterate through each row in the DataFrame
for index, row in csv_data.iterrows():
    ytid = row['ytid']
    file_path = os.path.join(directory_path, f'{ytid}.mp4')
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'Removed file: {file_path}')
    else:
        print(f'File not found: {file_path}')

