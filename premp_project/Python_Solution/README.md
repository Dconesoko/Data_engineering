# Data Analysis with Python

This script is a Python program that performs various data analysis tasks using the pandas and numpy libraries. It reads in data from two CSV files: `station_data.csv` and `trip_data.csv`.

# install dependencies
Use `pip install -r requirements.txt` to download neccessary packages

## Libraries Used
- pandas
- numpy
- datetime
- seaborn
- matplotlib
- re
- copy

## Tasks Performed
The script performs the following tasks:

### Question 7
- Loads `station_data` and `trip_data` CSV files into Pandas DataFrames.
- Names the columns of the `station_data` and `trip_data` DataFrames.
- Converts the date columns of the `trip_data` DataFrame into datetime objects.
- Saves the result to a csv file named "solution_eight.csv"

### Question 8
- Filters out trips that are less than 60 seconds and are within the same station.
- Saves the result to a CSV file named "solution_eight.csv".

### Question 9
- Creates a copy of the `trip_data` and `station_data` DataFrames.
- Joins the DataFrames to lookup the city of the start and end stations.
- Creates a new column to indicate if the trip is intercity.
- Saves the result to a CSV file named "solution_nine.csv".

### Question 10
- Filters out intercity trips.
- Aggregates the data to compute the number of intra-city trips, average trip duration, and total intra-city hours per city.
- Saves the result to a CSV file named "solution_ten.csv".

### Question 11
- Plots a bar graph of the number of trips per month broken down by customer type.
- Saves the plot to a file named "solution_eleven.jpg".

### Question 12
- Aggregates the data to compute the average trip duration per customer type on weekdays and weekends.
- Plots a bar graph of the average trip duration per month broken down by customer type.
- Saves the plot to a file name "solution_twelve.jpg".

## How to Run the Script
1. Clone or download the repository to your local machine.
2. Open a terminal window and navigate to the directory containing the script.
3. Run the script using the command `python nana_donkor.py`.
