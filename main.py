import matplotlib.pyplot as plt
from src.data_acquisition import load_data
from src.preprocessing import preprocess
from src.cleaning import clean_data
from src.analysis import analyze_data
from src.modelling import run_model
from src.visualisation import (plot_travel, plot_weekly, plot_weekly_distance, plot_high_trips, plot_scatter, plot_regression,plot_distance_bands, plot_processing_times)
from src.classification import classify_data
from src.compare_processing import compare_processing

if __name__ == "__main__":
    #load and prepare data
    df_distance, df_full, dd_distance, dd_full = load_data()
    df_distance, df_full = preprocess(df_distance, df_full)
    df_distance, df_full = clean_data(df_distance, df_full)
    df_distance = classify_data(df_distance)

    #analysis
    stay_home, travel, weekly_stay_home, weekly_travel, weekly_distance, high_10_25, high_50_100 = analyze_data(df_distance, df_full)

    #modelling
    model, y_pred, X_test, y_test, r2, rmse = run_model(df_distance)

    #serial vs Parallel
    #processing_results = compare_processing()

    # all plots
    plot_travel(stay_home, travel)
    plot_weekly(weekly_stay_home, weekly_travel)
    plot_weekly_distance(weekly_distance)
    plot_high_trips(high_10_25, high_50_100)
    plot_scatter(X_test, y_test)
    plot_regression(X_test, y_test, y_pred)
    plot_distance_bands(df_distance)
    #plot_processing_times(processing_results)
    plt.show()