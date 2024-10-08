WITH value AS (
	SELECT 
        year(date) AS year, 
        AVG(input_value) AS avg_value,
        AVG(fee) AS avg_fee,
        SUM(input_value) AS total_value,
        SUM(fee) AS total_fee,
        COUNT(*) AS count
	FROM df_btc_trans
	GROUP BY year(date)
	ORDER BY year
)
SELECT
	year,
	avg_value,
    avg_fee,
    total_value,
    total_fee,
    count AS total_transactions
FROM value