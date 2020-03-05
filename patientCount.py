import pymssql
from collections import defaultdict


def getPatientCount(cur):
    ip_ICU_mapping = {
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

    data = defaultdict(int)

    cur.execute(
        """
        SELECT B.ip_address, 
               COUNT (DISTINCT B.patient_id) AS patient_count_all
          FROM [Biosignal_Repository].[dbo].waveform_info A INNER JOIN (SELECT patient_id, ip_address
        	        						  FROM [Biosignal_Repository].[dbo].patient_info
        									 GROUP BY patient_id, ip_address) B
        	 ON A.patient_id = B.patient_id
         GROUP BY B.ip_address
        """)

    old = cur.fetchall()

    cur.execute(
        """
        SELECT B.ip_address, 
               COUNT (DISTINCT B.patient_id) AS patient_count_all
          FROM [Biosignal_philips].[dbo].waveform_info A INNER JOIN (SELECT patient_id, ip_address
                                              FROM [Biosignal_philips].[dbo].patient_info
                                             GROUP BY patient_id, ip_address) B
             ON A.patient_id = B.patient_id
         GROUP BY B.ip_address
        """)

    new = cur.fetchall()

    for row in old + new:
        data['total'] += row[1]
        data['summary'] += row[1]
        data[ip_ICU_mapping[row[0]]] += row[1]

    return data


if __name__ == '__main__':
    with pymssql.connect(host='10.5.99.80',
                         user='labuser', password='foqdbwj202012#$') as conn:
        with conn.cursor() as cur:
            print(getPatientCount(cur))
