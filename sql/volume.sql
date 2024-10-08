WITH eth_prices_ AS (
    SELECT 
        TO_DATE(snapped_at) as date, 
        price as eth_price
    FROM eth_prices
), btc_prices_ AS (
    SELECT 
        TO_DATE(snapped_at) as date, 
        price as btc_price
    FROM Btc_prices
), combined_prices as (
SELECT
    COALESCE(b.date, e.date) as date, 
    e.eth_price,
    b.btc_price
FROM btc_prices_ b
LEFT JOIN eth_prices_ e
    ON b.date = e.date
), daily_amt_eth AS (
    SELECT 
        TO_DATE(date) AS date, 
        sum(value/1E18) AS amt 
    FROM df_eth_trans
    GROUP BY date
), daily_amt_btc AS (
    SELECT 
        TO_DATE(date) AS date, 
        sum(input_value) AS amt 
    FROM df_btc_trans
    GROUP BY date
), A as (
    select 
        YEAR(coalesce(a.date, b.date)) AS year,
        SUM(a.amt * b.eth_price) as volume
    from daily_amt_eth a
    JOIN eth_prices_ b
        ON a.date = b.date
    GROUP BY year
    ORDER BY year
), B as (
        select 
        YEAR(coalesce(a.date, b.date)) AS year,
        SUM(a.amt * b.btc_price) as volume
    from daily_amt_btc a
    JOIN btc_prices_ b
        ON a.date = b.date
    GROUP BY year
    ORDER BY year
)
SELECT
    b.year,
    a.volume as eth_vol_usd,
    b.volume as btc_vol_usd
FROM A a
FULL OUTER JOIN B b
    ON a.year = b.year
ORDER BY year