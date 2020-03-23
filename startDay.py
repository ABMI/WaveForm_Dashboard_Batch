import pymssql


def getStartDay(cur):
    cur.execute(
        """
        DECLARE @Var2 VARCHAR(20);
        SET @VAR2 = (SELECT TOP 1 ISNULL(receiption_date, GETDATE()) AS receiption_date FROM IPEAK.dbo.local_report order by receiption_date);
        SELECT DATEDIFF(day, CONVERT(VARCHAR, SUBSTRING(@Var2, 0, 20), 120), GETDATE()) AS diff_date
        """
        )
    row = cur.fetchone()
    return {
        "total": row[0]
    }


if __name__ == '__main__':
    with pymssql.connect(host='10.5.99.80',
                         user='labuser', password='foqdbwj202012#$') as conn:
        with conn.cursor() as cur:
            print(getStartDay(cur))
