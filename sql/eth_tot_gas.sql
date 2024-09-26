WITH gas AS (
    SELECT YEAR(date) AS year, SUM(gas) AS gas
    FROM df_eth_trans
    GROUP BY YEAR(date)
    ORDER BY year
)
SELECT 
    year,
    gas AS gas_in_wei
FROM gas;
