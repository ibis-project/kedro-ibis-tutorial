ATTACH 'dbname=postgres user=postgres' AS pydata_london2024 (TYPE POSTGRES);

INSERT INTO pydata_london2024.flights
  FROM 'data/nycflights13_flights.parquet';
INSERT INTO pydata_london2024.weather
  FROM 'data/nycflights13_weather.parquet';
