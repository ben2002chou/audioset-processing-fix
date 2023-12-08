import pandas as pd

# Load the first CSV file
csv_file_1 = "/home/ben2002chou/code/cav-mae/data/cocochorals/class_labels_indices.csv"
df1 = pd.read_csv(csv_file_1)

# Load the second CSV file
csv_file_2 = "/home/ben2002chou/code/cav-mae/data/class_labels_indices.csv"
df2 = pd.read_csv(csv_file_2)

# Concatenate the two DataFrames
combined_df = pd.concat([df1, df2])

# Reset the index if necessary
combined_df.reset_index(drop=True, inplace=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv(
    "/home/ben2002chou/code/cav-mae/data/cocochorals/class_labels_indices_combined.csv",
    index=False,
)
