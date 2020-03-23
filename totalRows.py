import pymssql
from collections import defaultdict


def getTotalRows(cur):
    data = defaultdict(int)

    cur.execute("SELECT count(*) FROM IPEAK.dbo.local_report")

    total_row = cur.fetchall()
    data['total'] = total_row[0][0]
    return data


if __name__ == '__main__':
    with pymssql.connect(host='10.5.99.80',
                         user='labuser', password='foqdbwj202012#$') as conn:
        with conn.cursor() as cur:
            print(getTotalRows(cur))
