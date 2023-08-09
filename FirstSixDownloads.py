
from Date_setting import DateSetting
from FormManipulation import FillingForm, CleaningForm


#thuis needs to go back every time to the previous screen 
def Form_completion(driver, choosing_month, input_month):
    #all the different downloads 
    #the parameters here are already for the SERIAL NUMBER  view, the parameters are ok for the monitoring serial number
    # there are three because one appears later after the between is pressed. 1 (hours) , 0 no hours in date setting 
    DateSetting(driver,  "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", input_month, 1)
    #BOOKING IN 
    # should keep thing sin order here having the elements names and teh values to be inserted there 
    #first i get the elements then i insert the values
    #AS I HAVE ADDED A FILTER THEN I CAN ADD EVERYTHING TO TEH SINGLE LIST  
    
    
    #[2] --> advanced filtering, [4] --> 0 on the same page, 1 to download.
    #[5] -- it is  teh css selector to download teh different documents 
    
    
    
    
    
    
    FillingForm(driver, {"filter[Mo_vista_sn][F34][select]" : 'Equal to',  "filter[Mo_vista_sn][F34][from]": "Putaway" , 
                         "filter[Mo_vista_sn][F21][select]" : 'Equal to', "filter[Mo_vista_sn][F21][from]":'PO'}, 0, "BOOKING IN", 0, 'a[href*="Mo_vista_sn"][href*="export=xls/exportEnt=Mo_vista_sn"]')
    
    #cleaning the form , has kwargs here as well as there are differences to be considered
    CleaningForm(driver, ["filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", 
                          "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]"])
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
    
    
    
    
    #RETURNS (sum on top, as before but with RET)
    #date is to be set with the full hpours setting
    DateSetting(driver,  "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", input_month, 1)
    FillingForm(driver, {"filter[Mo_vista_sn][F34][select]" : 'Equal to',  "filter[Mo_vista_sn][F34][from]": 'Putaway', 
                         "filter[Mo_vista_sn][F21][select]" : 'Equal to', "filter[Mo_vista_sn][F21][from]":'RET'}, 0, "RETURNS", 0)
    
    #cleaning the form , has kwargs here as well as there are differences to be considered
    CleaningForm(driver, ["filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", 
                          "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]"])
    
    
    #PICK SAMPLE INT 
    DateSetting(driver,  "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", input_month, 1)
    FillingForm(driver, {"filter[Mo_vista_sn][F34][select]" : 'Equal to',  "filter[Mo_vista_sn][F34][from]": 'Picking', 
                         "filter[Mo_vista_sn][F21][select]" : 'Equal to', "filter[Mo_vista_sn][F21][from]":'SAMP_I', "filter[Mo_vista_sn][F75][select]" : "Select"}, 0, "PICK SAMPLE INT", 0)
    
    #cleaning the form , has kwargs here as well as there are differences to be considered
    CleaningForm(driver, ["filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", 
                          "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]"])
    
    
    
  
   
   
   
   
   
   
   
   
   
   
    
    
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