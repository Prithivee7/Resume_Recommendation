from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os
import codecs
import pdfkit
from selenium.webdriver.support.ui import Select

# path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
driver = webdriver.Chrome()
url = 'https://freesearch.naukri.com/search'
driver.get(url)
time.sleep(5)

#Role Search
xpath_search = '/html/body/div[5]/div[2]/a[4]/span'
driver.find_element_by_xpath(xpath_search).click()

#Software developer

xpath_search = '//*[@id="role24.02"]'
driver.find_element_by_xpath(xpath_search).click()

xpath_search = '//*[@id="role24.03"]'
driver.find_element_by_xpath(xpath_search).click()

xpath_search = '//*[@id="role24.04"]'
driver.find_element_by_xpath(xpath_search).click()

xpath_search = '//*[@id="role24.05"]'
driver.find_element_by_xpath(xpath_search).click()

xpath_search = '//*[@id="role24.06"]'
driver.find_element_by_xpath(xpath_search).click()

xpath_search = '//*[@id="role24.07"]'
driver.find_element_by_xpath(xpath_search).click()

xpath_search = '//*[@id="role24.08"]'
driver.find_element_by_xpath(xpath_search).click()

resumes_per_page = '/html/body/div[5]/form/div[3]/div[4]/div/div[7]/select'
driver.find_element_by_xpath(resumes_per_page).send_keys(160)


resume_duration = '//*[@id="daysold"]'
select = Select(driver.find_element_by_xpath(resume_duration))
select.select_by_value('3650')
time.sleep(2)

# switch_dept = '//*[@id="farea_id"]'
# driver.find_element_by_xpath(switch_dept).click()

# click_dept = '//*[@id="farea6"]'
# driver.find_element_by_xpath(click_dept).click()

# un_click_dept = '//*[@id="farea24"]'
# driver.find_element_by_xpath(un_click_dept).click()
# Find Resumes
find_resumes_xpath = '/html/body/div[5]/form/div[3]/div[6]/span/input'
driver.find_element_by_xpath(find_resumes_xpath).click()
time.sleep(2)