import pandas as pd

english_df = pd.read_excel('/Users/hashmat/Desktop/LLM project/squad2_English.xlsx')
urdu_df = pd.read_excel('/Users/hashmat/Desktop/LLM project/squad2_Urdu.xlsx')

merged_df = pd.merge(english_df, urdu_df, on='id', suffixes=('_English', '_Urdu'))
print("Columns after merging:", merged_df.columns)

sampled_df = merged_df.sample(n=20, random_state=66)

final_df = pd.DataFrame({
    'ID': sampled_df['id'],
    'English Question': sampled_df['question_English'], 
    'English Answer': sampled_df['answers'],  
    'English Title': sampled_df['title_English'],  
    'English Context': sampled_df['context_English'], 
    'Urdu Question': sampled_df['question_Urdu'], 
    'Urdu Answer': sampled_df['answer'],  
    'Urdu Title': sampled_df['title_Urdu'],  
    'Urdu Context': sampled_df['context_Urdu']  
})

final_df.to_excel('/Users/hashmat/Desktop/LLM project/squad2_English_Urdu_Pairs.xlsx', index=False)

print("New Excel file 'squad2_English_Urdu_Pairs.xlsx' created with 20 randomly selected question pairs.")
