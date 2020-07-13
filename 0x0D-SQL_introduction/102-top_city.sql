-- Top temeperatures
-- Show top 3 temperatures of database
SELECT city, AVG(temperatures) AS avg_temp FROM temperatures WHERE month BETWEEN 8 and 9 GROUP BY avg_temp ORDER BY avg_temp DESC LIMIT 3;
