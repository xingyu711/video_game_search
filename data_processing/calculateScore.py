import pandas as pd

# initializing variables to store min and max for target fields
minYear = float('inf')
maxYear = float('-inf')

minUserCount = float('inf')
maxUserCount = float('-inf')

minUserScore = float('inf')
maxUserScore = float('-inf')

minCriticCount = float('inf')
maxCriticCount = float('-inf')

minCriticScore = float('inf')
maxCriticScore = float('-inf')

minSales = float('inf')
maxSales = float('-inf')

# read data from file
df = pd.read_csv('games_cleaned.csv')

# find min and max for target fields
for index, row in df.iterrows():
    minYear = min(minYear, row['Year_of_Release'])
    maxYear = max(maxYear, row['Year_of_Release'])

    minUserCount = min(minUserCount, row['User_Count'])
    maxUserCount = max(maxUserCount, row['User_Count'])

    minUserScore = min(minUserScore, row['User_Score'])
    maxUserScore = max(maxUserScore, row['User_Score'])

    minCriticCount = min(minCriticCount, row['Critic_Count'])
    maxCriticCount = max(maxCriticCount, row['Critic_Count'])

    minCriticScore = min(minCriticScore, row['Critic_Score'])
    maxCriticScore = max(maxCriticScore, row['Critic_Score'])

    minSales = min(minSales, row['Global_Sales'])
    maxSales = max(maxSales, row['Global_Sales'])

# normalization formula: (X - min) / (max - min)
df['Game_Score'] = ''
for index, row in df.iterrows():
    # calculate normalized values
    yearNormalized = (row['Year_of_Release'] - minYear) / (maxYear - minYear)
    userCountNormalized = (row['User_Count'] - minUserCount) / (maxUserCount - minUserCount)
    userScoreNormalized = (row['User_Score'] - minUserScore) / (maxUserScore - minUserScore)
    criticCountNormalized = (row['Critic_Count'] - minCriticCount) / (maxCriticCount - minCriticCount)
    criticScoreNormalized = (row['Critic_Score'] - minCriticScore) / (maxCriticScore - minCriticScore)
    salesNormalized = (row['Global_Sales'] - minSales) / (maxSales - minSales)

    # calculate the quality/game score for each record
    score = (yearNormalized * 0.15) + (userCountNormalized * 0.15) + (userScoreNormalized * 0.20) + (criticCountNormalized * 0.15) + (criticScoreNormalized * 0.15) + (salesNormalized * 0.2)

    # scale the game scores
    # original game scores: 0.1 - 0.7
    # the query scores from ElasticSearch: typically 5 - 30
    # Scale up the game score by a factor of 45 to make the two scores comparable
    score = score * 45

    # save the scaled score
    df.at[index, 'Game_Score'] = score

# save the results to file
df.to_csv('games_with_score.csv', index=False)

