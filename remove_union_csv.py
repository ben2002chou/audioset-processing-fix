import pandas as pd

# Load the data from the CSV files into pandas DataFrames
csv2 = pd.read_csv('/home/ben2002chou/code/audioset-processing-fix/data/balanced_train_segments_missing.csv')
csv1 = pd.read_csv('/home/ben2002chou/code/audioset-processing-fix/data/balanced_train_segments_missing_extraction.csv')

# Find the intersection of the two CSV files
intersection = pd.merge(csv1, csv2, how='inner')

# Now find the rows in csv1 that are not in the intersection
# This will give you the rows that are in csv1 but not in csv2
difference = pd.merge(csv1, intersection, indicator=True, how='outer').query('_merge == "left_only"').drop('_merge', axis=1)
# Write the result to a new CSV file
difference.to_csv('/home/ben2002chou/code/audioset-processing-fix/data/balanced_train_segments_missing_extraction_dif.csv', index=False)
