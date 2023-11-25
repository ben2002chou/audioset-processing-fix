import csv
import os
import argparse

def file_exists(ytid, directory_path, file_extension):
    file_path = os.path.join(directory_path, f'{ytid}{file_extension}')
    return os.path.isfile(file_path)

def process_csv(input_csv_path, output_csv_path, directory_path, file_extension):
    with open(input_csv_path, newline='', encoding='utf-8') as infile, open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Copy the header row to the output CSV
        header = next(reader)
        writer.writerow(header)
        
        # Iterate over the rows of the input CSV
        for row in reader:
            ytid = row[0]
            if not file_exists(ytid, directory_path, file_extension):
                # If the file does not exist, write the row to the output CSV
                writer.writerow(row)

    print(f'Filtered CSV written to {output_csv_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process a CSV file and remove entries based on file existence.')
    parser.add_argument('input_csv', help='Path to the input CSV file')
    parser.add_argument('output_csv', help='Path to the output CSV file')
    parser.add_argument('directory', help='Path to the directory where audio files are stored')
    parser.add_argument('file_extension', help='File extension to check for (e.g., .mp4, .wav)')

    args = parser.parse_args()

    process_csv(args.input_csv, args.output_csv, args.directory, args.file_extension)
