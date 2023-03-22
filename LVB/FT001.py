import pandas as pd

df=pd.read_excel('/Users/hoangvuhanh/CodeHanh/LVB/RPT_FT001_DataOnly - 2023-02-16T134627.491.xls')

df1=df[['BRANCH_CODE','NARRATIVE', 'OFS_AMOUNT','MAKER_ID','ROUTE_CODE']]

df1['UPPER NARRATIVE'] = [str(x).upper() for x in df1['NARRATIVE']]
df1['UPPER MAKER_ID'] = [str(x).upper() for x in df1['MAKER_ID']]

df1=df1[['BRANCH_CODE','UPPER NARRATIVE', 'OFS_AMOUNT','UPPER MAKER_ID','ROUTE_CODE']]

filtered_df = df1[df1['UPPER NARRATIVE'].str.contains('GCHU') == False]
filtered_df1 = filtered_df[filtered_df['UPPER MAKER_ID'].str.contains('SYS') == False]
filtered_df1 = filtered_df1.reset_index()
filtered_df1=filtered_df1[['BRANCH_CODE','UPPER NARRATIVE', 'OFS_AMOUNT','UPPER MAKER_ID','ROUTE_CODE']]

arraysCode = filtered_df1['BRANCH_CODE'].values.tolist()

df2=pd.read_excel('/Users/hoangvuhanh/CodeHanh/LVB/Mã CN con.xlsx')
df2.rename(columns = {'MA': 'BRANCH_CODE'}, inplace = True)

list_df2 = df2.values.tolist()

list_result = []

for arrayCode in arraysCode:
    index = 0
    for x_df2 in list_df2:
        if str(arrayCode) == str(x_df2[0]):
            value = x_df2[1]
            index += 1
    if index == 0:
        print('Mã bị thiếu',arrayCode)
        list_result.append('')
    else:
        list_result.append(value)

list_result= pd.DataFrame(list_result)
list_result['Tên chi nhánh'] = list_result[0]
list_result = list_result[['Tên chi nhánh']]

result_df = pd.concat([filtered_df1, list_result], axis=1)

result_df1 = result_df[result_df['ROUTE_CODE'].str.contains('IBPS')==True]
result_df2 = pd.pivot_table(result_df1, values='OFS_AMOUNT', index='Tên chi nhánh', aggfunc=sum)

result_df3=result_df2[result_df2['OFS_AMOUNT'] < 3000000000]

value = result_df3['OFS_AMOUNT'].values.tolist()

FT001=sum(value)
print('Tổng số tiền citad dưới 3 tỷ ngày 01/03 {:,} VND'.format(FT001))