select date, (CASE 
  WHEN number<210000 THEN 50*number
  WHEN number<420000 THEN (210000-1)*50+25*(number-210000) 
  WHEN number<630000 THEN (210000-1)*50+25*210000+12.5*(number-420000)
  ELSE (210000-1)*50+25*210000+12.5*210000+6.25*(number-630000) 
  END) as reward
from (
    select 
        TO_DATE(date) as date,
        max(number) as number 
    from df_btc_blocks 
    group by date
) order by date 