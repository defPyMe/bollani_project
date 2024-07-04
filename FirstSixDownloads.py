
from Date_setting import DateSetting
from FormManipulation import FillingForm, CleaningForm
from Accessing import accessing_US


#thuis needs to go back every time to the previous screen 
def Form_completion(driver, input_month):

    
  
    
    
    
    
    #/----------------------------------------------------/
    #ITEM COUNT + TAG AND SORT
    DateSetting(driver,  "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", input_month, 0)
    #BOOKING IN 
    # should keep thing sin order here having the elements names and teh values to be inserted there 
    #first i get the elements then i insert the values
    #AS I HAVE ADDED A FILTER THEN I CAN ADD EVERYTHING TO TEH SINGLE LIST  
    FillingForm(driver, {"filter[Mo_vista_sn][F34][select]" : 'Equal to',  "filter[Mo_vista_sn][F34][from]": 'Putaway', 
                         "filter[Mo_vista_sn][F21][select]" : 'Equal to', "filter[Mo_vista_sn][F21][from]":'PO'}, 0, "ITEM COUNT + TAG SORT", 0)
    
    #cleaning the form , has kwargs here as well as there are differences to be considered
    CleaningForm(driver, ["filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", 
                          "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]"])
    
    #/----------------------------------------------------/
    
    
    
    #RETURNS (sum on top, as before but with RET)
    #date is to be set with the full hpours setting
    DateSetting(driver,  "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", input_month, 1)
    FillingForm(driver, {"filter[Mo_vista_sn][F34][select]" : 'Equal to',  "filter[Mo_vista_sn][F34][from]": 'Putaway', 
                         "filter[Mo_vista_sn][F21][select]" : 'Equal to', "filter[Mo_vista_sn][F21][from]":'RET'}, 0, "RETURNS", 0)
    
    #cleaning the form , has kwargs here as well as there are differences to be considered
    CleaningForm(driver, ["filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", 
                          "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]"])
    
    
    #/----------------------------------------------------/  
    
    
    
    
    #PICK SAMPLE INT 
    DateSetting(driver,  "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", input_month, 1)
    FillingForm(driver, {"filter[Mo_vista_sn][F34][select]" : 'Equal to',  "filter[Mo_vista_sn][F34][from]": 'Picking', 
                         "filter[Mo_vista_sn][F21][select]" : 'Equal to', "filter[Mo_vista_sn][F21][from]":'SAMP_I', "filter[Mo_vista_sn][F75][select]" : "Select"}, 0, "PICK SAMPLE INT", 0)
    
    #cleaning the form , has kwargs here as well as there are differences to be considered
    CleaningForm(driver, ["filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", 
                          "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]"])
    
    
    #/-----------------------------------------------------/
  
    #MANUAL PUTAWAY
    #no hours here
    DateSetting(driver,  "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", input_month, 0)
    
    FillingForm(driver, {"filter[Mo_vista_sn][F34][select]" : 'Equal to',  "filter[Mo_vista_sn][F34][from]": 'Putaway', 
                         "filter[Mo_vista_sn][F16][select]":"Different from" , "filter[Mo_vista_sn][F16][from]":"SHUTTLE"} , 1, "MANUAL PUTAWAY", 0)
    
    #cleaning the form , has kwargs here as well as there are differences to be considered
    CleaningForm(driver, ["filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", 
                          "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]",  
                          "filter[Mo_vista_sn][F16][select]", "filter[Mo_vista_sn][F16][from]" ])
    
    
    
    #/------------------------------------------------------/
    #PICKING
    DateSetting(driver,  "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", input_month, 1)
    
    FillingForm(driver, {"filter[Mo_vista_sn][F34][select]" : 'Equal to',  "filter[Mo_vista_sn][F34][from]": 'Picking', 
                        "filter[Mo_vista_sn][F15][select]":"Different from" , "filter[Mo_vista_sn][F15][from]":"SHUTTLE"} , 1, "PICKING", 0)
    
    #cleaning the form , has kwargs here as well as there are differences to be considered
    CleaningForm(driver, ["filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", 
                          "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]",  
                           "filter[Mo_vista_sn][F15][select]",  "filter[Mo_vista_sn][F15][from]" ])
    
      #BOOKING IN 
    DateSetting(driver,  "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", input_month, 1)
    # should keep thing sin order here having the elements names and teh values to be inserted there 
    #first i get the elements then i insert the values
    #AS I HAVE ADDED A FILTER THEN I CAN ADD EVERYTHING TO TEH SINGLE LIST 
    #[2] --> advanced filtering, [4] --> 0 on the same page, 1 to download.
    #[5] -- it is  teh css selector to download teh different documents 
    FillingForm(driver, {"filter[Mo_vista_sn][F34][select]" : "Equal to",  "filter[Mo_vista_sn][F34][from]": "Putaway" , 
                         "filter[Mo_vista_sn][F21][select]" : "Contains", "filter[Mo_vista_sn][F21][from]":"PO"}, 0, "BOOKING IN", 0, 'a[href*="Mo_vista_sn"][href*="export=xls/exportEnt=Mo_vista_sn"]')
    
    #cleaning the form , has kwargs here as well as there are differences to be considered
    CleaningForm(driver, ["filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", 
                          "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]"])
    
        
    #/------------------------------------------------------/
    
    #PRE PICK
    #This needs to be put into the correct page, i can change it here , as i reset to the main page i can get the button from here directly 
    
    accessing_US(driver, "US" )
    #then everything as usual accessing the elements as they come 
    DateSetting(driver,  "filter[Mo_vista_uds][D23][select]", "filter[Mo_vista_uds][D23][from]", "filter[Mo_vista_uds][D23][to]", input_month, 0)
    #chanfìging also teh input boxes as i hve changed the page now 
    FillingForm(driver, {"filter[Mo_vista_uds][F28_101][select]" : 'Equal to', "filter[Mo_vista_uds][F28_101][from]": 'B2C'} , 1, "PRE PICK", 0)
    
    #cleaning the form , has kwargs here as well as there are differences to be considered
    #also here we need to change the elements as the page is changed 
    #here i do not reset the the date fields as they are the same for the next, only to be emptied the two i need to change 
    CleaningForm(driver, ["filter[Mo_vista_uds][F28_101][select]" ,  "filter[Mo_vista_uds][F28_101][from]"])
    
    
    
    
    
    #/---------------------------------------------------------/
    #B2B JIT REPL
    # do not need to access the page anew as i have accessed it already 
    #do not set the date here as it is equal to the one above
    FillingForm(driver, {"filter[Mo_vista_uds][F28_101][select]" : 'Different from', "filter[Mo_vista_uds][F28_101][from]": 'B2C'} , 1, "PRE PICK", 0)
    
    #cleaning the form , has kwargs here as well as there are differences to be considered
    #as this is teh last i do not need to clean the form 
    
    
    
    
    
    
    
    
    """
    
    
    
    
    
    
    
    FillingForm(driver, "Shipment", "B2C", "MRP", "filter[Mo_vista_sn][F34][select]", 
                "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", 
                "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]",
                "filter[Mo_vista_sn][F75][from]")
    CleaningForm(driver,"filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]")
    #OTHER OUTBOUND
    FillingForm(driver, "Shipment", "B2BJIT", "NAP", "filter[Mo_vista_sn][F34][select]", 
                "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", 
                "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]",
                "filter[Mo_vista_sn][F75][from]")
    CleaningForm(driver,"filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]")
    #OTHER OUTBOUND
    FillingForm(driver, "Shipment", "B2BJIT", "MRP", "filter[Mo_vista_sn][F34][select]", 
                "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", 
                "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]",
                "filter[Mo_vista_sn][F75][from]")
    CleaningForm(driver,"filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]")
    #OTHER OUTBOUND
    #total return units 
    FillingForm(driver, "Check Serial Numbers", "RET", "NAP", "filter[Mo_vista_sn][F34][select]", 
                "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", 
                "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]",
                "filter[Mo_vista_sn][F75][from]")
    CleaningForm(driver,"filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]")
    #OTHER OUTBOUND    
    FillingForm(driver, "Check Serial Numbers", "RET", "MRP", "filter[Mo_vista_sn][F34][select]", 
                "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", 
                "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]",
                "filter[Mo_vista_sn][F75][from]")
    CleaningForm(driver,"filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]")
    #OTHER OUTBOUND    
    #total deliverd units
    FillingForm(driver, "Check Serial Numbers", "PO", "NAP", "filter[Mo_vista_sn][F34][select]", 
                "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", 
                "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]",
                "filter[Mo_vista_sn][F75][from]")
    CleaningForm(driver,"filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]")
    #OTHER OUTBOUND    
    FillingForm(driver, "Check Serial Numbers", "PO", "MRP", "filter[Mo_vista_sn][F34][select]", 
                "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", 
                "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]",
                "filter[Mo_vista_sn][F75][from]")
    CleaningForm(driver,"filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]")
    

    #OTHER OUTBOUND    
    #TOTAL SAMPLE UNITS
    FillingForm(driver, "Shipment", "SAMP_E", "NAP", "filter[Mo_vista_sn][F34][select]", 
                "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", 
                "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]",
                "filter[Mo_vista_sn][F75][from]")
    CleaningForm(driver,"filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]")
    #OTHER OUTBOUND    
    FillingForm(driver, "Shipment", "SAMP_E", "MRP", "filter[Mo_vista_sn][F34][select]", 
                "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", 
                "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]",
                "filter[Mo_vista_sn][F75][from]")
    CleaningForm(driver,"filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]")
    #OTHER OUTBOUND    
    #transfers from dc4
    FillingForm(driver, "Shipment", "B2BREP", "NAP", "filter[Mo_vista_sn][F34][select]", 
                "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", 
                "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]",
                "filter[Mo_vista_sn][F75][from]")
    CleaningForm(driver,"filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]")
    #OTHER OUTBOUND    
    FillingForm(driver, "Shipment", "B2BREP", "MRP", "filter[Mo_vista_sn][F34][select]", 
                "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", 
                "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]",
                "filter[Mo_vista_sn][F75][from]")
    CleaningForm(driver,"filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]")
    #OTHER OUTBOUND
    print("all downloaded")
    
    
    """
    
    
    
    
    
    
    """

	
			   


"""
