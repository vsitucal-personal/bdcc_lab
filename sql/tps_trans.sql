WITH eth_daily_txn AS (
    SELECT 
        date, 
        CAST(count(*) AS double) / (24 * 60 * 60) AS eth_transactions_per_sec
    FROM df_eth_trans
    GROUP BY date
), btc_daily_txn AS (
    SELECT 
        date, 
        CAST(count(*) AS double) / (24 * 60 * 60) AS btc_transactions_per_sec
    FROM df_btc_trans
    GROUP BY date
)
SELECT 
    YEAR(coalesce(eth.date, btc.date)) AS year,
    AVG(eth.eth_transactions_per_sec) AS eth_transactions_per_sec,
    AVG(btc.btc_transactions_per_sec) AS btc_transactions_per_sec
FROM eth_daily_txn eth
FULL OUTER JOIN btc_daily_txn btc ON eth.date = btc.date
GROUP BY year
ORDER BY year