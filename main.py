from selenium import webdriver
#finding the file by name
#importing module to hide teh password 
import pwinput
#importing datetime to calculate current month 
from datetime import datetime
#required mport to calculate last month 
import dateutil.relativedelta





#calculating current date for the timestamp
today = datetime.now()
current_month = today.strftime("%B")
#calculating previous month date 
last_month = today + dateutil.relativedelta.relativedelta(months=-1)
previous_month = last_month.strftime("%B")


#removed the driver in the script and put it inside the function 



def interface_start():
    choice = input("To see program schema press 1 to launch press 2      ")
    while choice == "1":
        #choosing to launch the documentation
        print("""

            \   __________    /         NOTHING HERE
             \  | O   0   |  /          BUT DESOLATION!!
              \ |   ()    | /
               \|         |/
              
              """)  
      
        choice = input("To see program schema press 1 to launch press 2     ")
    
    
    
    
    
    else:
        #choosing the month we want to download , months later than teh current ok only for the previous years 
        # asking for specific input , checking if the format is respected , removing posssiblel empty pieces placed there 
        choosing_month = input("""Please select the month to be downloaded, entering the following format with numeric values --> example : August 2022  ==  08-2022        """).strip()
        months = [str(i) if len(str(i))>1 else "0"+str(i) for i in range(1,13) ]
        years = [str(i) for i in range(1990, today.year)]
        while choosing_month[0:2] not in months and choosing_month[2:] not in years:
            choosing_month = input("""Please note that the input is invalid please mind the format that should be used, that is enter a date format with numeric values --> example : August 2022  ==  8-2022       """).strip()
        print("input ok")
            
            
            
    
interface_start()







