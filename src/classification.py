import numpy as np

def classify_data(df_distance):
    df_distance['Travel Category'] = np.where(
        df_distance['Population Not Staying at Home'] > df_distance['Population Staying at Home'],
        "High Travel",
        "Low Travel"
    )

    return df_distance