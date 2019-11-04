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
while True:
    try:
        browser.find_element_by_xpath('//*[@id="cpBody_dlApplications_LinkButton2_0"]').click()
        break
    except:
        time.sleep(1)
while True:
    try:
        ticket = browser.find_element_by_class_name('fa.fa-ticket.fa-fw').click()
        break
    except:
        time.sleep(2)
while True:
    try:
        browser.find_element_by_xpath('//a[@href="'+'/BookOnlineTicket/BookOnlineTicket?CT=QWR2YW5jZQ=='+'"]').click()
        break
    except:
        time.sleep(2)
time.sleep(2)
buttons = browser.find_elements_by_class_name("close")
buttons[1].click()


#check ticket availability
#fields = browser.find_elements(By.XPATH, ".//*[contains(@class,'col-lg-6')]")
label = 'ddl_place'
place = browser.find_element_by_xpath('//select[@id="ddl_place"]')
place.click()

#"//select[@name='element_name']/option[text()='option_text']"
#element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, label)))
#select = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, '')))
#Select(element).select_by_visible_text("Ranthambore National Park - Sawai Madhopur")

label = 'ddl_Zone'
element = Select(WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, label))))
element.select_by_visible_text("Zone 1")

label = 'txt_dateofarrival'
element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, label)))
element.click()
element.send_keys('27/11/2019')

label = 'ddl_Shift'
element = Select(WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, label))))
element.select_by_visible_text('Morning')

label = 'ddl_vehicle'
element = Select(WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, label))))
element.select_by_visible_text('Gypsy')


# start filling details



#table_id = browser.find_element_by_class_name('panel-body')
#rows = table_id.find_elements(By.XPATH, ".//*[contains(@id,'tblMemberInfo')]")  # get all of the rows in the table

##BUTTON CLOSE KARNE WALA CLICK KARNA HAI DIALOG BOX HATANE K LIYE
close = browser.find_elements_by_class_name('close')
print(len(close))
#close[4].click()

'''
# Check in
browser.find_element_by_xpath('//*[@id="tbAccChkIn"]').clear()
browser.find_element_by_xpath('//*[@id="tbAccChkIn"]').click()
browser.find_element_by_xpath('//*[@id="tbAccChkIn"]').send_keys(str(s1['Check In'][i]).replace('-', '/'))

# Check out
browser.find_element_by_xpath('//*[@id="tbAccChkOut"]').clear()
browser.find_element_by_xpath('//*[@id="tbAccChkOut"]').click()
browser.find_element_by_xpath('//*[@id="tbAccChkOut"]').send_keys(str(s1['Check Out'][i]).replace('-', '/'))

# Room type
Select(browser.find_element_by_xpath('//*[@id="ddlAccType"]')).select_by_visible_text(s1['Room Type'][i])

# Rooms
time.sleep(3)
Select(browser.find_element_by_xpath('//*[@id="ddlNoofRoom"]')).select_by_visible_text(str(int(s1['Rooms'][i])))
#Select(browser.find_element_by_xpath('//*[@id="ddlNoofRoom"]')).select_by_visible_text('2')
# Submit
t = 0

while t < 4:
    try:
        browser.find_element_by_xpath('//*[@id="lnkSearchAvailability"]').click()
        t = 4
    except:
        time.sleep(1)
        t += 1

#check checkbox if any 
flaghouse=False
hotelTable = browser.find_element_by_xpath('//*[@id="dlouterDataList_ctl00_dlShowAvailability"]')
hotelrows = hotelTable.find_elements(By.TAG_NAME, "tr")
for row in hotelrows:
    print(row.find_elements(By.TAG_NAME, "td")[1].text)
    if(row.find_elements(By.TAG_NAME, "td")[1].text == str(s2['Select_Location'][0])):
        #we found the element
        row.find_element_by_xpath(".//input[@type='checkbox']").click()
        flaghouse=True
        break
if(flaghouse):
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="btnProceed"]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="btnAccConfYes"]').click()
    delay=4
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'divSessionTimer')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
else:
    exit()

#start filling details 
table_id = browser.find_element_by_class_name('table-fill')
rows = table_id.find_elements(By.XPATH, ".//*[contains(@id,'G1tr')]") # get all of the rows in the table
k=0
print("number of rows found ",len(rows))
numberOfMembers = s3['Name'].count()
print("number of records to enter ",numberOfMembers)
numberOfRows = 2*(int(s1['Rooms'][i]))
maxK = min(numberOfMembers,numberOfRows)
for row in rows:
    j = k+1
    # Get the columns (all the column 2)
    # name        
    
    label = 'V'+str(j)+'Name'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    element.send_keys(s3['Name'][k])
    #gender
    label = 'V'+str(j)+'Gender'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    Select(element).select_by_visible_text(s3['Gender'][k])
    
    #age
    label = 'V'+str(j)+'Age'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    element.send_keys(str(int(s3['age'][k])))

    #country
    label = 'V'+str(j)+'country'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    Select(element).select_by_visible_text(s3['country'][k])

    #ID Type
    label = 'V'+str(j)+'ddlIDproof'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    Select(element).select_by_visible_text(s3['ID Type'][k])

    #idproof
    label = 'V'+str(j)+'tbIdProofNumber'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    element.send_keys(str(s3['ID proof'][k]))
    
    #mobile
    label = 'V'+str(j)+'mobileno'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    element.send_keys(str(s3['Mobile No.'][k]))
    k += 1
    if(k>=maxK):
        break


#start filling details 
rows = table_id.find_elements(By.XPATH, ".//*[contains(@id,'chld')]") # get all of the rows in the table
k=0
print("number of rows found ",len(rows))
numberOfMembers = s4['Name'].count()
print("number of records to enter ",numberOfMembers)
numberOfRows = (int(s1['Rooms'][i]))
maxK = min(numberOfMembers,numberOfRows)
for row in rows:
    j = k+1
    # Get the columns (all the column 2)
    # name        
    
    label = 'chld'+str(j)+'Name'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    element.send_keys(s4['Name'][k])
    #gender
    label = 'chld'+str(j)+'Gender'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    Select(element).select_by_visible_text(s4['Gender'][k])
    
    #age
    label = 'chld'+str(j)+'Age'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    element.send_keys(str(int(s4['age'][k])))

    #country
    label = 'chld'+str(j)+'country'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    Select(element).select_by_visible_text(s4['country'][k])

    #ID Type
    label = 'chld'+str(j)+'ddlIDproof'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    Select(element).select_by_visible_text(s4['ID Type'][k])

    #idproof
    label = 'chld'+str(j)+'tbIdProofNumber'
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,label)))
    element.send_keys(str(s4['ID proof'][k]))
    
    
    k += 1
    if(k>=maxK):
        break

#accept TOC
browser.find_element_by_xpath('//*[@id="TOC"]').click()
browser.find_element_by_xpath('//*[@id="btnProceed"]').click()
'''