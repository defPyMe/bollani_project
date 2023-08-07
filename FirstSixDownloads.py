
from Date_setting import DateSetting
from FormManipulation import FillingForm, CleaningForm


#thuis needs to go back every time to the previous screen 
def Form_completion(driver, choosing_month, input_month):
    #all the different downloads 
    #setting the date only the first time 
    DateSetting(driver,  "filter[Mo_vista_sn][F31][select]", "filter[Mo_vista_sn][F31][from]", "filter[Mo_vista_sn][F31][to]", input_month, 0)
    #ITEM COUNT + TAG AND SORT - date has already been set in the previous module
    FillingForm(driver, "Shipment", "B2C", "NAP", "filter[Mo_vista_sn][F34][select]", 
                "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", 
                "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]",
                "filter[Mo_vista_sn][F75][from]")
    #need to clean the date as well in case we need to add the hour 
    
    
    
    
    CleaningForm(driver,"filter[Mo_vista_sn][F34][select]", "filter[Mo_vista_sn][F34][from]", "filter[Mo_vista_sn][F21][select]", "filter[Mo_vista_sn][F21][from]", "filter[Mo_vista_sn][F75][select]", "filter[Mo_vista_sn][F75][from]")
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