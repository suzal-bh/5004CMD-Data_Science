import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

def plot_travel(stay_home, travel):
    plt.figure(figsize=(12, 5))
    plt.plot(stay_home.index.astype(str), stay_home.values, label='Stay Home')
    plt.plot(travel.index.astype(str), travel.values, label='Travel')
    plt.legend()
    plt.title("Travel vs Stay Home (Daily)")
    plt.xlabel("Date")
    plt.ylabel("Population")
    ax = plt.gca()
    ticks = ax.get_xticks()
    ax.set_xticks(ticks[::30])
    plt.xticks(rotation=45)
    plt.tight_layout()

def plot_weekly(weekly_stay_home, weekly_travel):
    plt.figure(figsize=(12, 5))
    plt.plot(weekly_stay_home.index.astype(str), weekly_stay_home.values, label='Stay Home')
    plt.plot(weekly_travel.index.astype(str), weekly_travel.values, label='Travel')
    plt.legend()
    plt.title("Question a: Weekly Stay Home vs Travel Population")
    plt.xlabel("Week")
    plt.ylabel("Average Population")
    ax = plt.gca()
    ticks = ax.get_xticks()
    ax.set_xticks(ticks[::10])
    plt.xticks(rotation=45)
    plt.tight_layout()

def plot_weekly_distance(weekly_distance):
    plt.figure(figsize=(12, 5))
    for col in weekly_distance.columns:
        plt.plot(weekly_distance.index.astype(str), weekly_distance[col], label=col)
    plt.legend(fontsize=7)
    plt.title("Question a: Weekly Average Trips by Distance Band")
    plt.xlabel("Week")
    plt.ylabel("Average Number of Trips")
    #only show every 10th week label
    ax = plt.gca()
    ticks = ax.get_xticks()
    ax.set_xticks(ticks[::10])
    plt.xticks(rotation=45)
    plt.tight_layout()

def plot_high_trips(high_10_25, high_50_100):
    plt.figure(figsize=(10, 6))
    plt.scatter(high_10_25['Date'], high_10_25['Trips 10-25 Miles'],
                alpha=0.5, label='>10M Trips 10-25 Miles', color='blue')
    plt.scatter(high_50_100['Date'], high_50_100['Trips 50-100 Miles'],
                alpha=0.5, label='>10M Trips 50-100 Miles', color='orange')
    plt.title("Question b: Dates with >10M Trips (10-25 vs 50-100 Miles)")
    plt.xlabel("Date")
    plt.ylabel("Number of Trips")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

def plot_regression(X, y, y_pred):
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, alpha=0.5, label='Actual')
    plt.plot(sorted(X), sorted(y_pred), color='red', label='Regression Line')
    plt.title("Question c: Regression Model")
    plt.xlabel("Trips 1-25 Miles")
    plt.ylabel("Population Not Staying at Home")
    plt.legend()
    plt.tight_layout()

def plot_distance_bands(df_distance):
    cols = [
        'Number of Trips 1-3', 'Number of Trips 3-5',
        'Number of Trips 5-10', 'Number of Trips 10-25',
        'Number of Trips 25-50', 'Number of Trips 50-100',
        'Number of Trips 100-250', 'Number of Trips 250-500',
        'Number of Trips >=500'
    ]
    avg = df_distance[cols].mean()
    plt.figure(figsize=(12, 6))
    plt.bar(range(len(avg)), avg.values, color='steelblue')
    plt.xticks(range(len(avg)), [c.replace('Number of Trips ', '') for c in cols], rotation=45)
    plt.title("Question d: Average Travellers by Distance Band")
    plt.xlabel("Distance Band")
    plt.ylabel("Average Number of Trips")
    plt.tight_layout()