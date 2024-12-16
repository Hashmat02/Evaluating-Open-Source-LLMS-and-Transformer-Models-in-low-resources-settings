import pandas as pd

file_path = '/Users/hashmat/Desktop/LLM project/squad2_English.xlsx'
sheets = ['train', 'validation']  
total_characters = 0 

for sheet in sheets:
    df = pd.read_excel(file_path, sheet_name=sheet)
    
    text_columns = ['title', 'context', 'question', 'answers']
    missing_columns = [col for col in text_columns if col not in df.columns]
    if missing_columns:
        print(f"Missing columns in sheet '{sheet}': {missing_columns}")
        continue
    
    sheet_character_count = df[text_columns].fillna('').applymap(len).sum().sum()
    print(f"Total characters in sheet '{sheet}': {sheet_character_count}")
    total_characters += sheet_character_count

# Final output
print(f"Total characters across all sheets: {total_characters}")
