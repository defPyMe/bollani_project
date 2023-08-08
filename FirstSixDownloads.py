
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
    FillingForm(connection = driver, movement_type = "filter[Mo_vista_sn][F34][select]", movement_type_options = "filter[Mo_vista_sn][F34][from]", 
                flow_type =  "filter[Mo_vista_sn][F21][select]", flow_type_options =  "filter[Mo_vista_sn][F21][from]", movement_type_value = "Putaway", flow_value = "PO")
    #cleaning the form , has kwargs here as well as there are differences to be considered
    CleaningForm(connection = driver, movement_type ="filter[Mo_vista_sn][F34][select]", movement_type_options = "filter[Mo_vista_sn][F34][from]", flow_type =  "filter[Mo_vista_sn][F21][select]",
                 flow_type_options = "filter[Mo_vista_sn][F21][from]")
    
    
    
    
    
    
    
    
    
    
    
    
    
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