SELECT 
    TO_DATE(date) AS date, 
    SUM(input_value) AS total_value
FROM df_btc_trans
GROUP BY date
ORDER BY date