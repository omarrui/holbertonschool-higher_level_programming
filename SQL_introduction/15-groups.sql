-- group records with the same scores
SELECT score, COUNT(*) as number from second_table GROUP BY score ORDER BY number DESC;