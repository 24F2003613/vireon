# in collab files, .ipynb ,i have done detailed step by step way

## in feature 1
first it said to arrange acording to devices
i got the count of shed and strs
then ran a loop 
which on having shed 1 - 
checks timestamp within 5(missed)/10 mins(danger) - d["timestamp"].diff().dt.total_seconds() / 60 
if greater 10 mins count to danger and gets added there
we eventually get total reading and completness %
same for other shed - shed 2

## in feature 2
we are given conditions already listed down 
-> voltage_unbalance_pct > 2 , voltage_unbalance_pct > 5
-> pf_avg < 0.9 , pf_avg < 0.85
-> neutral_current_a > 0.1*avg_ph
-> avg_phase is the mean of currents through r b and y
-> fire_risk_level - HIGH/WARNING - flag

i used dataframe.assign operator assigning the req values
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html

took help of this 

and count the respective requiremnts