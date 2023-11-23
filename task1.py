# 1st pip install pandas
# 2nd pip install pandas-profiling
import pandas as pd
from pandas_profiling import profilreport

pf=pd.read_csv('machine-readable-business-employment-data-jun-2023-quarter.csv')
print(pf)
# to generate profile report
profile= profilreport(pf)
profile.to_file(output_file="annualreport.html")