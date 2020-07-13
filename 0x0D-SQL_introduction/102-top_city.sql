-- Top temeperatures
-- Show top 3 temperatures of database
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month BETWEEN 8 AND 9 GROUP BY avg_temp ORDER BY avg_temp DESC LIMIT 3;
