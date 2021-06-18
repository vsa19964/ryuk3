from selenium import webdriver
import pandas as pd
driver= webdriver.Chrome("C:\\Users\\vsa19\\Documents\\PYTHON\\Automation\\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/table-search-filter-demo.html')
task = driver.find_elements_by_xpath('//tbody/tr[1]/td[2]')
assignee = driver.find_elements_by_xpath('//tbody/tr[1]/td[3]')
status = driver.find_elements_by_xpath('//tbody/tr/td[4]')
final_table = []
for i in range(len(task)):
    temp_data= {'Task': task[i].text,
    'Assignee': assignee[i].text,
    'Status':status[i].text}
    final_table.append(temp_data)

df_data = pd.DataFrame(final_table)
df_data.to_excel('sample_table_result.xlsx', index=False)


