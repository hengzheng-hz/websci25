import pandas as pd

# File paths
file1 = '/Users/zhenghz/Desktop/data from MC/for test can delete/20210120-0319_most_dem.csv'
file2 = '/Users/zhenghz/Desktop/data from MC/for test can delete/20210120-0319.csv'

# Read the CSV files
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Concatenate the contents  of the first file to the second file
merged_df = pd.concat([df2, df1], ignore_index=True)

# Save the merged content back to the second file
merged_df.to_csv(file2, index=False)

print(f"Merged {file1} into {file2}")