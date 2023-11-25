import pandas as pd
import os
import argparse

def remove__corrupted_files(csv_file_path, directory_path):
    # Load the data from the CSV file into a pandas DataFrame
    csv_data = pd.read_csv(csv_file_path, header=None, names=['ytid', 'start', 'end', 'labels'])

    # Iterate through each row in the DataFrame
    for index, row in csv_data.iterrows():
        ytid = row['ytid']
        file_path = os.path.join(directory_path, f'{ytid}.mp4')
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f'Removed file: {file_path}')
        else:
            print(f'File not found: {file_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove files based on a CSV file listing.')
    parser.add_argument('csv_file', help='Path to the input CSV file')
    parser.add_argument('directory', help='Path to the directory where files are located')

    args = parser.parse_args()

    remove_files(args.csv_file, args.directory)

