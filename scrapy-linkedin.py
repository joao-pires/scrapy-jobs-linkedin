from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from parsel import Selector
import csv
import argparse
from argparse import RawTextHelpFormatter
from bs4 import BeautifulSoup
import sys

JOB=sys.argv[1]
LOCAL=sys.argv[2]

# csv file
writer = csv.writer(open('jobs_info_linkedin.csv', 'w', encoding='utf-8'))
writer.writerow(['Empresa','Local','Cargo','Requisitos', 'URL'])

# Chrome driver
driver = webdriver.Chrome()

# Google
driver.get('https://google.com')

# Search fild
search_input = driver.find_element_by_name('q')

# Google search
search_input.send_keys('site:linkedin.com/jobs AND "{}" and "{}"'.format(JOB,LOCAL))
search_input.send_keys(Keys.ENTER)
sleep(2)

# Select jobs page
select_page = driver.find_element_by_xpath('//div[@class="yuRUbf"]/a').get_attribute('href')
sleep(2)
driver.get(select_page)
sleep(5)

# Set number jobs 
number_of_jobs = 25
i = 2
while i <= (number_of_jobs/25): 
    driver.find_element_by_xpath('/html/body/main/div/section/button').click()
    i = i + 1
    sleep(5)

pageSource = driver.page_source
lxml_soup = BeautifulSoup(pageSource, 'lxml')

# Extract URLs
jobs_list = driver.find_elements_by_class_name("result-card__full-card-link")
jobs_link = [perfil.get_attribute('href') for perfil in jobs_list]


# Extract Informations
for perfil in jobs_link:
    driver.get(perfil)
    sleep(4)

    jobs_function = driver.find_element_by_xpath('/html/body/main/section[1]/section[2]/div[1]/div[1]/h1').text
    company_name = driver.find_element_by_xpath('/html/body/main/section[1]/section[2]/div[1]/div[1]/h3[1]/span[1]').text
    jobs_description = driver.find_element_by_xpath('/html/body/main/section[1]/section[3]/div/section/div').text
    local = driver.find_element_by_xpath('/html/body/main/section[1]/section[2]/div[1]/div[1]/h3[1]/span[2]').text
    jobs_link = perfil

    # Write in .csv file
    writer.writerow([company_name,local,jobs_function,jobs_description, jobs_link])

# Power Off Driver
driver.quit()
