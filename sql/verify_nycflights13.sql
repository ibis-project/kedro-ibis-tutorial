SELECT 'flights' table_name, COUNT(*) FROM flights UNION
SELECT 'weather' table_name, COUNT(*) FROM weather
ORDER BY table_name;
