from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import sys

JOB=sys.argv[1]
LOCAL=sys.argv[2]

# csv file
writer = csv.writer(open('jobs_info_linkedin.csv', 'w', encoding='utf-8'))
writer.writerow(['Company','Location','Post','Description', 'Url'])

# Chrome driver
driver = webdriver.Chrome('/home/joaopires/scrapy-jobs-linkedin-main/chromedriver')

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

# Extract URLs
jobs_list = driver.find_elements_by_class_name("base-card__full-link")
jobs_link = [perfil.get_attribute('href') for perfil in jobs_list]  


# Extract Informations
for perfil in jobs_link:
    driver.get(perfil)
    sleep(4)

    jobs_function = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h1').text
    company_name = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[1]/a').text
    jobs_description = driver.find_element_by_class_name("show-more-less-html__markup").text
    local = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[2]').text
    jobs_link = perfil
    

    # Write in .csv file
    writer.writerow([company_name,local,jobs_function,jobs_description, jobs_link])

# Power Off Driver
driver.quit()
