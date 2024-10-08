SELECT
    a.date,
    d.reward/a.total_value as btc_nvt,
    c.max_supply/b.total_value as eth_nvt
FROM daily_btc_amt a
FULL OUTER JOIN daily_eth_amt b
    ON a.date = b.date
FULL OUTER JOIN eth_supply c
    ON a.date = c.date
FULL OUTER JOIN btc_supply d
    ON a.date = d.date