import pandas as pd
import cx_Oracle
conn = cx_Oracle.connect('java','oracle','127.0.0.1:1521/XE')
# df = pd.read_sql('select * from employees',conn)
# print(df)
# df_2000 = df[df['SALARY']>15000]
# print(df_2000)
df = pd.read_sql("""select *
                    from employees
                    where emp_name like '%'||:nm||'%'
                    """, con= conn, params={"nm":"Steven"})
print(df)
