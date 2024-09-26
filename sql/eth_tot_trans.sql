SELECT year(date) AS year, COUNT(*) AS total_transactions
FROM df_eth_trans
GROUP BY year(date)
ORDER BY year
