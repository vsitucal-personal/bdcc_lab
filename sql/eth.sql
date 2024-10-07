WITH value AS (
	SELECT 
        year(date) AS year, 
        AVG(value/1E18) AS avg_value,
        AVG(CASE 
                WHEN receipt_status = 1 AND receipt_effective_gas_price > 0 
                THEN receipt_effective_gas_price/1E18 
                ELSE 0 
            END) AS avg_gas,
        COUNT(*) AS count
	FROM df_eth_trans
	GROUP BY year(date)
	ORDER BY year
)
SELECT
	year,
	value AS avg_value_in_eth,
    gas AS avg_gas_in_eth,
    count AS total_transactions
FROM value;
