import subprocess
subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

import pandas as pd
import numpy as np
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import re
from pandas import Series, DataFrame
import os
from typing import List
from copy import deepcopy


""" Question 7"""
# Load station data and name columns
station_data: DataFrame = pd.read_csv("../station_data.csv", header=None)
station_data.columns = [
    "Station_ID",
    "Station_name",
    "Latitude",
    "Longitude",
    "Number_of_docks",
    "City",
    "Installation",
]

# Load trip data and name columns
trip_data: DataFrame = pd.read_csv("../trip_data.csv", header=None)
trip_data.columns = [
    "Trip_id",
    "Trip_duration",
    "Start_date",
    "Start_station_name",
    "Start_station_id",
    "End_date",
    "End_station_name",
    "End_station_id",
    "Bike_id",
    "Customer_type",
    "Zip_code",
]

# convert date columns to datetime
date_cols: pd.Index = trip_data.filter(like="date").columns
trip_data[date_cols] = trip_data[date_cols].apply(pd.to_datetime)


""" Question 8"""
# Filter out trips that are less than 60 seconds and are within the same station
within_sixsec: Series = (trip_data.End_date - trip_data.Start_date).dt.seconds <= 60
same_station: Series = trip_data.Start_station_id == trip_data.End_station_id
cond: Series = within_sixsec & same_station
# Write solution to question 8 to slution_eight.csv file
trip_data.loc[~cond].to_csv("solution_eight.csv", index=False, mode="w")


""" Question 9"""
# Create a copy of the dataframes
trip_nine: DataFrame = deepcopy(trip_data)
station_nine: DataFrame = deepcopy(station_data[["City", "Station_ID"]])

# Join the dataframes to lookup the city of the start and end stations
data_nine: DataFrame = pd.merge(
    trip_nine,
    station_nine,
    left_on="Start_station_id",
    right_on="Station_ID",
    how="inner",
).rename(columns={"City": "Start_city"})

data_nine = data_nine.merge(
    station_nine, left_on="End_station_id", right_on="Station_ID", how="inner"
).rename(columns={"City": "End_city"})

# Create a new column to indicate if the trip is intercity
data_nine["is_intercity"] = np.where(
    data_nine["Start_city"] == data_nine["End_city"], 0, 1
)
# Write solution to question 9 to solution_nine.csv file
data_nine.to_csv("solution_nine.csv", index=False, mode="w")


""" Question 10"""
# Filter out intercity trips
data_ten: DataFrame = data_nine.query("is_intercity==0")
cities = (
    station_data.groupby("City")["Station_ID"]
    .count()
    .to_frame("number_of_stations")
    .reset_index()
)

data: DataFrame = (
    data_ten.groupby("Start_city")
    .agg({"Trip_id": "count", "Trip_duration": ["mean", "sum"]})
    .reset_index()
)

data.columns = [
    cols[0] if (cols[1] == "") else cols[0] + "_" + cols[1] for cols in data.columns
]

data = data.rename(
    columns={
        "Trip_id_count": "Number_of_intra_trips",
        "Trip_duration_mean": "Avg_intra_trips",
        "Trip_duration_sum": "Total_intra_hours",
        "Start_city": "City",
    }
).assign(Total_intra_hours=lambda x: x["Total_intra_hours"] / 3600)
data = data.merge(cities, on="City", how="inner")
data.to_csv("solution_ten.csv", index=False, mode="w")

""" Question 11"""

# Plot a graph of number of trips per month broken down by customer type.
fig, axs = plt.subplots(figsize=(10, 5))
plt.xticks(rotation=90)
plot_data = (
    trip_data.groupby([trip_data.Start_date.dt.month, "Customer_type"])
    .agg({"Trip_id": "count"})
    .reset_index()
    .rename(columns={"Trip_id": "Number_of_trips"})
)

diag = sns.barplot(
    x="Start_date", y="Number_of_trips", hue="Customer_type", data=plot_data
)
plt.title("Number of trips per month broken down by customer type")
plt.xlabel("Month")
plt.ylabel("Number of trips")
plt.tight_layout()
# save plot to solution_eleven.jpg
plt.savefig("solution_eleven.jpg")


""" Question 12"""
is_week: Series = trip_data.Start_date.dt.weekday.isin([5, 6])
trip_data["is_weekday"] = np.where(is_week, "Weekend", "Weekday")
weekday_plot = (
    trip_data.groupby(["is_weekday", "Customer_type"])["Trip_duration"]
    .mean()
    .reset_index()
    .rename(columns={"Trip_duration": "Avg_trip_duration"})
)
weekday_plot.head()

# Plot a graph of average trip duration per month broken down by customer type.
fig, axs = plt.subplots(figsize=(10, 5))
sns.barplot(
    x="is_weekday", y="Avg_trip_duration", hue="Customer_type", data=weekday_plot
)
plt.title("Average trip duration per month broken down by customer type")
plt.xlabel("Month")
plt.ylabel("Average trip duration")
plt.tight_layout()
# save plot to solution_twelve.jpg
plt.savefig("solution_twelve.jpg")
