SELECT 
    TO_DATE(date) AS date, 
    SUM(value/1E18) AS total_value
FROM df_eth_trans
GROUP BY date
ORDER BY date