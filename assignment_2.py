
'''
The objective of this assignment is to print the dataframe showed in the instruction.
Only one test will be done.
You can write you code after this comment :
'''
#Your code here:
import pandas as pd
dictio = {'Name' : ['Brad', 'Angelina', 'Tom'], 'Surname' : ['Pitt', 'Jolie', 'Cruise'], 'Age' : [58, 47, 60]}
dataframe = pd.DataFrame(dictio)
print(dataframe)