import pandas as pd
#데이터프레트레임을 기보능로 (Sql 테이블, r의 데이터 프로엠과 유사함)
#행과 열로 이루저니 표 형태
#group by, join, 함수지원
df = pd.DataFrame({"name":['Bob','Alex','Janice']
                   ,"age":[60, 25, 33]})
print(df.head())
df['age_plus_one'] = df['age'] +1
df['age_squared']=df['age']*df['age']
print(df)
total_age=df['age'].sum()
print('sum:', total_age)
df_below50=df[df['age']<50]
print(df_below50)