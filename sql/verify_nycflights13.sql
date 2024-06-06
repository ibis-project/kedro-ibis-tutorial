SELECT 'flights' table, COUNT(*) n FROM flights UNION
SELECT 'weather' table, COUNT(*) n FROM weather
ORDER BY "table";
