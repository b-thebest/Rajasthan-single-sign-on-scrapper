from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pandas as pd
import time

s1 = pd.read_excel('person_details.xlsx', 'Sheet1')

#Defining browser
#browser = webdriver.Chrome(str(os.getcwd()) + "/chromedriver")
browser = webdriver.Firefox()
browser.get('https://sso.rajasthan.gov.in/signin')
browser.implicitly_wait(15)

i = 0

# First form --------
browser.find_element_by_xpath('//*[@id="cpBody_txt_Data1"]').send_keys('DAILYTOUR360')
browser.find_element_by_xpath('//*[@id="cpBody_txt_Data2"]').send_keys('DTT4SHALU')

input('Press enter after solving captcha')
'''//*[@id="bt_login"]/i'''


# Close pop up
try:
    browser.find_element_by_xpath('//*[@id="cpBody_btn_LDAPLogin"]').click()
except:
    print('no pop up was found')

# Second form ------
#element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "cpBody_dlApplications_LinkButton2_0")))
browser.implicitly_wait(10)
try:
    browser.find_element_by_xpath('//*[@id="cpBody_txt_Data2"]').send_keys('DTT4SHALU')
    time.sleep(1)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'cpBody_cbx_newsession'))).click()
    browser.find_element_by_xpath('.//*[@id="cpBody_btn_LDAPLogin"]').click()
except:
    time.sleep(1)

browser.implicitly_wait(10)
#element = WebDriverWait(browser, 10).until_not(EC.visibility_((By.ID, "cpBody_dlApplications_LinkButton2_0")))
element = browser.find_element_by_id("cpBody_dlApplications_LinkButton2_0")
browser.execute_script("arguments[0].click();", element)

browser.implicitly_wait(10)
elem = browser.find_elements_by_class_name("fa.fa-ticket.fa-fw")
browser.execute_script('arguments[0].click();', elem[0])
browser.implicitly_wait(3)
elem = browser.find_element_by_xpath('//a[@href="/BookOnlineTicket/BookOnlineTicket?CT=QWR2YW5jZQ=="]')
browser.execute_script('arguments[0].click();', elem)

'''while True:
    try:
        #WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "fa.fa-ticket.fa-fw"))).click()
        #WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/BookOnlineTicket/BookOnlineTicket?CT=QWR2YW5jZQ==']"))).click()
        elem = browser.find_elements_by_class_name("fa.fa-ticket.fa-fw")
        elem[0].click()
        browser.implicitly_wait(1)
        #WebDriverWait(browser, 10).until(EC.presence_of_element_located(
         #   (By.XPATH, "//a[@href='/BookOnlineTicket/BookOnlineTicket?CT=QWR2YW5jZQ==']"))).click()
        browser.find_element_by_xpath('//a[@href="/BookOnlineTicket/BookOnlineTicket?CT=QWR2YW5jZQ=="]').click()
        break
    except:
        time.sleep(2)'''

try:
    browser.implicitly_wait(4)
    buttons = browser.find_elements_by_class_name("close")
    buttons[1].click()
except:
    pass

number_of_seats = None
while True:
    text = browser.find_element_by_xpath('//*[@id="lbl_NumberofMembersavailable"]').text
    if text != '':
        print(text)
        number_of_seats = int(text.split(': ')[1])
        print(number_of_seats)
        break
    time.sleep(2)

if number_of_seats > s1['Name'].count():
    table_id = browser.find_element_by_id('tblMemberInfo')
    rows = table_id.find_elements(By.XPATH, ".//*[contains(@id,'tbdMemberInfo')]")  # get all of the rows in the table
    k = 0
    print("number of rows found ", len(rows))
    numberOfMembers = s1['Name'].count()
    print("number of records to enter ", numberOfMembers)
    maxK = numberOfMembers + 1
    for j in range(numberOfMembers):
        browser.implicitly_wait(5)

        # name
        label = 'Member' + 'Name' + str(j)
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, label)))
        element.send_keys(s1['Name'][j].title())
        element.send_keys(Keys.TAB)
        time.sleep(0.25)

        # gender
        label = 'Member' + 'Gender' + str(j)
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, label)))
        element.send_keys(s1['Gender'][j].title())
        element.send_keys(Keys.TAB)
        time.sleep(0.25)

        # nationality
        label = 'Member' + 'Nationality' + str(j)
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, label)))
        element.send_keys(s1['Nationality'][j].title())
        element.send_keys(Keys.TAB)
        time.sleep(0.25)

        # ID type
        label = 'Member' + 'IdType' + str(j)
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, label)))
        element.send_keys(s1['ID_type'][j])
        element.send_keys(Keys.TAB)
        time.sleep(0.25)

        # ID No,
        label = 'Member' + 'IdNo' + str(j)
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, label)))
        element.clear()
        element.send_keys(str(s1['ID_no'][j]))
        element.send_keys(Keys.TAB)
        time.sleep(0.5)

        # Video camera
        label = 'MemberTotalCamera' + str(j)
       # element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, label)))
        element = browser.find_element_by_id(label)
        element.send_keys(str(s1['Num_of_Camera'][j]))
        element.send_keys(Keys.TAB)
        time.sleep(1)

while True:
    pass