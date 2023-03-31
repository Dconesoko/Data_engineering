# Bikeshare SQL Script

This is an SQL script for creating a bikeshare database and tables, and loading it with data. It also contains SQL queries for answering questions 3 to 6f.

## Prerequisites
- SQL Server Management Studio (SSMS)
- Two CSV files named "station_data.csv" and "trip_data.csv" in a directory named "Temp" on your Windows PC (or in the /tmp directory on a Mac or Linux machine).

## Getting Started
1. Open SQL Server Management Studio (SSMS).
2. Copy and paste the code from the script into a new query window.
3. Save the script as a .sql file.
4. Run the script.

## How It Works
The script checks if the bikeshare database exists, and creates it if it doesn't. It then checks if the "stations" and "trips" tables exist, and creates them if they don't. After creating the tables, the script loads data from the CSV files into the tables using the BULK INSERT command.

The script also contains SQL queries for answering some questions related to the bikeshare data. These include:

- A query that lists the top 10 bikes with the most number of trips.
- A query that lists the number of trips originating from each city.
- A query that lists the number of trips between each pair of cities
- A query that lists the most recent ride date for each bike.

### Notes
- The script uses a mix of ANSI sql and T-sql
- The script is made idempotent to ensure that multiple runs, especially the DDLs, do not fail.
- The script assumes that the CSV files are stored in a directory named "Temp" on your Windows PC (or in the /tmp directory on a Mac or Linux machine). You can migrate the CSV files using `mv station_data.csv trips_data.csv /tmp` on mac and linux.
- The script uses the TOP clause instead of analytical functions to filter the top N results.
- The script includes TRY and CATCH blocks to trap errors during loading of data.
- The script includes comments explaining each section of code.
