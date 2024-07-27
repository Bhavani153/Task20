import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

driver_path = r"E:\Automation testing\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)
driver.get("https://www.cowin.gov.in/")
driver.maximize_window()
time.sleep(2)
firstwindow = driver.window_handles[0]
time.sleep(2)

driver.execute_script("window.open('https://www.cowin.gov.in/faq','new window')")
secoundwindow=driver.window_handles[1]
driver.switch_to.window(secoundwindow)
secoundwindow=driver.title
print(secoundwindow)
time.sleep(2)

search = driver.find_element(By.XPATH,'//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a')
time.sleep(2)
search.click()
time.sleep(3)

thirdright=driver.window_handles[-1]
driver.switch_to.window(thirdright)
time.sleep(3)
driver.close()

secoundright=driver.window_handles[-2]
driver.switch_to.window(secoundright)
time.sleep(3)
driver.close()

# **********

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

driver_path = r"E:\Automation testing\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)
driver.get("https://labour.gov.in/")
driver.maximize_window()
search = driver.find_element(By.LINK_TEXT,"Documents")
time.sleep(2)
search.click()
time.sleep(2)

search = driver.find_element(By.XPATH,'//*[@id="nav"]/li[7]/a')
time.sleep(2)
search.click()
time.sleep(2)
x=driver.find_element(By.XPATH,'//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/a')
x.click()
j=driver.switch_to.alert
j.accept()
time.sleep(2)
driver.close()
a=driver.find_element(By.XPATH,'//*[@id="nav"]/li[10]/a')
a.click()





