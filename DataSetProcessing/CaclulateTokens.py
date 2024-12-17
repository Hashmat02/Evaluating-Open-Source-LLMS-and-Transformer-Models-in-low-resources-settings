import pandas as pd
import tiktoken

df = pd.read_csv('smallset.csv')
tokenizer = tiktoken.get_encoding("gpt2")  

def calculate_tokens(text):
    return len(tokenizer.encode(text))

def calculate_characters(text):
    return len(text)

total_tokens = 0
total_characters = 0

for index, row in df.iterrows():
    combined_text = f"Context: {row['context']} Question: {row['question']} Answer: {row['answer']}"
    total_tokens += calculate_tokens(combined_text)
    total_characters += calculate_characters(combined_text)

print(f"Total number of tokens: {total_tokens}")
print(f"Total number of characters: {total_characters}")

