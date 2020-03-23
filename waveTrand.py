import pymssql
from collections import defaultdict


def getWaveTrand(cur):
    """
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

    cur.execute(

    )

    old = cur.fetchall()


    data = {
        "EICU": defaultdict(int),
        "MICU": defaultdict(int),
        "TICUA": defaultdict(int),
        "TICUB": defaultdict(int),
        "TICUC": defaultdict(int),
        "TOR": defaultdict(int),
        "3ICUA": defaultdict(int),
        "3ICUB": defaultdict(int),
        "total": defaultdict(int),
        "summary": defaultdict(int)
    }

    for row in old + new:
        data[icu[row[2]]][row[0]] += row[1]
        data['total'][row[0]] += row[1]
        data['summary'][row[0]] += row[1]
    """
    data = {"total":1}
    return data


if __name__ == '__main__':
    with pymssql.connect(host='10.5.99.80',
                         user='labuser', password='foqdbwj202012#$') as conn:
        with conn.cursor() as cur:
            print(getWaveTrand(cur))
