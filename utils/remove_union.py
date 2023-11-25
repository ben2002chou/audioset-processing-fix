import pandas as pd
import argparse

def process_csv(input_csv1_path, input_csv2_path, output_csv_path):
    # Load the data from the CSV files into pandas DataFrames
    csv1 = pd.read_csv(input_csv1_path)
    csv2 = pd.read_csv(input_csv2_path)

    # Find the intersection of the two CSV files
    intersection = pd.merge(csv1, csv2, how='inner')

    # Find the rows in csv1 that are not in the intersection
    # This gives you the rows that are in csv1 but not in csv2
    difference = pd.merge(csv1, intersection, indicator=True, how='outer').query('_merge == "left_only"').drop('_merge', axis=1)

    # Write the result to a new CSV file
    difference.to_csv(output_csv_path, index=False)

    print(f'Difference CSV written to {output_csv_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find the difference between two CSV files and output the result.')
    parser.add_argument('input_csv1', help='Path to the first input CSV file')
    parser.add_argument('input_csv2', help='Path to the second input CSV file')
    parser.add_argument('output_csv', help='Path to the output CSV file')

    args = parser.parse_args()

    process_csv(args.input_csv1, args.input_csv2, args.output_csv)
