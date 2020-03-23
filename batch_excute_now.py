import json
import time

import os
import requests

import collection

# url = "http://52.78.14.28:3000/saveStatistic"
url = "http://localhost:3000/saveStatistic"
data = collection.get_data()

with open(os.path.join('D:\\Project\\pathology\\KTY\\json\\', 'dashboard_' + time.strftime(
        "%Y%m%d_%H%M%S")) + '.json', 'w') as f:
    json.dump(data, f)

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(time.strftime("%Y/%m/%d, %H:%M:%S"), r.status_code, r.reason)

exit(0)
