/** I PURPOSEFULLY MADE THE SCRIPT IDEMPOTENT TO ENSURE THAT MULTIPLE RUNS ESPECIALLY THE DDLs DO NOT FAIL **/
/** TO MAKE THIS SCRIPT WORK THE TWO DATA SOURCES NEEDS TO BE MOVED TO A DIR CALLED "C:\Temp" on a WINDOWS PC OR
   /tmp DIR ON A MAC OR LINUX. YOU CAN  MIGRATE THE CSV FILES USING `mv station_data.csv trips_data.csv /tmp` **/
USE master;

go

DECLARE @db_name CHAR(100);

SET @db_name='bikeshare';

IF NOT EXISTS (SELECT NAME
               FROM   sys.databases
               WHERE  NAME = @db_name) --CHECKING FOR DATABASE EXISTENCE
  BEGIN
      CREATE DATABASE bikeshare; --CREATE DATABASE IF IT DOESNT EXIST
  END;

go

USE bikeshare;

go

IF Object_id('dbo.stations', 'U') IS NULL
  -- CHECKING IF TABLE EXIST BEFORE CREATION
  BEGIN
      CREATE TABLE dbo.stations
        (
           station_id        INT NOT NULL,
           station_name      VARCHAR(max),
           latitude          FLOAT,
           longitude         FLOAT,
           number_of_docks   INT,
           city              VARCHAR(200),
           installation_date DATE,
           PRIMARY KEY (station_id)
        );

      PRINT 'Done creating table stations';
  END;

IF Object_id('dbo.trips', 'U') IS NULL
  BEGIN
      CREATE TABLE dbo.trips
        (
           trip_id            INT NOT NULL,
           trip_duration      INT,
           [start_date]       DATETIME,
           start_station_name VARCHAR(max),
           start_station_id   INT,
           end_date           DATETIME,
           end_station_name   VARCHAR(max),
           end_station_id     INT,
           bike_id            INT,
           customer_type      VARCHAR(10),
           zip_code           VARCHAR(100),
           PRIMARY KEY (trip_id)
        );

      PRINT 'Done creating table trips';
  END;

go

PRINT 'Loading trip_data into trips table';

/** WRAP TALBE IN A TRY AND CATCH BLOCK TO TRAP ERROS DURING LOADING OF DATA**/
BEGIN try
    BULK INSERT dbo.trips -- LOADING TRIPS DATA INTO THE TABLE
      FROM 'C:\Temp\trip_data.csv'
      WITH
        (
          fieldterminator = ',',
          rowterminator = '\n',
          firstrow= 1
        )
    ;

    PRINT 'Done loading trip_data into trips table';
END try

BEGIN catch
    PRINT 'Error loading trip_data into trips table';
END catch;

PRINT 'Loading station_data into stations table';

BEGIN try
    BULK INSERT dbo.stations --LOADING STATION DATA INTO THE TABLE
      FROM 'C:\Temp\station_data.csv'
      WITH
        (
          fieldterminator = ',',
          rowterminator = '\n',
          firstrow= 1
        )
    ;

    PRINT 'Done loading station_data into stations table';
END try

BEGIN catch
    PRINT 'Error loading station_data into stations table';
END catch;

/** QUERIES **/
/** Solution to question 3**/
WITH popular_bike
     AS (SELECT bike_id,
                Count(trip_id) AS num_trips
         FROM   dbo.trips
         GROUP  BY bike_id)
-- IN MSSQL SERVER THE TOP CLAUSE IS A SIMPLER ALTERNATIVE THAN TO USE ANALYTICAL FUNCTIONS THEN FILTERING THEM FOR THE TOP N REQUIRED
SELECT TOP 10 *
FROM   popular_bike
ORDER  BY num_trips DESC;

/** Solution to question 4 **/
-- JOINING TRIP TABLE TO STATION TO LOOK UP CITY
WITH base_data
     AS (SELECT stations.city,
                trips.trip_id
         FROM   dbo.stations AS stations
                INNER JOIN dbo.trips AS trips
                        ON stations.station_id = trips.start_station_id)
SELECT city,
       Count(trip_id) AS number_of_trips
FROM   base_data
GROUP  BY city
ORDER  BY 2 DESC;

/** Solution to question 5 **/
--PERFORMING LOOKUP IN STATION TABLE FOR THE ORIGIN AND DESTINATIN CITY
WITH cross_cities
     AS (SELECT B.city AS start_city,
                c.city AS end_city,
                A.trip_id
         FROM   dbo.trips AS A
                INNER JOIN dbo.stations AS B
                        ON A.start_station_id = B.station_id
                INNER JOIN dbo.stations AS C
                        ON A.end_station_id = C.station_id
         WHERE  B.city != c.city) -- FILTER OUT INTRA CITY RIDES
/** WAS CONSIDERING SUMING UP THE NUMBER OF TRIPS BETWEEN TWO LOCATIONS
BUT REFRAINED FROM DOING DUE TO THE REQUEST FOR THE START AND END LOCATION **/
SELECT start_city,
       end_city,
       Count(*) AS number_of_trips
FROM   cross_cities
GROUP  BY start_city,
          end_city;

/** Solution to question 6 **/
/** WAS A BIT CONFUSED WITH THE 'BIKE_ID' FOR INDIVIDUAL BIKE **/
/** 
IF THE SOLUTION REQUESTED FOR MOST RECENT DATE AND THE RIDE ID FOR EACH BIKE THE SOLUTION WOULD HAVE BEEN 

with latest_ride as (
select *,row_number() over (partition by bike_id order by end_date desc) as recent_ride
from dbo.trips
)
select bike_id,end_date,recent_ride
from latest_ride
where recent_ride=1 

**/
SELECT bike_id,
       Max(Cast(end_date AS DATE)) AS recent_ride
FROM   dbo.trips
GROUP  BY bike_id; 