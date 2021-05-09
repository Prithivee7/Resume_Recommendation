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

#select All Resumes
resume_duration = '//*[@id="daysold"]'
select = Select(driver.find_element_by_xpath(resume_duration))
select.select_by_value('3650')

#Find Resumes
find_resumes_xpath = '/html/body/div[5]/form/div[3]/div[6]/span/input'
driver.find_element_by_xpath(find_resumes_xpath).click()
time.sleep(2)


parent_handle = driver.current_window_handle
parent = driver.title
# url_list = []
# count = 11399
count = 13640
save_path = 'V:/Final_Project/DBA/'
for i in range(6):
    for j in range(160):
        # print(driver.find_element_by_id)
        if(driver.find_element_by_id == None):
            break
        driver.find_element_by_id(j).click()
        handles = driver.window_handles
        for handle in handles:
            driver.switch_to.window(handle)
            if(driver.title != parent):
                # url_list.append(driver.current_url)
                
                file_name = 'Resume'+str(count)+'.html'
                complete_name = os.path.join(save_path, file_name)
                file_object = codecs.open(complete_name, "w", "utf-8")
                html = driver.page_source
                file_object.write(html)
                print("Completed "+file_name)

                # f = complete_name[:-5] + '.pdf'
                # print('downloaded '+complete_name)
                # pdfkit.from_file(complete_name, f,configuration=config) 
                driver.close()
        count += 1
        driver.switch_to.window(parent_handle)
    time.sleep(2)
    next_page_click = '/html/body/div[15]/div/div[1]/form/div/a'
    driver.find_element_by_xpath(next_page_click).click()
