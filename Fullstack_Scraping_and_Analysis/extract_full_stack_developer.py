import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os
import pickle

driver = webdriver.Chrome()
url = 'https://www.naukri.com/full-stack-developer-jobs'
driver.get(url)
time.sleep(4)

parent_handle = driver.current_url
print(parent_handle)


dict_links = {}
count = 0
# 5900
for k in range(5001,5900):
    if k == 1:
        a = driver.find_elements_by_class_name("title.fw500.ellipsis")
        for i in a:
            if (str(i.get_attribute('href')) != 'None'):
                count += 1
                dict_links[count] = i.get_attribute('href')
    else:
        url = 'https://www.naukri.com/full-stack-developer-jobs-'+str(k)
        # print(url)
        driver.get(url)
        time.sleep(3)
        a = driver.find_elements_by_class_name("title.fw500.ellipsis")
        for i in a:
            if (str(i.get_attribute('href')) != 'None'):
                count += 1
                print(count)
                dict_links[count] = i.get_attribute('href')
    print("/////////////////////////////////////////////////////////")
    print(k)
    print("/////////////////////////////////////////////////////////")

print(len(dict_links))


# for i in dict_links:
#     print(i,dict_links[i])

# df = pd.Series(dict_links).to_frame()
# df.columns = ["Links"]
# df.to_csv("full_stack_developer_1.csv",header=False)

# df = pd.read_csv("full_stack_developer_1.csv") 
# print(df.head())

# file_to_write = open("full_stack_developer1.pickle", "wb")

# pickle.dump(dict_links, file_to_write)


with open("full_stack_developer6.pickle", "wb") as h:
    pickle.dump(dict_links, h)

df = pd.read_pickle(r'full_stack_developer6.pickle')
print(len(df))
# print(df)

d = {}
for i in df:
    if(df[i] in d):
        d[df[i]] += 1
    else:
        d[df[i]] = 0
print(len(d))

