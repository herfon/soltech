__author__ = "Khom Her"

import os
import time

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

dir = os.path.dirname(__file__)
chrome_dir = os.path.join(dir, '/Users/khomher/PycharmProjects/pythonCoding/chromedriver')

"""
Scenario: Reset the page size to 0x0
When I set the window postion to 0x0
Then the display set to default size

Scenario: Reset the page size to 1814x974
When I set the window size to 1814x974
Then the display is set to 1814x974

"""
driver=webdriver.Chrome(chrome_dir)
driver.set_page_load_timeout(30)
driver.get("http://soltech.net/")
driver.set_window_position(0,0)
driver.set_window_size(1814,974)
driver.implicitly_wait(20)

"""
Senario: Mouse over the Careers link and Click Open Positions
When I mouse over the Careers link
And I click on the Open Positions
Then I will see the Job Listings page
"""
open_position = driver.find_element_by_xpath("""//*[@id="navbar"]/div/ul/li[5]/a""").click()

"""
This line of code was commented out due to a bug in ChromeDriver to change tab.
An implicit get() was used to access "careers-soltech.icims.com/jobs/search?hashed=-435773336'.
#driver.find_element_by_link_text("Open Positions").click()
"""

"""
Scenario: Access the careers at Soltech page
When I enter the link https://careers-soltech.icims.com/jobs/search?hashed=-435773336 in the url
Then I will see the Job Listings page
"""
time.sleep(3)
driver.get("https://careers-soltech.icims.com/jobs/search?hashed=-435773336")


"""
Scenario: Search for QA jobs
Given I am at the Job Listings page
When I enter QA in the keywords field
And I select search
Then I will see jobs for QA
"""
time.sleep(3)
# swirch frame to job searh section
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
elem_search = driver.find_element_by_xpath("""//*[@id="jsb_f_keywords_i"]""")
elem_search.send_keys("qa")
driver.switch_to.default_content()

# switch frame to search button
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_xpath("""//*[@id="jsb_form_submit_i"]""").click()
driver.switch_to.default_content()


"""
Scenario: Select QA Automation Engineer link
When I select the QA Automation Engineer link
Then I will see the job ID and details
"""
# switch frame to Job listing by Title
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_xpath("""/html/body/div[2]/table/tbody/tr[1]/td[1]/a""").click()
driver.switch_to.default_content()

"""
Scenario: Printing to console of Job ID 
Given I am at the job detail page
When I run print() of the header
And I run print() of the id
Then I will see the header and id in the console
"""
# switch frame to Job Detail page
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
elem_header = driver.find_element_by_class_name("iCIMS_Header")
elem_id = driver.find_element_by_class_name("iCIMS_JobHeaderData")
print("*** Printing to console ***")
print("Job Title: ", elem_header.text, "ID: ", elem_id.text)
driver.switch_to.default_content()

time.sleep(5)
driver.quit()

