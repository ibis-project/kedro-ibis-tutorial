ATTACH 'dbname=postgres user=postgres' AS postgres_db (TYPE POSTGRES);
INSERT INTO postgres_db.flights FROM flights;
INSERT INTO postgres_db.weather FROM weather;
