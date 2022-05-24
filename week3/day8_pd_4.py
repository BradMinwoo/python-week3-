import pandas as pd
import requests
import json
from pandas import json_normalize
import pandas
#pip install xlsxwriter
url="http://api.upbit.com/v1/market/all"
resp=requests.get(url)
text = resp.text
json_data=json.loads(text)
print(json_data)
#pandas excel 생성
df = json_normalize(json_data)
write = pd.ExcelFile('altCoin.xlsx', engine='xlsxwriter')
df.to_excel(write, sheet_name='Sheet1')
write.close()