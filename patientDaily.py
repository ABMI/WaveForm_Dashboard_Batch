import pymssql
from collections import defaultdict


def getPatientDaily(cur):
    cur.execute(
        'SELECT LEFT(timestamp, 8) AS day, ' +
        ' COUNT (DISTINCT patient_id) AS patient_count_day, ' +
        '       ip_address ' +
        '  FROM [Biosignal_Repository].[dbo].patient_info ' +
        ' WHERE CONVERT(VARCHAR, LEFT(timestamp, 8), 120) >= DATEADD(dd, DATEDIFF(day,0, getdate()) - 30, 0) ' +
        ' GROUP BY LEFT(timestamp, 8), ip_address ' +
        ' ORDER BY LEFT(timestamp, 8) ')
    old = cur.fetchall()

    cur.execute(
        'SELECT LEFT(timestamp, 8) AS day, ' +
        ' COUNT (DISTINCT patient_id) AS patient_count_day, ' +
        '       ip_address ' +
        '  FROM [Biosignal_philips].[dbo].patient_info ' +
        ' WHERE CONVERT(VARCHAR, LEFT(timestamp, 8), 120) >= DATEADD(dd, DATEDIFF(day,0, getdate()) - 30, 0) ' +
        ' GROUP BY LEFT(timestamp, 8), ip_address ' +
        ' ORDER BY LEFT(timestamp, 8) ')
    new = cur.fetchall()

    data = {
        "EICU": defaultdict(int),
        "MICU": defaultdict(int),
        "TICUA": defaultdict(int),
        "TICUB": defaultdict(int),
        "TOR": defaultdict(int),
        "TICUC": defaultdict(int),
        "3ICUA": defaultdict(int),
        "3ICUB": defaultdict(int),
        "total": defaultdict(int),
        'summary': defaultdict(int)

    }

    icu = {
        "192.168.62.25": "EICU",
        "192.168.62.27": "EICU",
        "192.168.62.50": "MICU",
        "192.168.62.52": "MICU",
        "192.168.62.10": "TICUA",
        "192.168.62.21": "TICUB",
        "192.168.62.22": "TICUC",
        '192.168.62.31': 'TOR',
        '192.168.62.32': 'TOR',
        '192.168.62.33': 'TOR',
        '192.168.62.71': '3ICUA',
        '192.168.62.70': '3ICUA',
        '192.168.62.80': '3ICUB'
    }

    for row in old + new:
        """
        row[0] : date
        row[1] : close
        row[2] : icu
        """
        data[icu[row[2]]][row[0]] += row[1]
        data['total'][row[0]] += row[1]
        data['summary'][row[0]] += row[1]

    return data


if __name__ == '__main__':
    with pymssql.connect(host='10.5.99.80',
                         user='labuser', password='foqdbwj202012#$') as conn:
        with conn.cursor() as cur:
            print(getPatientDaily(cur))
