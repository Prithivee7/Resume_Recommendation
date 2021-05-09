from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os
import codecs

driver = webdriver.Chrome()
url = 'https://freesearch.naukri.com/search'
driver.get(url)
time.sleep(5)

#Role Search
xpath_search = '/html/body/div[5]/div[2]/a[4]/span'
driver.find_element_by_xpath(xpath_search).click()

#Software developer
xpath_search = '//*[@id="role24.01"]'
driver.find_element_by_xpath(xpath_search).click()
time.sleep(1)
#Find Resumes
find_resumes_xpath = '/html/body/div[5]/form/div[3]/div[6]/span/input'
driver.find_element_by_xpath(find_resumes_xpath).click()
time.sleep(2)
# handle = driver.current_window_handle


resumes_per_page = '//*[@id="resumesPerPage"]'
driver.find_element_by_xpath(resumes_per_page).send_keys(160)

parent_handle = driver.current_window_handle
handle_links = []
resume_links = []
for i in range(2):
    # handle_links.append(driver.current_window_handle)
    for j in range(160):
        resume_links.append(driver.find_element_by_id(j))
    time.sleep(2)
    next_page_click = '/html/body/div[15]/div/div[1]/form/div/a'
    driver.find_element_by_xpath(next_page_click).click()

