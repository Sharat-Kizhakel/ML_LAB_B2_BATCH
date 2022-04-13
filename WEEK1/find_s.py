import pandas as pd
import numpy as np
meta_data=pd.read_csv("C:/Users/BMSCE/Downloads/Find_S.csv")
print(meta_data)
hypo=['NULL'for i in range((len(meta_data.columns)-1))]
print(hypo)
rest_of_attributes=np.array(meta_data)[:,:-1]
# print(rest_of_attributes)
# positive=np.array(meta_data)[:,-1]
print("Positive-negative:")
test=np.array(meta_data)[:]
# print(test)
for id,row in enumerate(test):
    if row[-1]=="Yes":
        print(row)
        for i in range(len(row)-1):
            if hypo[i]=='NULL':
                hypo[i]=row[i]
            elif hypo[i]!=row[i]:
                hypo[i]='?'
print(hypo)    
    # print(row,id)
