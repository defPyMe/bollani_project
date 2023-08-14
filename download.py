from selenium.webdriver.common.by import By
from countdown import countdown 

#CSS SELECTOR SEEMS TO CHANGE AT A PAGE LEVEL , 
#SO ALL THE DOWNLOADS ON TYHE SAME PAGE SHOLD HAVE THE SAME ARGUMENT 


#'a[href*="Mo_vista_sn"][href*="export=xls/exportEnt=Mo_vista_sn"]'



def download_excel(driver, css_selector):
    print("css_selector", css_selector)
    
    image = driver.find_element(By.CSS_SELECTOR, css_selector)
    countdown(4)
    image.click()#'a[href*="Mo_vista_uds"][href*="export=xls/exportEnt=Mo_vista_uds"]'
    countdown(1260)