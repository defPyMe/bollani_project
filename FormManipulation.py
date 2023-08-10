import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from isolating_writing import isolating_and_writing
from countdown import countdown
#imorting download functtion
from download import download_excel
#getting the file
from GetFile import file_name, removeFile
#importing the processed function
from processing_downloaded_file import processing_file

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


    # some things are the added aas a dictionary as we are isolating the options, teh second dictionary is used for teh values to be pushed
    FillingForm(driver, {"filter[Mo_vista_sn][F34][select]" : 'Equal to',  "filter[Mo_vista_sn][F34][from]": 'Equal to', "filter[Mo_vista_sn][F21][select]" : 'Equal to'}, 
                { "filter[Mo_vista_sn][F21][from]":'PO'}, 0, "BOOKING IN")
    """



#maybe the args is a better solution here as a tuple is returned 

def FillingForm(*args):
    #driver is teh first, the rest is stored in a dictionary 
    args_ = args
    #need to do it in a loop because there are different lenghts in the inputs 
    #accessing the elements in the elements list
    
#NOT SURE HERE IT IS WORKING CORRECTLY 
#HOW DO I ACCESS THE SECOND LIST?     
    #using a filter for opening or not the advanced filter so that i can add all teh values to teh first dictionary 
    if args_[2] == 0:
            #not doing anything here so as to write the looking for applying filter only once 
        pass
    else:    
            #the only one that i am using is for the monitor serial number
        advanced_filter = args_[0].find_elemen(By.XPATH, "//input[@value='Advanced filter']").click()
        #shouldn t need too much sleep there 
        time.sleep(2)
        #now i add teh valuesi have inside the list 
        
    
    for i in args_[1]:
        # NEEDS TO SEE IF IT ACTUALLY WORKS OR NOT WHEN NEW PAGE IS OPEN -- ADDED IN THE FIRST LIST 
        #how do we get the different elemets 
        
        possible_options = ["Equal to", "Different from", "Select, Equal to", "Different from", "Greater than", "Greater or equal to", "Less than", "Less than or equal to", "Between", "Not between"
                            ,"In list" 	,"Not in list" 	,"Begins with" ,"Not starting with" ,"Contains" ,"Does not contain" ,"Ends with" ,"Non ending with" ,"Empty" ,"Not empty", "Select", "Inbound", 
                            "Inventory" ,"Picking" ,"Refilling" ,"Reload" ,"Change Classification","Correction","Shipment","Putaway","Movement","Check Serial Numbers"
                            ,"Sorting","UT Load","Unload UT","Deliver in Work Area","Discharge from Work Operation","Change Stock To Order","Recoding"]
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
            looped_element= args_[0].find_element(By.NAME,i)# flusso_options_input
            #variable either bj2jit, b2b , REM 
            #here it goes in the second dictionary 
            looped_element.send_keys(args_[1][i])#flow)
            pass

        #then just filter it out 
        filter_button = args_[0].find_element(By.NAME, "applyFilter").click()
        #usually enough to download teh file correctly 
        countdown(45)
        
        #flag number 4 is the one where we decideif teh value is to be islated on the page or if we have to download a file
        if args_[4] == 1:
            #then we isolate the value in the page 
            isolating_and_writing(args_[0],args_[3])
            pass
        else:
            
            #here we download directly and apply a certain processing
            #args five is teh flag we use to get the type of processing we need, it is a flag present in all instances that end up here 
            
            
            
            
            #download_file
            #since i am dowwloading always an excel file i will have to isolatre always the same element 
            download_excel(args_[0], args_[5])
            #waiting for teh download to take effect
            countdown(300)
            #look for file, similar to the function already used but it also erases the file
            found = file_name()
            if found != "":
                #if the filename is not empty we found the file 
                    #process_file(file, processing_code)
                    #args_3 as the processing flag with teh name of what we are downloading, assigning it to an obj as it is the 
                    processed = processing_file(found, args_[3])
                    #writing to file now, should be the same for all cases 
                    isolating_and_writing(args_[0], processed)
                    #deleting the file 
                    removeFile(found)
            else:
                print("file not found for the downloading of -->  ", args_[3])
                
            
      
          
            
            
            
            
        
#ISOLATING AND WRITING HERE GETS DIFFERENT VALUES BASED ON THE CASE WE ARE IN
#SO I NEED TO MAKE THIS GENERAL OR RETURNING A SINGLE VALUE WITH TEH FUNCTIONS 
        
    
#not sure i need to print anything here... maybe that i am isolating the values for a certain value in the invoice 
#passing in what we are calculating a sthe argument number 3 in args_
        print(f"Filling in form  for {args_[3]}")
#last flag to ee if we need to download a file opr not 



        #isolating_and_writing(args_[0],args_[7], args_[8],  args_[9])#type_, flow, division
    pass


