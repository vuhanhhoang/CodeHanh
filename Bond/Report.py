import pandas as pd

# gọi bảng deals trong excel
df = pd.read_excel('/Users/hoangvuhanh/CodeHanh/Bond/Deals_END_DAY_Report (9).xlsx', 'Deals')
# print(df['Account No']) 
for i in df['Account No'].head(5):
    
    if len(str(i)) < 10:
        i = '0'*(10 - len(str(i))) + str(i)
        print(i)