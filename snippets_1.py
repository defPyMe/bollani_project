




import pandas as pd

df = pd.read_excel(r"C:\Users\cavazzinil\OneDrive - YOOX NET-A-PORTER GROUP\Desktop\export20230809170038.xlsx")
#GOING TO THE NEW COLUMN THAT IS LOCAT FROM 
#yellow spaces to be kept if we wnat to index correctly

#B2B JIT+Repl
result = sum([(df.loc[(df['Flow'] == "B2B JIT") | (df['Flow'] == "B2B REPL"), 'Total Qty']).sum()])
#B2B cartons management
result1 = sum([(df.loc[(df['Flow'] == "B2B JIT") | (df['Flow'] == "B2B REPL"), 'US']).count()])
#Pick&pack RTV
result2 = (df.loc[(df['Flow'] == "RTV"), "Total Qty"]).sum()
#Pick&pack Sample ext
result3 = (df.loc[(df['Flow'] == "SAMPLE ESTERNO"), "Total Qty"]).sum()


print(result3)
#slicing the column to obtain the first three
"""
totalquantitysum_SERIALNUMBERGOH= (df.loc[(df['Locat. To Iso'] == "GOH"), 'Serial Number']).count()
totalquantitysum_SERIALNUMBERSOV= (df.loc[(df['Locat. To Iso'] == "SOV"), 'Serial Number']).count()
totalquantitysum_SERIALNUMBERSHM= (df.loc[(df['Locat. To Iso'] == "SHM"), 'Serial Number']).count()
print("totalquantitysum_SERIALNUMBERGOH", totalquantitysum_SERIALNUMBERGOH, "totalquantitysum_SERIALNUMBERSOV", totalquantitysum_SERIALNUMBERSOV,"totalquantitysum_SERIALNUMBERSHM", totalquantitysum_SERIALNUMBERSHM )
"""