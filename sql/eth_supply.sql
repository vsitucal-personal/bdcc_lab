SELECT date, (
  CASE
    -- Initial reward phase (5 ETH per block)
    WHEN number < 4370000 THEN 5 * number
    -- Byzantium phase (3 ETH per block)
    WHEN number < 7280000 THEN (4370000 - 1) * 5 + 3 * (number - 4370000)
    -- Constantinople phase (2 ETH per block)
    WHEN number < 15537393 THEN (4370000 - 1) * 5 + 3 * (7280000 - 4370000) + 2 * (number - 7280000)
    -- After The Merge (Proof of Stake, block reward becomes 0)
    ELSE (4370000 - 1) * 5 + 3 * (7280000 - 4370000) + 2 * (15537393 - 7280000)
  END
) + 72000000 AS max_supply
FROM (
  SELECT 
    TO_DATE(date) AS date,
    MAX(number) AS number
  FROM df_eth_blocks
  GROUP BY date
) AS yearly_blocks
ORDER BY date