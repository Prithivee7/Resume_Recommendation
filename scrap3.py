from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os
import codecs
import pdfkit


path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# path_wkhtmltopdf = 'C:/Users/Prithivee Ramalingam/AppData/Roaming/Python/Python37/site-packages/wkhtmltopdf-0.2-py3.7.egg-info'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
driver = webdriver.Chrome()
url = 'https://freesearch.naukri.com/search'
driver.get(url)
time.sleep(5)

#Role Search
xpath_search = '/html/body/div[5]/div[2]/a[4]/span'
driver.find_element_by_xpath(xpath_search).click()

#Software developer
xpath_search = '//*[@id="role24.11"]'
driver.find_element_by_xpath(xpath_search).click()

xpath_search = '//*[@id="role24.12"]'
driver.find_element_by_xpath(xpath_search).click()

xpath_search = '//*[@id="role24.13"]'
driver.find_element_by_xpath(xpath_search).click()

xpath_search = '//*[@id="role24.14"]'
driver.find_element_by_xpath(xpath_search).click()

xpath_search = '//*[@id="role24.15"]'
driver.find_element_by_xpath(xpath_search).click()
time.sleep(1)

#Find Resumes
find_resumes_xpath = '/html/body/div[5]/form/div[3]/div[6]/span/input'
driver.find_element_by_xpath(find_resumes_xpath).click()
time.sleep(2)
# handle = driver.current_window_handle


resumes_per_page = '//*[@id="resumesPerPage"]'
driver.find_element_by_xpath(resumes_per_page).send_keys(160)

resume_links = []
for i in range(160):
    resume_links.append(driver.find_element_by_id(i))

parent_handle = driver.current_window_handle
parent = driver.title
print(parent)
save_path = 'V:/Final_Project/DBA'
count = 10001
for link in resume_links:
    link.click()
    handles = driver.window_handles
    for handle in handles:
        print("------------")
        driver.switch_to.window(handle)
        print(driver.current_window_handle)
        # if(driver.currrent_window_handle != parent):
        if(driver.title != parent):
            child_link = driver.current_url
            print(child_link)
            file_name = 'Resume'+str(count)+'.html'
            complete_name = os.path.join(save_path, file_name)
            file_object = codecs.open(complete_name, "w", "utf-8")
            html = driver.page_source
            file_object.write(html)
            f = complete_name[:-5] + '.pdf'
            print('Converted '+f)
            pdfkit.from_file(complete_name, f,configuration=config) 
            driver.close()
    break
    count += 1
    driver.switch_to.window(parent_handle)
    # driver.quit()



# <a class="p_l" href="https://freesearch.naukri.com/preview/preview?uname=0602aa9878898eef9cdf423e0d7b0159050c550d1b515c4557585f0c084f5048635e4c52481d460e560c6&amp;sid=4246062447&amp;LT=1611290617" id="0" target="_blank">DevOps Engineer seeking roles in Software Configuration Management,Build Management,Release Management,Continuous Integration,Application Deployment,Maven,Jenkins,Git,Ansible,Apache-Tomcat,Putty,MS...</a>