import os
import pandas as pd

data_dir = "path/to/dat/files"
output_csv = "merged_data.csv"

#List all .dat files in the directory
dat_files = [f for f in os.listdir(data_dir) if f.endswith('.dat')]

all_data = []

for file in dat_files:
    file_path = os.path.join(data_dir, file)

#Adjust the separator based on your file format (',' for CSV, '\s+' for space-separated)
    df = pd.read_csv(file_path, sep=" ", header=None)  # Change separator as needed
    all_data.append(df)

#Merge all data into a single DataFrame
merged_df = pd.concat(all_data, ignore_index=True)

#Save to CSV
merged_df.to_csv(output_csv, index=False)
print(f"Saved to {output_csv}")