WITH value as (
	SELECT 
        year(date) AS year, 
        SUM(value) AS value,
        SUM(gas) AS gas,
        COUNT(*) as count
	FROM df_eth_trans
	GROUP BY year(date)
	ORDER BY year
)
SELECT
	year,
	value as value_in_wei,
    gas as gas_in_wei,
    count as total_transactions
from value
