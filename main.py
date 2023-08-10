from selenium import webdriver
#finding the file by name
#importing module to hide teh password 
import pwinput
#importing datetime to calculate current month 
from datetime import datetime
#required mport to calculate last month 
import dateutil.relativedelta
#importing the accessing function
from Accessing import accessing_DC4
#importing the form completion function
from FirstSixDownloads import Form_completion
#importing timestamp function
from isolating_writing import adding_timestamp


#NBOT SURE THIS HERE MAKES SENSE



#calculating current date for the timestamp
#today = datetime.now()
#current_month = today.strftime("%B")
#calculating previous month date 
#last_month = today + dateutil.relativedelta.relativedelta(months=-1)
#previous_month = last_month.strftime("%B")


#removed the driver in the script and put it inside the function 



def interface_start():
    choice = input("To see program schema press 1 to launch press 2      ")
    while choice == "1":
        #choosing to launch the documentation
        print("""

            main.py : lets the user choose month and year to extract the data, collects the username and password, lets the user choose the type of launch that is headless or not
            
            accessing_DC4.py :  accesses the main page of Stockager and goes directly to the monitoring section
            
            DateSetting.py : sets the date for the field of the movement date. Takes different arguments and finally sends the date values to the intended fields
            
                - driver 
                - name of the : choosing interval, first date field, second date field in the page monitoring
                - input_month in the format inserted by the user ex : "08-2023" and turns it into a date
                - flag that sets if teh inserted date wioll have the hour inserted or just the date (1 hours, 0 date-only)
            
            isolating_writing.py :  it has three main functions here 

                - adding_timestamp : takes the current_date and chosen_month as argumnets. The current_date is used for
                  getting the date of the extraction. The chosen month gets us teh detail of the period the extraction refers to.
                  it has the same line of code in datesetting that processes the input to get the date
                - isolating_and_writing : isolates the value in the page when we are looking for the small value on top
                  near the Record string. isolates the record witha  list comprehension and then brings back to tehe form to be filled in
                - writing_processed_values : writes the values that are returned by the dicts after the file has been processed
                
            countdown.py : small script with just one function that takes an integer as argument and prints a small conter in
            either in the terminal if launched from the editor or inside the console when packed into an application. useful to get an idea of when the script will be finished 
            running
           
            
           
           
           
           
           
           
           
           
            FormManipulation.py : 
            
            FirstSixDownloads.py : imports three 
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
              
              
              
            
              
              
              
              
            
              
              """)  
      
        choice = input("To see program schema press 1 to launch press 2     ")
    else:

        #choosing the month we want to download , months later than teh current ok only for the previous years 
        # asking for specific input , checking if the format is respected , removing posssiblel empty pieces placed there 
        choosing_month = input("""Please select the month to be downloaded, entering the following format with numeric values --> example : August 2022  ==  08-2022        """).strip()
        months = [str(i) if len(str(i))>1 else "0"+str(i) for i in range(1,13) ]
        today = datetime.now()
        years = [str(i) for i in range(1990, today.year)]
        while choosing_month[0:2] not in months and choosing_month[2:] not in years:
            choosing_month = input("""Please note that the input is invalid please mind the format that should be used, that is enter a date format with numeric values --> example : August 2022  ==  8-2022       """).strip()
        #as the month matches the input i can add teh timestamp 
        adding_timestamp(today, choosing_month)
        
        
        #now that i have the time horizon i can get the credentials
        username = input("insert your username    ")
        password = pwinput.pwinput("insert your password    ")
        #asking now if the program wnats to be launched headless or not 
        headless_choice = input("to run headless (hiding the website) press 1, else press 2     ")
        if headless_choice == "1":
            
            options = webdriver.ChromeOptions()
            options.add_argument('--headless=new')
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Chrome()
        driver.get("https://stockager-dc4.warehouse.ynap.biz/")
        #now i can access dc4 interface, first getting the values that can be calculated on top 
        accessing_DC4('Serial Number', driver, username, password)
        #first three downloads where we have to clean the form as we have thre downloads
        #we choose the month and then the date is based off off the kind of download we are making
        Form_completion(driver, choosing_month, choosing_month)
            
            
            
    
interface_start()







