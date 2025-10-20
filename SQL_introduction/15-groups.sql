-- group records with the same scores
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;