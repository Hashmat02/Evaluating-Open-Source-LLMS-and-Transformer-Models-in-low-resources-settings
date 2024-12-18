import re
import pandas as pd
from tqdm import tqdm
import json

class SQuADCleaner:
    def __init__(self, original_delimiter='&quot;', new_delimiter='••'):
        self.char_map = {
            "–": "--", 
            "—": "--", 
            "″": "", 
            "'": "'", 
            "⁄":"/", 
            "ˈ":"'", 
            """:"", 
            """:"", 
            "\"":"", 
            ";": "؛"
        }
        self.original_delimiter = original_delimiter
        self.new_delimiter = new_delimiter

    def clean_context(self, context):
        """Clean context by replacing special characters"""
        if isinstance(context, str):
            context = [context]
        
        new_context = []
        for text in context:
            for key, value in self.char_map.items():
                text = re.sub(key, value, text)
            new_context.append(text)
        return new_context

    def clean_text(self, text):
        """Clean text by replacing special characters"""
        for key, value in self.char_map.items():
            text = re.sub(key, value, text)
        return text

    def replace_delimiter(self, context):
        """Replace the original delimiter with the new delimiter"""
        if isinstance(context, str):
            context = [context]
        
        new_context = []
        for text in context:
            text = text.replace(self.original_delimiter, self.new_delimiter)
            new_context.append(text)
        return new_context

    def insert_delimiter(self, context, answer_start, answer_length):
        """Insert delimiter around the answer in the context"""
        if isinstance(context, str):
            context = [context]
        
        new_context = []
        if len(context) == 1:
            line = (context[0][:answer_start] + 
                    self.new_delimiter + context[0][answer_start:answer_start + answer_length] + 
                    self.new_delimiter + 
                    context[0][answer_start + answer_length:])
            new_context = [line]
        else:
            idx = -1
            running_length = 0
            while running_length <= answer_start:
                idx += 1
                running_length += len(context[idx])
            
            for i in range(0, idx):
                answer_start -= len(context[i])
            
            for i in range(len(context)):
                if i == idx:
                    line = (context[i][:answer_start] + 
                            self.new_delimiter + 
                            context[i][answer_start:answer_start + answer_length] + 
                            self.new_delimiter + 
                            context[i][answer_start + answer_length:])
                    new_context.append(line)
                else:
                    new_context.append(context[i])
        
        return new_context

    def clean_SQuAD(self, SQuAD_df):
        """Clean and process the SQuAD DataFrame"""
        cleaned_data = []
        if isinstance(SQuAD_df, str):
            try:
                SQuAD_df = pd.DataFrame(json.loads(SQuAD_df))
            except json.JSONDecodeError:
                SQuAD_df = pd.read_json(SQuAD_df)

        if not isinstance(SQuAD_df, pd.DataFrame):
            raise ValueError("Input must be a DataFrame or JSON string")

        for index, row in tqdm(SQuAD_df.iterrows()):
            context = row['context']
            context = self.replace_delimiter(context)
            context = self.clean_context(context)
            answer = self.clean_text(row['answer'])

            cleaned_row = {
                'data_num': index,
                'paragraph_num': 0,  
                'id': row.get('id', index),
                'title': row.get('title', ''),
                'context': context,
                'question': row['question'],
                'answer': answer,
                'is_impossible': row.get('is_impossible', False)
            }
            cleaned_data.append(cleaned_row)

        cleaned_df = pd.DataFrame(cleaned_data)
        return cleaned_df

def main():
    csv_file = "Datasets/SQuAD_Translated_Pashto.csv"
    start_row = 0
    end_row = 150
    cleaner = SQuADCleaner(original_delimiter='&quot;', new_delimiter='••')
    SQuAD = pd.read_csv(csv_file)
    cleaned_df = cleaner.clean_SQuAD(SQuAD)
    

    cleaned_df.to_csv("cleaned_SQuAD_Pashto.csv", index=False)
    print(f"Cleaned data saved. Total rows: {len(cleaned_df)}")

if __name__ == "__main__":
    main()