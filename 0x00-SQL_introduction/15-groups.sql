-- lists the number of records with the same score from second_table

SELECT score, COUNT(score_ AS number FROM second_table GROUP BY score
ORDER BY score DESC;
