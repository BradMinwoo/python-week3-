import pandas as pd
#데이터프레임의 1열은 시리즈구조

#1열은 시리즈 구조
s = pd.Series([1, 2, 3]) #칼럼으로 데이러틑 나타냄
print(s)
print(s+1)
print(s+pd.Series([2,4,6]))#길이가 같은 시리즈를 더하면 성분별 덧셈
df_w_age = pd.DataFrame({"name":['Tom','Tyrell','Claire']
                         ,"age": [60, 25, 33]})
df_w_height = pd.DataFrame({"name":['Tom','Tyrell','Claire']
                         ,"heiht": [6.2, 4.0, 5.5]})
joined = df_w_age.set_index("name").join(df_w_height.set_index('name')) # index set 는 앞에 숫자값을 표현해줌 ㅋ
print(joined)
print(joined.reset_index())
df = joined.reset_index()
#함수지원
# def agg(p_df):
#     return pd.Series({"name":max(p_df['name'])
#                       ,"oldest":max(p_df['age'])
#                       ,"mean_height":p_df['height'].mean()})
# print(df.apply(agg))

#lambda 지원함
#익명으로 쓰는 함수, 휘발성으로 사용  like 자바스크립트

re = (lambda x : x+1)(3)
print('정의와 동시에 사용 ', re)
print((lambda x, y : x+y)(10,20))
#객체에 담아 사용
func = lambda x, y  : x *y +1
print(func(4,2))

#pandas 람다지원
df['age_squar'] = df['age'].apply(lambda x:x*x)  # 'age'값을 가져와서 (apply) 함수를 적용한다.
print(df)
func1 = lambda x:x*x
df['age_aquar2'] = df['age'].apply(func1)
print(df)