import pandas as pd
url = 'https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/tas/1901-2016/53.544388$cckp$-113.490929/53.544388$cckp$-113.490929'
weather = pd.read_csv(url)
print(weather)