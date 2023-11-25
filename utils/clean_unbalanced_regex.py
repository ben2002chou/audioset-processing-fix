def clean_csv(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            # Skip header or empty lines
            if line.startswith('#') or not line.strip():
                continue

            # Split the line into components
            parts = line.strip().split(',')

            # Process the positive_labels part
            if len(parts) > 3:
                labels_part = '"' + ','.join(parts[3:]).replace('"', '') + '"'
                parts = parts[:3] + [labels_part]

            # Reconstruct and write the line
            cleaned_line = ','.join(parts)
            outfile.write(cleaned_line + '\n')


# Specify your input and output file paths
input_csv = '/home/ben2002chou/code/audioset-processing-fix/data/unbalanced_train_segments_missing.csv'
output_csv = '/home/ben2002chou/code/audioset-processing-fix/data/unbalanced_train_segments_missing_2.csv'
# Clean the CSV
clean_csv(input_csv, output_csv)
