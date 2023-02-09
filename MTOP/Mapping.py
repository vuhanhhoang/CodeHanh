import pandas as pd

#gọi Sheet3 trong file excel
df3=pd.read_excel('/Users/hoangvuhanh/CodeHanh/MTOP/MTOP.xlsx','Sheet3')
# print(df3)
# df3=df3.groupby('Mã Deal')

df4=pd.read_excel('/Users/hoangvuhanh/CodeHanh/MTOP/MTOP.xlsx','Sheet4')
# print(df4)

for i in df3['Mã Deal']:
    print(i)

