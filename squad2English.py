from datasets import load_dataset
import pandas as pd

ds = load_dataset("rajpurkar/squad_v2")

with pd.ExcelWriter("squad_v2_data.xlsx") as writer:
    if 'train' in ds:
        train_df = pd.DataFrame(ds['train'])
        train_df.to_excel(writer, sheet_name="train", index=False)  

    if 'validation' in ds:
        validation_df = pd.DataFrame(ds['validation'])
        validation_df.to_excel(writer, sheet_name="validation", index=False)  

print("SQuAD 2.0 data saved as squad_v2_data_english.xlsx with separate sheets for train and validation.")
