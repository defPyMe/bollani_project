from selenium.webdriver.common.by import By
import time
import os
from datetime import datetime

download = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')


#isolating the values in the previous function and then writing to the file 
def isolating_and_writing(driver, name_attribute):
    try:
        body = driver.find_element(By.XPATH, "/html/body").text
        body_as_list = body.split()
        record = [body_as_list[i+1] for i in range(len(body_as_list)) if "Record:" in body_as_list[i]]
        
        # writing just one values and the name of the value that is isolated 
        
        with open (download + "\\output.txt","a", encoding="utf-8") as f:
            f.write( name_attribute,   record[0] )
            f.write("\n")
        
        # Line that goes back to the form to be filled in - maybe it shouldn t stay here but ok
        image = driver.find_element(By.XPATH, "//td[@class='title']/img")
        image.click()
        print(f"writing to file - {name_attribute} - written correctly")
        time.sleep(3)
    except:
        print("writing to file")
        with open (download + "\\output.txt","a", encoding="utf-8") as f:
            f.write(name_attribute + "   " + "Record not found" )
            f.write("\n")
       
        print(f"writing to file - values not written - Error encountered")
        
    return None


#writes the processed file 
def writing_processed_values(result_dict):
    try:
        with open (download + "\\output.txt","a", encoding="utf-8") as f:
            for i in result_dict:
                f.write( str(i) + "    " + str(result_dict[i])) 
                f.write("\n")
  
        print("Processed values added correctly")
    except:
        with open (download + "\\output.txt","a", encoding="utf-8") as f:
            for i in result_dict:
                f.write( str(i) + "    " + "Error finding value") 
                f.write("\n")
      
        print("Processed values added correctly")


#adding here the current date and the selected month to teh output file (top of it )
def adding_timestamp(current_date, chosen_month):
    try:
        #as the format is a string i should isolate the values from the input string
        date_obj = datetime.strptime(chosen_month, "%m-%Y")
        #merely opening the file and appending teh urrent date and teh selected month that is calculated in main.py 
        with open (download + "\\output.txt","a", encoding="utf-8") as f:
            f.write("\n")
            f.write("Extracting data on " + str(current_date) + " , for " + str(date_obj) )
            f.write("\n")
        print("Added timestamp")
    except:
        print("invalied date inserted, timestamp not added ")
    pass

