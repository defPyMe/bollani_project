import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from isolating_writing import isolating_and_writing



#no need for webdrivers as i insert in a module where i am already conected
#do i need here the elements to use for the isolation of the values 
def CleaningForm(driver, calendar_movement_type_input, calendar_movement_type_option_input,
                  flusso_type_input, flusso_options_input, division_type_input,
                  division_options_input):
    #ewebElement.sendKeys(Keys.CONTROL + "a")
    #webElement.sendKeys(Keys.DELETE)
    #trying to initialize them again
    calendar_movement_type = driver.find_element(By.NAME, calendar_movement_type_input)
    calendar_movement_type_option = driver.find_element(By.NAME,  calendar_movement_type_option_input)
    flusso_type = driver.find_element(By.NAME,  flusso_type_input)
    flusso_options= driver.find_element(By.NAME, flusso_options_input)
    division_type = driver.find_element(By.NAME, division_type_input)
    division_options = driver.find_element(By.NAME,  division_options_input)
    #after initialization i clean 
    calendar_movement_type.send_keys(Keys.CONTROL + "a")
    calendar_movement_type.send_keys(Keys.DELETE)
    #cleaning second element
    calendar_movement_type_option.send_keys(Keys.CONTROL + "a")
    calendar_movement_type_option.send_keys(Keys.DELETE)
    #cleaning third element
    flusso_type.send_keys(Keys.CONTROL + "a")
    flusso_type.send_keys(Keys.DELETE)
    
    flusso_options.send_keys(Keys.CONTROL + "a")
    flusso_options.send_keys(Keys.DELETE)
    
    division_type.send_keys(Keys.CONTROL + "a")
    division_type.send_keys(Keys.DELETE)
    
    division_options.send_keys(Keys.CONTROL + "a")
    division_options.send_keys(Keys.DELETE)
    return None




def FillingForm(driver, type_, flow, division, calendar_movement_type_input, 
                calendar_movement_type_option_input, flusso_type_input, 
                flusso_options_input, division_type_input, division_options_input):
    
    #isolating tipo movimento
    calendar_movement_type = driver.find_element(By.NAME, calendar_movement_type_input)
    select = Select(calendar_movement_type)
    # Select an option by its visible text
    select.select_by_visible_text('Equal to')
    calendar_movement_type_option = driver.find_element(By.NAME, calendar_movement_type_option_input)
    select = Select(calendar_movement_type_option)
    time.sleep(2)
    #to select Spedizione, Spunta Serial Number ##variables 
    select.select_by_visible_text(type_)
    
    
    #isolating flusso
    flusso_type = driver.find_element(By.NAME, flusso_type_input)
    select = Select(flusso_type)
    # Select an option by its visible text
    select.select_by_visible_text('Equal to')
    flusso_options= driver.find_element(By.NAME, flusso_options_input)
    #variable either bj2jit, b2b , REM 
    flusso_options.send_keys(flow)
    
    
    #isolating division
    division_type = driver.find_element(By.NAME, division_type_input )
    select = Select(division_type)
    # Select an option by its visible text
    select.select_by_visible_text('Equal to')
    division_options = driver.find_element(By.NAME, division_options_input)
    select = Select(division_options)
    # different options such as MRP/NAP 
    select.select_by_visible_text(division)
    #applying filter
    filter_button = driver.find_element(By.NAME, "applyFilter").click()
    

    time.sleep(45)
    print(f"Filling in form  for {type_}, {flow},  {division}")
    #
    #SPLITING AS I NEED TO GET HERE THE VALUES ISOLATED 
    #
    isolating_and_writing(driver, type_, flow, division)
    
    pass


