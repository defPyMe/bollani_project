#accesses any page in the homepage depending on the parameter page inserted in the function 
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def accessing_DC4(page, driver, user, passw):
    print("Accessing DC4")
    try:
        time.sleep(3)
    #start isolating all the values 
        element = driver.find_element(By.NAME, "cliente")
        element.click()
        #click, send keys down, enter
        time.sleep(2)
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        element.send_keys(Keys.RETURN)
        time.sleep(2)
        #credentials for accessing 
        USER = user 
        PASS = passw
        #isolating the elements needed for the completion
        #what happens after a page has been turned??
        username_element = driver.find_element(By.NAME, "username")
        password_element = driver.find_element(By.NAME, "password")
        username_element.send_keys(USER)
        password_element.send_keys(PASS)
        #isolating by text 
        time.sleep(2)
        Login = driver.find_element(By.CLASS_NAME, "inputButton")
        Login.send_keys(Keys.RETURN)
        
        time.sleep(2)
        #working up until now
        time.sleep(3)
        #accesing monitoraggi here 
        Monitoraggi = driver.find_element(By.LINK_TEXT, 'Monitoring').click()
        time.sleep(2)
        Serial_number = driver.find_element(By.LINK_TEXT, page).click()
        time.sleep(10)
        print("accessed DC4")
    except:
        print("""Some error occurred while trying to access the site,
              try again checking username and password credentials""")
        
#needed because the last two downloads are in a different pageì
def accessing_US(driver, page):
    Serial_number = driver.find_element(By.LINK_TEXT, page).click()
    time.sleep(5)
    
