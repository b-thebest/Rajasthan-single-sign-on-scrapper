from tkinter import *
from tkinter.ttk import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
def runbot(entries):


    import time

    #s1 = pd.read_excel('person_details.xlsx', 'Sheet1')

    #Defining browser
    #browser = webdriver.Chrome(str(os.getcwd()) + "/chromedriver")
    browser: WebDriver = webdriver.Firefox(executable_path ='geckodriver')
    browser.get('https://sso.rajasthan.gov.in/signin')
    browser.implicitly_wait(15)


    #  Input form ------

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

    #if number_of_seats > s1['Name'].count():
    if number_of_seats > len(entries):
        table_id = browser.find_element_by_id('tblMemberInfo')
        rows = table_id.find_elements(By.XPATH, ".//*[contains(@id,'tbdMemberInfo')]") # get all of the rows in the table
        k = 0
        print("number of rows found ", len(rows))
        numberOfMembers = len(entries)
        print("number of records to enter ", numberOfMembers)
        maxK = numberOfMembers
        SHORT_TIMEOUT = 0.25
        LONG_TIMEOUT = 0.25
        LOADING_ELEMENT_XPATH = '//*[@id="xPath"]/xPath/To/The/Loading/Element'
        for j in range(numberOfMembers):
            if entries[j][2].get() != '--select--' and entries[j][2].get() != '--select--' and entries[j][3].get() != '--select--':
                for i in range(6):
                    print(entries[j][i].get())

                browser.implicitly_wait(5)
                # name
                label = 'Member' + 'Name' + str(j)
                element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, label)))
                element.clear()
                element.send_keys(entries[j][0].get())
                element.send_keys(Keys.TAB)
                time.sleep(0.25)

                #blockUI blockMsg blockPage

                # gender
                label = 'Member' + 'Gender' + str(j)
                element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, label)))
                element.send_keys(str(entries[j][1].get()))
                element.send_keys(Keys.TAB)
                #time.sleep(0.25)

                # nationality
                label = 'Member' + 'Nationality' + str(j)
                element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, label)))
                element.send_keys(str(entries[j][2].get()))
                element.send_keys(Keys.TAB)
                try:
                    #load_element = browser.find_element_by_class_name('blockUI.blockMsg.blockPage')[0]
                    WebDriverWait(browser, SHORT_TIMEOUT
                                  ).until(EC.presence_of_element_located((By.CLASS_NAME, 'blockUI.blockMsg.blockPage')))
                    WebDriverWait(browser, LONG_TIMEOUT
                                  ).until_not(EC.presence_of_element_located((By.CLASS_NAME, 'blockUI.blockMsg.blockPage')))
                except TimeoutException:
                    pass
                #time.sleep(1)

                # ID type
                label = 'Member' + 'IdType' + str(j)
                element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, label)))
                hov0 = ActionChains(browser).move_to_element(element)
                hov0.perform()
                element.send_keys(str(entries[j][3].get()))
                element.send_keys(Keys.TAB)
                try:
                    #load_element = browser.find_element_by_class_name('blockUI.blockMsg.blockPage')[0]
                    WebDriverWait(browser, SHORT_TIMEOUT
                                  ).until(EC.presence_of_element_located((By.CLASS_NAME, 'blockUI.blockMsg.blockPage')))
                    WebDriverWait(browser, LONG_TIMEOUT
                                  ).until_not(EC.presence_of_element_located((By.CLASS_NAME, 'blockUI.blockMsg.blockPage')))
                except TimeoutException:
                    pass
                #time.sleep(0.25)

                # ID No,
                label = 'Member' + 'IdNo' + str(j)
                element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, label)))
                element.clear()
                element.send_keys(str(entries[j][4].get()))
                element.send_keys(Keys.TAB)
                try:
                    #load_element = browser.find_element_by_class_name('blockUI.blockMsg.blockPage')[0]
                    WebDriverWait(browser, SHORT_TIMEOUT
                                  ).until(EC.presence_of_element_located((By.CLASS_NAME, 'blockUI.blockMsg.blockPage')))
                    WebDriverWait(browser, LONG_TIMEOUT
                                  ).until_not(EC.presence_of_element_located((By.CLASS_NAME, 'blockUI.blockMsg.blockPage')))
                except TimeoutException:
                    pass
                #time.sleep(1)

                #  Video camera
                label = 'MemberTotalCamera' + str(j)
                # element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, label)))
                element = browser.find_element_by_id(label)
                hov = ActionChains(browser).move_to_element(element)
                hov.perform()

                element.send_keys(str(entries[j][5].get()))
                element.send_keys(Keys.TAB)
                try:
                    #load_element = browser.find_element_by_class_name('blockUI.blockMsg.blockPage')[0]
                    WebDriverWait(browser, SHORT_TIMEOUT
                                  ).until(EC.presence_of_element_located((By.CLASS_NAME, 'blockUI.blockMsg.blockPage')))
                    WebDriverWait(browser, LONG_TIMEOUT
                                  ).until_not(EC.presence_of_element_located((By.CLASS_NAME, 'blockUI.blockMsg.blockPage')))
                except TimeoutException:
                    pass
                time.sleep(2)

    while True:
        pass