import pymssql


def getStartDay(cur):
    cur.execute(
        """
        SELECT TOP 1 DATEDIFF(day, CONVERT(VARCHAR, SUBSTRING(starttime, 0, 9), 120), GETDATE()) AS diff_date
          FROM [Biosignal_Repository].[dbo].[waveform_info]
         ORDER BY starttime
        """
        )
    nion_row = cur.fetchone()

    cur.execute(
        """
        SELECT TOP 1 DATEDIFF(day, CONVERT(VARCHAR, SUBSTRING(starttime, 0, 9), 120), GETDATE()) AS diff_date
          FROM [Biosignal_philips].[dbo].[waveform_info]
         ORDER BY starttime
        """)

    philips_row = cur.fetchone()

    return {
        "EICU": philips_row[0],
        "MICU": philips_row[0],
        "TICUA": philips_row[0],
        "TICUB": nion_row[0],
        "TICUC": nion_row[0],
        "TOR": philips_row[0],
        "3ICUA": philips_row[0],
        "3ICUB": philips_row[0],
        "total": nion_row[0] if nion_row[0] > philips_row[0] else philips_row[0],
        "summary": nion_row[0] if nion_row[0] > philips_row[0] else philips_row[0]
    }


if __name__ == '__main__':
    with pymssql.connect(host='10.5.99.80',
                         user='labuser', password='foqdbwj202012#$') as conn:
        with conn.cursor() as cur:
            print(getStartDay(cur))
