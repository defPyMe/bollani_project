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
#import os to try and color teh terminal output
import os
from termcolor import colored

#importing trying to correct timeout error
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#os.system('color')

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
        print('''
              
              
DOCUMENTATION :

''')
        
        print(colored('''

 SSSSS  TTTTT    OOOO    CCCC   K    K      A        GGGGGG     EEEEEE   RRRR 
(         T     O    O   C      K  K       A A     G            EE       R   R
 SSSSS    T     O    O   C      KKK       AAAAA   G             EEEEE    RRR 
      )   T     O    O   C      K  K     A     A   G      GGG   EE       R   R2
 SSSSS    T      OOOO    CCCC   K    K  A       A    GGGGG      EEEEEE   R    R
                     
''', 'red')     )               
            
        print("""

            main.py : lets the user choose month and year to extract the data, collects the username and password, lets the user choose the type of launch that is headless or not
            
            accessing_DC4.py :  accesses the main page of Stockager and goes directly to the monitoring section. Added a section where the US page is accessed as it is needed for
            the last two downloads 
            
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
           
            download.py : just a small function that isolates the element to press to download teh file based off of tehe argument css_selector that is
            passed to it. in the form manipulation script we call this only when we need to download the excel file (args_[4] == 1 no download,
            args_[4] == 0 file to download) 
            
            GetFile.py : 5 different functions here. All directed to getting the file that was just downloaded (looks for it in the user's download folder). 3 functions are part of the functioning 
            of the fourth (file_name uses get_download_path, get_current_date_time, find_file_by_name). they isolate the file with the given string input
            that is the day and hour of download up until the hours. (narrows the search). The mother function file_name returns the full path of the chosen file.
           
                - removeFile : deletes the file after the processing to avoid congestion in the Downloads folder and possible errors when others are downloaded.  

            processing_downloaded_file.py : it is used only for those cases in which we download a file so in the form completion file when the args_[4] flag is equal to 
            0. Then we differentiate based of the possible names of the analyzed download, to differentiate between the cases that require
            the downloading of the file (the name is stored in the args passed to the fillingform function in args_[3]).
            In all the cases we return adictonary with the possible results that we can iterate over when writing to the file , using the key to get what we are downloading
            and the value for teh value we are looking for.
            

            FormManipulation.py : two functions, one to fill in the form online and the other to clean the form to get the info out of teh chosen
            function. both the two functions takle different arguments with teh *args function. 
                - FillingForm : called for each one of the downloads as they need different requirements. the arguments they are called with can vary in number based 
                  on the different requirements, but they are generally the same up until the flag args_[4] that tells us if the file is to be downloaded or not. 
                  there can be an added parameter where we have to download the file as we need to isolate the address of the download button
                - CleaningForm :  takes args here as well as we do not know how many of teh fields were actually filled in
            
            
            FirstSixDownloads.py : imports the datesetting to get the difference based on if we have the date or not.
            Then the filling form is called with different number of arguments. Then we clean the form calling the cleaningForm function with as arguments mainly the names of the
            elements we want to empty along with the driver
            
              
              """)  
      
        choice = input("To see program schema press 1 to launch press 2     ")
    else:

        #choosing the month we want to download , months later than teh current ok only for the previous years 
        # asking for specific input , checking if the format is respected , removing posssiblel empty pieces placed there 
        choosing_month = input("""Please select the month to be downloaded, entering the following format with numeric values --> example : August 2022  ==  08-2022        """).strip()
        months = [str(i) if len(str(i))>1 else "0"+str(i) for i in range(1,13)]
        today = datetime.now()
        years = [str(i) for i in range(1990, today.year)]
        while choosing_month[0:2] not in months and choosing_month[2:] not in years and len(choosing_month)!=7:
            choosing_month = input("""Please note that the input is invalid please mind the format that should be used, that is enter a date for mat with numeric values --> example : August 2022  ==  8-2022       """).strip()
        #as the month matches the input i can add teh timestamp 
        adding_timestamp(today, choosing_month)
        
        
        #now that i have the time horizon i can get the credentials
        username = input("insert your username    ")
        password = pwinput.pwinput("insert your password    ")
        #asking now if the program wnats to be launched headless or not 
        headless_choice = input("to run headless (hiding the website) press 1, else press 2     ")
        if headless_choice == "1":
            options = webdriver.ChromeOptions()
            #adding here
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument('disable-infobars')
            options.add_argument('--headless=new')
            options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Chrome()
        driver.get("")
        #now i can access dc4 interface, first getting the values that can be calculated on top 
        accessing_DC4('Serial Number', driver, username, password)
        #first three downloads where we have to clean the form as we have thre downloads
        #we choose the month and then the date is based off off the kind of download we are making
        Form_completion(driver, choosing_month)
            
            
            
    
interface_start()







