import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from isolating_writing import isolating_and_writing



#no need for webdrivers as i insert in a module where i am already conected
#do i need here the elements to use for the isolation of the values 

"""
    driver, calendar_movement_type_input, calendar_movement_type_option_input,
                  flusso_type_input, flusso_options_input, division_type_input,
                  division_options_input
    
"""



def CleaningForm(**kwargs):
    #assigning the args to a variable to be accessed , driver always the first
    args_ = kwargs
    #getting the case where we have the three direct downloads
    if len(args_)==7:
        #isolating the elements with the progressive args 
        calendar_movement_type = args_[0].find_element(By.NAME, args_[1] )#calendar_movement_type_input
        calendar_movement_type_option = args_[0].find_element(By.NAME, args_[2] ) #calendar_movement_type_option_input
        #need to add here the movement type 
        movement_type = args_[0].find_element(By.NAME, args_[3] )#division_type_input
        movement_type_options = args_[0].find_element(By.NAME, args_[4])# division_options_input
        #nflusso now
        flusso_type = args_[0].find_element(By.NAME, args_[5] )# flusso_type_input
        flusso_options= args_[0].find_element(By.NAME, args_[6])#flusso_options_input
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
        
        movement_type.send_keys(Keys.CONTROL + "a")
        movement_type.send_keys(Keys.DELETE)
        
        movement_type_options.send_keys(Keys.CONTROL + "a")
        movement_type_options.send_keys(Keys.DELETE)
    return None




"""
    
driver, type_, flow, division, calendar_movement_type_input, 
                calendar_movement_type_option_input,movement_type, movement_type_options , flusso_type_input, 
                flusso_options_input,


"""


def FillingForm(**kwargs):
    #driver is teh first
    args_ = kwargs
    #isolating tipo movimento
    calendar_movement_type = args_[0].find_element(By.NAME,args_[1])#calendar_movement_type_input
    select = Select(calendar_movement_type)
    # Select an option by its visible text
    select.select_by_visible_text('Equal to')
    calendar_movement_type_option = args_[0].find_element(By.NAME, args_[2])#calendar_movement_type_option_input
    select = Select(calendar_movement_type_option)
    time.sleep(2)
    #to select Spedizione, Spunta Serial Number ##variables 
    select.select_by_visible_text(args_[7])#type_
    #isolating flusso
    flusso_type = args_[0].find_element(By.NAME,args_[5])#flusso_type_input
    select = Select(flusso_type)
    # Select an option by its visible text
    select.select_by_visible_text('Equal to')
    flusso_options= args_[0].find_element(By.NAME,args_[6])# flusso_options_input
    #variable either bj2jit, b2b , REM 
    flusso_options.send_keys(args_[8])#flow)
    #isolating division
    movement_type = args_[0].find_element(By.NAME,args_[3])#division_type_input 
    select = Select(movement_type)
    # Select an option by its visible text
    select.select_by_visible_text('Equal to')
    movement_type_options = args_[0].find_element(By.NAME, args_[4])#division_options_input
    select = Select(movement_type_options)
    # different options such as MRP/NAP 
    select.select_by_visible_text(args_[9])#division
    #applying filter
    filter_button = args_[0].find_element(By.NAME, "applyFilter").click()
    time.sleep(45)
    print(f"Filling in form  for {args_[7]}, {args_[8]},  {args_[9]}")
    #
    #SPLITING AS I NEED TO GET HERE THE VALUES ISOLATED 
    #
    isolating_and_writing(args_[0],args_[7], args_[8],  args_[9])#type_, flow, division
    pass


