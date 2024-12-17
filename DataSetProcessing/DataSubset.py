# file_path = "/Users/hashmat/Downloads/train-v2.0-clean.csv" 
# output_path = "SquadSubset.csv" 
import pandas as pd
import random

file_path = "Datasets/SQuAD_Translated_Pashto.csv"
output_path = "smallpashto.csv"
subset_size = 250
data = pd.read_csv(file_path)
subset = data.sample(n=subset_size, random_state=40)
sorted_subset = subset.sort_values(by=['data_num', 'paragraph_num'], ascending=[True, True])
sorted_subset.to_csv(output_path, index=False)
print(f"Random subset of {subset_size} items saved to {output_path}")
