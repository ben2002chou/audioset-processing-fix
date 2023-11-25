import csv
import os

input_csv_path = 'data/unbalanced_train_segments.csv'  # replace with the path to your input CSV
extra_videos_csv_path = 'data/unbalanced_train_segments_extra.csv'  # replace with the path to your output CSV
directory_path = '/grand/EVITA/ben/AudioSet/unbalanced/videos'  # replace with the path to the directory where you're checking for files

# Step 1: Create a set of all the YTIDs from the CSV file
ytids_from_csv = set()
with open(input_csv_path, newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Skip the header row
    for row in reader:
        ytids_from_csv.add(row[0])

# Step 2: Iterate through all the files in the specified directory
# and check if each file's YTID is in the set
extra_ytids = []
for filename in os.listdir(directory_path):
    # Assuming all files are .mp4 and removing the extension to get the YTID
    ytid = filename.replace('.mp4', '')
    if ytid not in ytids_from_csv:
        extra_ytids.append([ytid])

# Step 3: Write any extra YTIDs to a new CSV file
with open(extra_videos_csv_path, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['YTID'])  # Writing header
    writer.writerows(extra_ytids)  # Writing rows

print(f'Extra videos CSV written to {extra_videos_csv_path}')
