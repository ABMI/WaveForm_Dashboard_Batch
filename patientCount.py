import pymssql
from collections import defaultdict


def getPatientCount(cur):
    data = defaultdict(int)

    cur.execute(
        """
        select count(distinct patient_id) From [IPEAK].[dbo].[local_report]
        """)
    count = cur.fetchall()


    data['total'] = count[0][0]

    return data


if __name__ == '__main__':
    with pymssql.connect(host='10.5.99.80',
                         user='labuser', password='foqdbwj202012#$') as conn:
        with conn.cursor() as cur:
            print(getPatientCount(cur))
