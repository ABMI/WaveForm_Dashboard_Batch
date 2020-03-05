import pymssql
from collections import defaultdict


def getTotalRows(cur):
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

    data = defaultdict(int)

    cur.execute(
        """
        SELECT sum(c) AS total_row, ip_address
          FROM (
                SELECT count(id) AS c, ip_address FROM [Biosignal_Repository].[dbo].cached_patient_info GROUP BY ip_address
                 UNION ALL
                SELECT count(id) AS c, ip_address FROM [Biosignal_Repository].[dbo].patient_info GROUP BY ip_address 
                 UNION ALL
                SELECT count(A.patient_id) AS c, B.ip_address
                  FROM [Biosignal_Repository].[dbo].patientid_mapping A INNER JOIN (SELECT patient_id, ip_address
                              	    				      FROM [Biosignal_Repository].[dbo].patient_info
                             						     GROUP BY patient_id, ip_address) B
          			 ON A.patient_id = B.patient_id
        	  	  GROUP BY B.ip_address
                 UNION ALL
                SELECT count(A.id) AS c, B.ip_address
                  FROM [Biosignal_Repository].[dbo].waveform_info A INNER JOIN (SELECT patient_id, ip_address
        										      FROM [Biosignal_Repository].[dbo].patient_info
        											 GROUP BY patient_id, ip_address) B
        			 ON A.patient_id = B.patient_id
        		  GROUP BY B.ip_address
        ) AS b GROUP BY ip_address
        """
    )

    old = cur.fetchall()

    cur.execute(
        """
        SELECT sum(c) AS total_row, ip_address
          FROM (
                SELECT count(id) AS c, ip_address FROM [Biosignal_philips].[dbo].cached_patient_info GROUP BY ip_address
                 UNION ALL
                SELECT count(id) AS c, ip_address FROM [Biosignal_philips].[dbo].patient_info GROUP BY ip_address 
                 UNION ALL
                SELECT count(A.patient_id) AS c, B.ip_address
                  FROM [Biosignal_philips].[dbo].patientid_mapping A INNER JOIN (SELECT patient_id, ip_address
                                                            FROM [Biosignal_philips].[dbo].patient_info
                                                          GROUP BY patient_id, ip_address) B
                       ON A.patient_id = B.patient_id
                    GROUP BY B.ip_address
                 UNION ALL
                SELECT count(A.id) AS c, B.ip_address
                  FROM [Biosignal_philips].[dbo].waveform_info A INNER JOIN (SELECT patient_id, ip_address
                                                      FROM [Biosignal_philips].[dbo].patient_info
                                                     GROUP BY patient_id, ip_address) B
                     ON A.patient_id = B.patient_id
                  GROUP BY B.ip_address
        ) AS b GROUP BY ip_address
        """
    )

    new = cur.fetchall()

    for row in old + new:
        data['total'] += row[0]
        data['summary'] += row[0]
        data[icu[row[1]]] += row[0]

    return data


if __name__ == '__main__':
    with pymssql.connect(host='10.5.99.80',
                         user='labuser', password='foqdbwj202012#$') as conn:
        with conn.cursor() as cur:
            print(getTotalRows(cur))
