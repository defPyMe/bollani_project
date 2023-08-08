
from datetime import datetime
import calendar
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import dateutil.relativedelta


#keeping just one flag to add the hour or not
#the type, first_date, second_date are the input fields on teh page, flag is the type of date (only date) or hours also
def DateSetting(driver, type_name, first_date_name, second_date_name, input_month, flag):
    #if flag month == 1 then we are avoiding putting the hour inside
    #getting a general date from the input month that has only the date (no hours)
    date_obj = datetime.strptime(input_month, "%m-%Y")
    #getting the number of days in the selected month
    days_count = calendar.monthrange(date_obj.year, date_obj.month)[1]
    
    if flag == 1:
        #case in which we want the complete date
        #adding the two cases with the start and end of the date , the output has to be returned as string 
        #first day ok with time and date 
        first_day = date_obj.replace(day=1, hour=0, minute=0, second=0, microsecond=0).strftime("%d-%m-%Y %H:%M:%S")
        last_day =  date_obj.replace(day=days_count, hour=23, minute=59, second=59, microsecond=59).strftime("%d-%m-%Y %H:%M:%S")
        #extracting the date as date only 
    else:
        first_day = date_obj.strftime("%d-%m-%Y")
        last_day = date_obj.replace(day=days_count).strftime("%d-%m-%Y")
        pass

    
    
    #isolating data movimento
    DataMovimento = driver.find_element(By.NAME, type_name)
    select = Select(DataMovimento)
    # Select an option by its visible text
    select.select_by_visible_text('Between')
    #two calendars
    calendar_movimento_firstdate = driver.find_element(By.NAME, first_date_name )
    calendar_movimento_lasttdate = driver.find_element(By.NAME, second_date_name )
    #adding the date values we created above
    calendar_movimento_firstdate.send_keys(first_day)
    calendar_movimento_lasttdate.send_keys(last_day)
    