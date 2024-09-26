WITH value as (
	SELECT year(date) AS year, SUM(value) AS value
	FROM df_eth_trans
	GROUP BY year(date)
	ORDER BY year
)
SELECT
	year,
	value as value_in_wei
from value
