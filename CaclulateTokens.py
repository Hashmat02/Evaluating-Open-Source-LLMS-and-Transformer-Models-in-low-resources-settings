import pandas as pd
import tiktoken

# Load your CSV file into a pandas DataFrame
df = pd.read_csv('smallset.csv')

# Initialize the OpenAI tokenizer for GPT-2 (which works for GPT models)
tokenizer = tiktoken.get_encoding("gpt2")  # Use 'gpt2' as the encoding for GPT models

# Function to calculate tokens for a single text entry
def calculate_tokens(text):
    return len(tokenizer.encode(text))

# Function to calculate the number of characters for a single text entry
def calculate_characters(text):
    return len(text)

# Initialize counters for total tokens and total characters
total_tokens = 0
total_characters = 0

# Iterate over the rows of the dataset and calculate the tokens and characters
for index, row in df.iterrows():
    # Combine context, question, and answer text for tokenization
    combined_text = f"Context: {row['context']} Question: {row['question']} Answer: {row['answer']}"
    
    # Calculate tokens for this combined text
    total_tokens += calculate_tokens(combined_text)
    
    # Calculate characters for this combined text
    total_characters += calculate_characters(combined_text)

# Print the total number of tokens and characters
print(f"Total number of tokens: {total_tokens}")
print(f"Total number of characters: {total_characters}")

