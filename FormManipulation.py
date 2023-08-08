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


#the driver is added and a list of teh fields io need to clean
def CleaningForm(*args):
    #assigning the args to a variable to be accessed , driver always the first
    args_ = args
    #getting the case where we have the three direct downloads
    for i in args_[1]:
        #isolating the elements with the progressive args 
        looping_cleaning = args_[0].find_element(By.NAME, i )#calendar_movement_type_inpu
        looping_cleaning.send_keys(Keys.CONTROL + "a")
        looping_cleaning.send_keys(Keys.DELETE)
    return None




"""
    
driver, type_, flow, division, calendar_movement_type_input, 
                calendar_movement_type_option_input,movement_type, movement_type_options , flusso_type_input, 
                flusso_options_input,




    FillingForm(connection = driver, movement_type = "filter[Mo_vista_sn][F34][select]", movement_type_options = "filter[Mo_vista_sn][F34][from]", 
                flow_type =  "filter[Mo_vista_sn][F21][select]", flow_type_options =  "filter[Mo_vista_sn][F21][from]", movement_type_value = "Putaway", flow_value = "PO")

"""





"""
possible options :     Equal to, Different from,  Select, Equal to, 	Different from, Greater than, 	Greater or equal to,  Less than,  Less than or equal to,  Between, Not between 	,In list 	,Not in list 	,Begins with 
,Not starting with 		,Contains 			,Does not contain 		,Ends with 		,Non ending with 	,Empty 			,Not empty 	
    """



#maybe the args is a better solution here as a tuple is returned 

def FillingForm(*args):
    #driver is teh first, the rest is stored in a dictionary 
    args_ = args
    #need to do it in a loop because there are different lenghts in the inputs 
    #accessing the elements in the elements list
    for i in args_[1]:
        #isolating tipo movimento
        
        
        
        #how do we get the different elemets 
        
        possible_options = ["Equal to", "Different from", "Select, Equal to", "Different from", "Greater than", "Greater or equal to", "Less than", "Less than or equal to", "Between", "Not between"
                            ,"In list" 	,"Not in list" 	,"Begins with" ,"Not starting with" ,"Contains" ,"Does not contain" ,"Ends with" ,"Non ending with" ,"Empty" ,"Not empty"]
        #the differences are that the selet by text re aklways the same or at least predictable 
        #so if teh value of teh key is in the checklist then we 
        if args_[1][i] in possible_options:
            #if it is in possible options then we are dealing with a drop down menu
            looping_elements = args_[0].find_element(By.NAME,i)#calendar_movement_type_input
            select = Select(looping_elements)
            # Select an option by its visible text, it is a value in the dictionary 
            #some of them have the visible text option , the others do not 
            select.select_by_visible_text(args_[1][i])
        else:
            flusso_options= args_[0].find_element(By.NAME,i)# flusso_options_input
            #variable either bj2jit, b2b , REM 
            flusso_options.send_keys(args_[1][i])#flow)
            #isolating division
        
#here i need to consider also when i am applying an advanced filter or not 
#using a flag i access by index [2], if 0 then no advanced filtering, if one ther eis advanced filtering
        
    
    
    #applying filter
    filter_button = args_[0].find_element(By.NAME, "applyFilter").click()
    time.sleep(45)
    
    
    print(f"Filling in form  for {args_[7]}, {args_[8]},  {args_[9]}")
    #
    #SPLITING AS I NEED TO GET HERE THE VALUES ISOLATED 
    #
    isolating_and_writing(args_[0],args_[7], args_[8],  args_[9])#type_, flow, division
    pass


