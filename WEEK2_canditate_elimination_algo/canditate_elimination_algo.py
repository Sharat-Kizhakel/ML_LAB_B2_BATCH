# import numpy as np
# import pandas as pd
# #reading csv
# data=pd.read_csv("enjoy_sport.csv") #trainig example 'd'
# #creating the data frame
# df=pd.DataFrame(data)
# print(df)# dataframe.iloc[row, column]   
# concepts=np.array(df.iloc[:,-1])
# print(concepts)
# targets=np.array(df.iloc[:,:-1])#now its 2d array of csv
# print(targets)
# # print(df.iloc[:,:-1])all col but last i.e target
# # print(df.iloc[:,-1]) only last col i.e concepts(yes,no)

# #first initializing general and specific hypothesis
# def learn(concepts,targets):
#     specific_hypo=targets[0]
#     print(specific_hypo)
#     general_hypo=["?" for i in specific_hypo]   
#     print(general_hypo)
#     for i in range(len(targets)):
#         #checking for positive case
#         if concepts[i]=="yes":
#             for x in range(len(specific_hypo)):
#                 if targets[i][x]!=specific_hypo[x]:
#                     specific_hypo[x]='?'
#                 # print(specific_hypo) 
#         #checking for negative case
#         if concepts[i]=="no":
#             for x in range(len(specific_hypo)):
#                 if targets[i][x]!=specific_hypo[x]:
#                    general_hypo[x]=specific_hypo[x]
#                 else:
#                     general_hypo[x]='?'
#     return specific_hypo,general_hypo              
            
   
    
# specific_hypo,general_hypo=learn(concepts,targets)
# print("Final Specific",specific_hypo)
# print("Final General",general_hypo)
from __future__ import print_function
import numpy as np
import pandas as pd
data = pd.DataFrame(data=pd.read_csv('enjoy_sport.csv'))
concepts = np.array(data.iloc[:,0:-1])
print(concepts)
target = np.array(data.iloc[:,-1])
print(target)
def learn(concepts, target):
    specific_h = concepts[0].copy()
    print("initialization of specific_h and general_h")
    print(specific_h)
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print(general_h)
    for i, h in enumerate(concepts):
        if target[i] == "yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] ='?'
                    general_h[x][x] ='?'
                print(specific_h)
        print(specific_h)
        if target[i] == "no":
            for x in range(len(specific_h)):
                if h[x]!= specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
        print(" steps of Candidate Elimination Algorithm",i+1)
        print(specific_h)
        print(general_h)  
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]    
    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])
    return specific_h, general_h
    
s_final, g_final = learn(concepts, target)
print("Final Specific_h:", s_final, sep="\n")
print("Final General_h:", g_final, sep="\n")