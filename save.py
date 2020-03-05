import json
import time

import os
import requests

url = "http://128.1.99.43:3000/saveStatistic"

# For local testing
# url = "http://localhost:3000/saveStatistic"

json_dir = 'D:\\Project\\Biosignal\\KTY\\json'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

data = ''

with open(os.path.join(json_dir, os.listdir(json_dir)[-1]), encoding='utf-8') as f:
    data = json.load(f)
# with open('dashboard_20190129_001708.json', encoding='utf-8') as f:
    

r = requests.post(url, data=json.dumps(data), headers=headers)
print(time.strftime("%Y/%m/%d, %H:%M:%S"), r.status_code, r.reason)
    