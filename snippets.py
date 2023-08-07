
    
    
        if choosing_month == "1":
            flag_month = 1
            #accessing the week method
            week_choice = input("Insert the week number here (1-52)  ")
            while week_choice not in [str(i) for i in range(1,53)]:
                #adding time stamp, can i use the current montha s a weeksince it is a string anyways 
                print("Invalid week number, try again inserting a week that is in the interval 1-52")
                week_choice =input("Insert the week number here (1-52)  ")
            adding_timestamp_week(today, week_choice)
            print("Extracting data of week" + week_choice)
            #passing here the week number as an argument 
            pass
        else:
            month_choice = input("To extract data of the current month press 1, to extract previous month data press 2    ")
            if month_choice=="1":
                flag_month = 2
                #adding time stamp  
                adding_timestamp(today, current_month)
                print("Extracting data of " + current_month)
            else:
                flag_month = 3
                #calculating last month and extracting name 
                # adding the timestamp
                adding_timestamp(today, previous_month)
                print("Extracting data of " + previous_month)
            #setting default week choice
            week_choice=0
        #adding a blank line
        print("\n")
        
        
    #adding  an header to the batch file to describe the project
        print("""Small project to automatize Stockager. the program will access the
    main interface through Selenium and will perform the following downloads in order 
    1) Outbound Units B2C
    2) Other Outbound Units (only JIT) 
    3) Return Units
    4) Delivered Units
    5) Sample Units
    6) Transfer From DC4  (Replenishment Only)

    the script then downloads and processes the excel file to calculate the following metrics

    7) Total Out Orders (NAP / MRP) 
    8) Premier Order 
    9) Premier Units

    all the results are saved in a txt file called output.txt in the user's Downloads folder
            """)
        print("\n")
        #adding the choice to see ho the program works 
        
   
        
        username = input("insert your username    ")
        password = pwinput.pwinput("insert your password    ")
        
        headless_choice = input("to run headless (hiding the website) press 1, else press 2     ")
        if headless_choice == "1":
            
            options = webdriver.ChromeOptions()
            options.add_argument('--headless=new')
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Chrome()
        driver.get("https://stockager-dc4.warehouse.ynap.biz/")
        
        accessing_DC4('Serial Number', driver, username, password)
        #output.insert(END, "accessing_DC4")#.insert(END,"\n"+txt)
        
        #adding here the flag for the data of teh selected month 
        Form_completion(driver, flag_month, week_choice)
        #output.insert(END, "completed  the form")
        DownloadingFileUS(driver, flag_month, week_choice)
        file_to_process_ = file_name()
        result = processing(file_to_process_)
        writing_processed_values(result)
        exit_program = input("Program finished runnig, press any key + enter to exit ...")
        while exit_program == "":
            pass









#the others are filled in with the form created





interface_start()

#should add the __name__=="main"