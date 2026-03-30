def clean_data(df_distance, df_full):
    df_full = df_full.drop(columns=[
        'State FIPS', 'State Postal Code',
        'County FIPS', 'County Name'
    ], errors='ignore')

    df_distance = df_distance.fillna(df_distance.mean(numeric_only=True))
    df_full = df_full.fillna(df_full.mean(numeric_only=True))
    df_distance = df_distance.drop_duplicates()
    df_full = df_full.drop_duplicates()

    return df_distance, df_full