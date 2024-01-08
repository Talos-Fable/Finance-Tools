from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

import time

PATH = "C:\chromedriver.exe"


# driver = webdriver.Chrome(PATH)
# driver.get('https://www.careers.fiserv.com/search-jobs')
# print(driver.title)


# time.sleep(2)
# element = driver.find_element("xpath", '//*[@id="system-ialert-button"]')
# element.click()

# element = driver.find_element("xpath", '//*[@id="search-results-list"]/ul/li[1]/a')
# #element = driver.find_element("link text", "Incident Manager")
# element.click()




#############Text input#################

driver = webdriver.Chrome(PATH)
driver.get('https://fiserv.wd5.myworkdayjobs.com/en-US/EXT/login/ok')

time.sleep(10)

input_email = driver.find_element("xpath", '//*[@id="input-4"]')
input_email.clear() #clears field

input_email.send_keys("jahsiahsanders14@yahoo.com")



input_pwd = driver.find_element("xpath", '//*[@id="input-5"]')
input_pwd.clear() #clears field
input_pwd.send_keys("Nightwolf14*")


submit_button = driver.find_element("xpath", '//*[@id="wd-Authentication-NO_METADATA_ID-uid6"]/div/div[1]/div/form/div[3]/div/div/div/div/div')
submit_button.click()
time.sleep(4)


search_for_jobs = driver.find_element("xpath", '//*[@id="root"]/div/div/div[1]/div/header/div[2]/div[3]/div/nav/button[1]')
search_for_jobs.click()
time.sleep(4)


search_bar = driver.find_element("xpath", '/html/body/div/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div/input')
search_bar.click()
time.sleep(5)
search_bar.send_keys("Georgia")
time.sleep(3)

search_icon = driver.find_element("xpath", '/html/body/div/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/button')
time.sleep(3)
search_icon.click()


driver.get('https://fiserv.wd5.myworkdayjobs.com/en-US/EXT/job/Alpharetta-Georgia/Technical-Project-Manager_R-10303162?q=Georgia')
time.sleep(2)


apply = driver.find_element("xpath", '//*[@id="mainContent"]/div/div/div[1]/div[1]/div/div/div/div/div/a')
apply.click()


lastapp = driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[6]/div/div/a')
lastapp.click()
time.sleep(5)



# select_element = driver.find_element("xpath", '//*[@id="input-1"]')
# select_element.click()
# time.sleep(2)

select_drop = driver.find_element("id", 'input-1')
select_drop.click()

# select by visible text
select_drop.select_by_visible_text('CareerBuilder')


while(True):
     pass