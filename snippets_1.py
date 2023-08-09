




import pandas as pd

df = pd.read_excel(r"C:\Users\cavazzinil\Downloads\export20230809113645.xlsx")
#GOING TO THE NEW COLUMN THAT IS LOCAT FROM 
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
pick_OVS = sum((result_SOV)


print(total_GOH_minus_B2BREP)
#slicing the column to obtain the first three
"""
totalquantitysum_SERIALNUMBERGOH= (df.loc[(df['Locat. To Iso'] == "GOH"), 'Serial Number']).count()
totalquantitysum_SERIALNUMBERSOV= (df.loc[(df['Locat. To Iso'] == "SOV"), 'Serial Number']).count()
totalquantitysum_SERIALNUMBERSHM= (df.loc[(df['Locat. To Iso'] == "SHM"), 'Serial Number']).count()
print("totalquantitysum_SERIALNUMBERGOH", totalquantitysum_SERIALNUMBERGOH, "totalquantitysum_SERIALNUMBERSOV", totalquantitysum_SERIALNUMBERSOV,"totalquantitysum_SERIALNUMBERSHM", totalquantitysum_SERIALNUMBERSHM )
"""