




import pandas as pd

df = pd.read_excel(r"C:\Users\cavazzinil\OneDrive - YOOX NET-A-PORTER GROUP\Desktop\export20230809135303.xlsx")
#GOING TO THE NEW COLUMN THAT IS LOCAT FROM 
#yellow spaces to be kept if we wnat to index correctly
x =["NOIMB" , "O27a (was sign. but used basic instead)", "O28a (was sign. but used basic instead)", "O28b (was sign. but used basic instead)" ,
                     "Outer MRP size 15", "Outer MRP size 27a", "Outer MRP size 28a", "Outer MRP size 28b"]

#isolating only the right boxes 
y = [i for i in range(4,100)]

result_GOH = sum([(df.loc[(df['Package type'] == i), 'Total Qty']).sum() for i in x])

#prepick ok 
prepick = sum([(df.loc[(df['Total Qty'] == i), 'Total Qty']).sum() for i in y])

#B2C CARTON PREPARATION
B2Ccartonpreparation = df["US"].count()


B2CcartonSignature = df.loc[(df['Box Type'] == "Signature"), 'US'].count()


B2Ccartonoversize = sum([(df.loc[(df['Package type'] == i), 'US']).count() for i in x])


B2CpickandPack = df["Total Qty"].sum()

B2CcartonManagement = B2Ccartonpreparation + B2Ccartonoversize 









#slicing the column to obtain the first three
"""
totalquantitysum_SERIALNUMBERGOH= (df.loc[(df['Locat. To Iso'] == "GOH"), 'Serial Number']).count()
totalquantitysum_SERIALNUMBERSOV= (df.loc[(df['Locat. To Iso'] == "SOV"), 'Serial Number']).count()
totalquantitysum_SERIALNUMBERSHM= (df.loc[(df['Locat. To Iso'] == "SHM"), 'Serial Number']).count()
print("totalquantitysum_SERIALNUMBERGOH", totalquantitysum_SERIALNUMBERGOH, "totalquantitysum_SERIALNUMBERSOV", totalquantitysum_SERIALNUMBERSOV,"totalquantitysum_SERIALNUMBERSHM", totalquantitysum_SERIALNUMBERSHM )
"""