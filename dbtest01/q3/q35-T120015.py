#q35

from MyDatabase import my_open, my_query, my_close
import pandas as pd

dsn = {
    'host': '172.30.0.10',
    'port': '3306',
    'user': 'root',
    'password': '1234',
    'database': 'dbtest01'
}

dbcon, cur = my_open(**dsn)

query = f"""
    select kamokucode, subjectname, sum(atdata) as cnt
    from ga_ka_at
    where gakusekicode = 'H1004'
    group by kamokucode
    ;
"""

my_query(query, cur)
recset = pd.DataFrame(cur.fetchall())
my_close(dbcon, cur)

print(recset)

