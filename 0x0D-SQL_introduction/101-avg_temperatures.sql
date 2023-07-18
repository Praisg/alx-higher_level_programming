-- displays the average temperature by city ordered by temperature (descend

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
