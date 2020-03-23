import pymssql
from collections import defaultdict


def getWaveType(cur):
    cur.execute(
        """
        SELECT LEFT(pathology_id,1) as issue_type, count(*) as cnt From [IPEAK].[dbo].[local_report]
        GROUP BY LEFT(pathology_id,1)
        having count(*) > 50
        order by issue_type
        """
    )

    old = cur.fetchall()


    data = {
        'total': defaultdict(int)
    }

    for row in old:
        data['total'][row[0]] += row[1]

    return data


if __name__ == '__main__':
    with pymssql.connect(host='10.5.99.80',
                         user='labuser', password='foqdbwj202012#$') as conn:
        with conn.cursor() as cur:
            print(getWaveType(cur))
