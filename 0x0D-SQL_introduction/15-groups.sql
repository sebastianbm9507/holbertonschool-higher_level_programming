-- Display result group by
-- Lists the number of records with the same score in the table second_table
SELECT score , COUNT(roowww) AS number from second_table GROUP BY score ORDER BY score DESC;
