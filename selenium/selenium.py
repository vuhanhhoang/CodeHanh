from selenium import webdriver

# Gọi ra công cụ tìm kiếm
from selenium.webdriver.common.by import By

# Set up thuộc tính của webdriver 
from selenium.webdriver.chrome.options import Options

# Dừng lại sau thao tác này bn lâu
from time import sleep

import pandas as pd

chrome_options = Options()
brower=webdriver.Chrome(executable_path='chromedriver', options=chrome_options)

brower.get("https://vn.investing.com/economic-calendar/cpi-67")

sleep(5)

while True:
    try:
        brower.find_element(By.XPATH,'/html/body/div[5]/section/div[12]/div[1]/a').click()
    except:
        break

table = []
i = 1
while True:
    try:
        array = []
        for j in range(5):
            dt = brower.find_element(By.XPATH, f'/html/body/div[5]/section/div[12]/table/tbody/tr[{i}]/td[{j+1}]').text
            array.append(dt)
        table.append(array)
        i += 1
    except:
        break 
table = pd.DataFrame(table)
table['Ngày phát hành'] = [x[0:10] for x in table[0]]
table['Dự báo'] = [x[:-1] for x in table[3]]
table['Thực tế'] = [x[:-1] for x in table[2]]
table['Trước đó'] = [x[:-1] for x in table[4]]
table = table[['Ngày phát hành','Dự báo', 'Thực tế', 'Trước đó']]
table = table.set_index('Ngày phát hành')
print(table)

table.to_csv('CPI Anh Quốc.csv')

import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('CPI Anh Quốc.csv')
sns.lineplot(data=data.drop(['Ngày phát hành'], axis=1))
plt.show()