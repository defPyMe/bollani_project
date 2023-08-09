import pandas as pd

def processing_file(filename, processing_flag):
#the processing flag is the name of the type of data we are looking for --> args_[3]
#regardless of the imported file it needs to be written
    df = pd.read_excel(filename)
    if processing_flag == "MANUAL PUTAWAY":
    #slicing the column to obtain the first three
        df['Locat. To Iso'] = df['Locat. To'].str.slice(stop=3)
        totalquantitysum_SERIALNUMBERGOH = (df.loc[(df['Locat. To Iso'] == "GOH"), 'Serial Number']).count()
        totalquantitysum_SERIALNUMBERSOVSHM = ((df.loc[(df['Locat. To Iso'] == "SOV"), 'Serial Number']).count()) + ((df.loc[(df['Locat. To Iso'] == "SHM"), 'Serial Number']).count())
        result = (totalquantitysum_SERIALNUMBERGOH, totalquantitysum_SERIALNUMBERSOVSHM)  
    elif processing_flag == "PICKING":
        df['Locat. To Iso'] = df['Locat. From'].str.slice(stop=3)
        x = [ "B2BJIT", "B2BREP", "B2C", "BULK", "EXTREP", "FAULTY", "JVJIT", "RECODE", "RESHIP", "RTV", "SAMP_E", "SAMP_I"]
        #EXTRACTING ALL values for each line 
        #GOH
        result_GOH = [(df.loc[(df['Locat. To Iso'] == "GOH") & (df['Flow'] == i), 'Serial Number']).count() for i in x]
        #SFA
        result_SFA = [(df.loc[(df['Locat. To Iso'] == "SFA") & (df['Flow'] == i), 'Serial Number']).count() for i in x]
        #SHM
        result_SHM = [(df.loc[(df['Locat. To Iso'] == "SHM") & (df['Flow'] == i), 'Serial Number']).count() for i in x]
        #SHV 
        result_SHV = [(df.loc[(df['Locat. To Iso'] == "SHV") & (df['Flow'] == i), 'Serial Number']).count() for i in x]
        #SOV
        result_SOV = [(df.loc[(df['Locat. To Iso'] == "SOV") & (df['Flow'] == i), 'Serial Number']).count() for i in x]
        #performing the actual calculations
        print(result_GOH, result_GOH[1])
        total_GOH_minus_B2BREP = sum(result_GOH) - result_GOH[1]
        total_GOH_B2BREPL = result_GOH[1]
        pick_HZ = sum(result_SHM)
        pick_OVS = sum(result_SOV)
    elif processing_flag == "PRE PICK":
        
        

        x =["NOIMB" , "O27a (was sign. but used basic instead)", "O28a (was sign. but used basic instead)", "O28b (was sign. but used basic instead)" ,
                     "Outer MRP size 15", "Outer MRP size 27a", "Outer MRP size 28a", "Outer MRP size 28b"]

        #isolating only the right boxes 
        y = [i for i in range(4,100)]

        #B2C pick&pack OS
        result_GOH = sum([(df.loc[(df['Package type'] == i), 'Total Qty']).sum() for i in x])

        #Pre-pick
        prepick = sum([(df.loc[(df['Total Qty'] == i), 'Total Qty']).sum() for i in y])

        #B2C carton preparation (basic)
        B2Ccartonpreparation = df["US"].count()

        #B2C carton preparation (signature)
        B2CcartonSignature = df.loc[(df['Box Type'] == "Signature"), 'US'].count()

        #B2C carton preparation (oversize)
        B2Ccartonoversize = sum([(df.loc[(df['Package type'] == i), 'US']).count() for i in x])

        #B2C pick&pack
        B2CpickandPack = df["Total Qty"].sum()
        
        #B2C cartons management
        B2CcartonManagement = B2Ccartonpreparation + B2Ccartonoversize 


    elif processing_flag == "PRE PICK":
        #B2B JIT+Repl
        result = sum([(df.loc[(df['Flow'] == "B2B JIT") | (df['Flow'] == "B2B REPL"), 'Total Qty']).sum()])
        #B2B cartons management
        result1 = sum([(df.loc[(df['Flow'] == "B2B JIT") | (df['Flow'] == "B2B REPL"), 'US']).count()])
        #Pick&pack RTV
        result2 = (df.loc[(df['Flow'] == "RTV"), "Total Qty"]).sum()
        #Pick&pack Sample ext
        result3 = (df.loc[(df['Flow'] == "SAMPLE ESTERNO"), "Total Qty"]).sum()

        
    
    
    