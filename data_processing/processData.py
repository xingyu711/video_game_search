import pandas as pd

# read data from file
df = pd.read_csv('games.csv')

for index, row in df.iterrows():
    # scale the critic score to range of 0 - 10
    df.at[index, 'Critic_Score'] = row['Critic_Score'] / 10

    # delete records with missing fields
    if pd.isna(row['User_Score']) or pd.isna(row['User_Count']) or pd.isna(row['Critic_Count']) or pd.isna(row['Critic_Score']):
        df.drop(index, inplace=True)

# export as csv file
header = ['Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher', 'Global_Sales', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']
df.to_csv('games_cleaned.csv', index = False, columns = header)