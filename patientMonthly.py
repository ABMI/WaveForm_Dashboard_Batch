import pymssql
from collections import defaultdict

## 수정 됨
import pymssql
from collections import defaultdict

def getPatientMonthly(cur):
    data = defaultdict(int)

    cur.execute(
        """
        SELECT TOP 14 LEFT(issue_date,7) as issue_date, count(*) as cnt From [IPEAK].[dbo].[local_report]
        GROUP BY LEFT(issue_date,7)
        order by issue_date desc
        """)

    rows = cur.fetchall()
    total = {}
    for row, val in rows:
        row = row.replace("-", "")
        if int(row[:4]) < 2200:
            total[row]= val
    data['total'] = total
    return data

if __name__ == '__main__':
    with pymssql.connect(host='10.5.99.80',
                         user='labuser', password='foqdbwj202012#$') as conn:
        with conn.cursor() as cur:
            print(getPatientMonthly(cur))
