import csv
import os

input_csv_path = 'data/unbalanced_train_segments.csv'  # replace with the path to your input CSV
output_csv_path = 'data/unbalanced_train_segments_missing.csv'  # replace with the path to your output CSV
directory_path = '/grand/EVITA/ben/AudioSet/unbalanced/videos'  # replace with the path to the directory where you're checking for files

def file_exists(ytid):
    file_path = os.path.join(directory_path, f'{ytid}.mp4')
    return os.path.isfile(file_path)

with open(input_csv_path, newline='', encoding='utf-8') as infile, open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Copy the header row to the output CSV
    header = next(reader)
    writer.writerow(header)
    
    # Iterate over the rows of the input CSV
    for row in reader:
        ytid = row[0]
        if not file_exists(ytid):  # Modified line
            # If the file does not exist, write the row to the output CSV
            writer.writerow(row)

print(f'Filtered CSV written to {output_csv_path}')
