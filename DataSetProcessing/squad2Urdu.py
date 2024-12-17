from datasets import load_dataset
import pandas as pd

ds = load_dataset("uqa/UQA")

with pd.ExcelWriter("uqa_data.xlsx") as writer:
    if 'train' in ds:
        train_df = pd.DataFrame(ds['train'])
        train_df.to_excel(writer, sheet_name="train", index=False)  

    if 'test' in ds:
        test_df = pd.DataFrame(ds['test'])
        test_df.to_excel(writer, sheet_name="test", index=False) 

    if 'validation' in ds:
        validation_df = pd.DataFrame(ds['validation'])
        validation_df.to_excel(writer, sheet_name="validation", index=False)  

print("Data saved as uqa_data.xlsx with separate sheets for train, test, and validation.")
