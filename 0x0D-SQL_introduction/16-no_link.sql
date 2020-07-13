-- List All records table
--  Script that lists all records of the table second_table of the database hbtn_0c_0
SELECT score, name from second_table where name IS NOT NULL ORDER BY score DESC;
