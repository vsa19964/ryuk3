from selenium import webdriver
import pandas as pd

driver =driver = webdriver.Chrome("C:\\Users\\vsa19\\Documents\\PYTHON\\Automation\\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.worldometers.info/world-population/population-by-country/')
# driver.implicitly_wait(8)
# e1 = driver.find_element_by_xpath('//*[@id="nav-yesterday-tab"]/a').click()

countries = driver.find_elements_by_xpath('//tbody/tr/td[2]/a')
population = driver.find_elements_by_xpath(' //tbody/tr/td[3]')
yearly_change = driver.find_elements_by_xpath('//tbody/tr/td[4]')
world_change = driver.find_elements_by_xpath('//tbody/tr/td[12]')

population_result = []
for i in range(len(countries)):
    temp_data = {'Country': countries[i].text, 'Population': population[i].text, 'Annual change': yearly_change[i].text,
    'World_share': world_change[i].text}
    population_result.append(temp_data)

df_data = pd.DataFrame(population_result)
df_data.to_excel('Population_World_result.xlsx', index=False)

driver.close()
