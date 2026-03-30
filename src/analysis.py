import pandas as pd

def analyze_data(df_distance, df_full):
    #original daily averages
    stay_home_avg = df_distance.groupby('Date')['Population Staying at Home'].mean()
    travel_avg = df_distance.groupby('Date')['Population Not Staying at Home'].mean()

    #question a) weekly stats
    df_distance['Week'] = df_distance['Date'].dt.to_period('W')
    weekly_stay_home = df_distance.groupby('Week')['Population Staying at Home'].mean()
    weekly_travel = df_distance.groupby('Week')['Population Not Staying at Home'].mean()
    weekly_distance = df_distance.groupby('Week')[[
        'Number of Trips 1-3', 'Number of Trips 3-5',
        'Number of Trips 5-10', 'Number of Trips 10-25',
        'Number of Trips 25-50', 'Number of Trips 50-100'
    ]].mean()

    #question b) - dates where - 10,000,000 people did 10-25 and 50-100 trips
    high_10_25 = df_full[df_full['Trips 10-25 Miles'] > 10000000]
    high_50_100 = df_full[df_full['Trips 50-100 Miles'] > 10000000]

    return stay_home_avg, travel_avg, weekly_stay_home, weekly_travel, weekly_distance, high_10_25, high_50_100