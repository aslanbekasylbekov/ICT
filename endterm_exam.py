'''
-------------------------ENDTERM EXAM-----------------
DO NOT DELETE THE FOLLOWING CODE
'''
import sklearn.linear_model as skmod
import sklearn.preprocessing as skprepro
import numpy as np
import matplotlib.pyplot as plt
import sklearn.model_selection
import pandas as pd
import sklearn.preprocessing as skprepro

import sys

try:
    input1 = sys.argv[1]
except:
    pass
'''
In the following file, do not delete anything (comments, code, ...). Just add you code in every part (one per exercise).
Use my variable for input (if there is any), use my printing for output (if there is any).
You can upload your code to codepost.io to check the tests. A sucess in one test doesn't always mean than your exercise is correct,
a fail doesn't always mean that your exercise is wrong. I will check all codes.
At the end of exam, you should upload the last version of your code to codepost.io or to the online folder on Teams.
The only authorized packages are:
- pandas
- pyarrow
- fastparquet
- numpy
- sklearn
- matplotlib
- datetime

'''

if input1 == '2':
# ----------------------EXERCISE 2 - Data plotting--------------------------------------
# Instructions:
# Open the dataframe (Ex_2_price_to_plot_v2.parquet) with the read_parquet() function of the pandas package.
# If you upload your code to codepost use the the following path in the read_parquet() function : "Ex_2_price_to_plot_v2.parquet".
# Display 1 scatter (dots only) plot. Only datas between the 2009-08-18 00:00:00 and the 2020-08-06 00:00:00 must be plotted.
# The graph x axis is the "Low" column of the dataframe and the y axis is the "Close" column of the dataframe.
# Its x limits are 13.6 and 83.5.
# You can find the required plot in the file Ex_2_plot_V2.png

    df = pd.read_parquet("Ex_2_price_to_plot_v2.parquet")
    x1 = df['Date'].to_numpy().reshape(-1,1)
    open = df['Open'].to_numpy().reshape(-1,1)
    low = df['Low'].to_numpy().reshape(-1,1)

    x = np.array(open).reshape(-1,1)
    y = np.array(low).reshape(-1,1)
    poly2 = skprepro.PolynomialFeatures(4, include_bias = False)
    model = skmod.LinearRegression().fit(poly2.fit_transform(y), x)
    plt.plot(np.arange(13.6, 83.5), model.predict(poly2.fit_transform(np.arange(13.6, 83.5).reshape(-1,1))))






    plt.show()
# ----------------------End of EXERCISE 2 --------------------------------------

elif input1 == '3':
# ----------------------EXERCISE 3 - Machine Learning I--------------------------------------
# Instructions:
# - Transform all the three given lists into numpy arrays.
# - Transform the L1 array into a matrix (called L5) with 9 lines and 3 columns.
# - Print the obtained matrix (L5). You can find a example of the desired matrix in the document Ex_3_array_new_shape_V2.txt
# - Reshape the arrays L2 and L3 into 1 columns arrays and create a 2 columns matrix (called L6) where the first column is the L2 array and the second the L3 array.
# - Print the obtained matrix (L6). You can find a example of the desired matrix in the document Ex_3_array_matrix_V2.txt
# - Do the multiplication of L3 by 5 and call it L7.
# - Print the obtained array (L7). You can find a example of the desired matrix in the document Ex_3_array_operation_V2.txt

	L1 = [51, 16, 56, 10, 31, 1, 1, 55, 6, 27, 30, 36, 9, 17, 30, 48, 47, 5, 31, 12, 18, 47, 25, 6, 29, 48, 44]
	L2 = [44, 31, 3, 8, 52, 20, 51, 26, 53, 38, 16, 23, 53, 49, 26, 23, 23, 16, 35, 2, 14, 7, 6, 25, 38, 21, 26]
	L3 = [42, 6, 31, 30, 9, 58, 50, 51, 37, 36, 6, 57, 43, 9, 49, 13, 20, 41, 36, 35, 31, 38, 35, 46, 15, 53, 52]

L1 = np.array(L1)
L2 = np.array(L1)
L3 = np.array(L1)

L5 = L1.reshape((9,3))
print(L5)
L6 = L2.reshape(L1.shape)
print(L6)
L7 = []
for i in L6.iterows():
    L7.append(i)

 
print(L7)
    
    







# Here are the print function for each matrix:
    # print(L5)
    # print(L6)
    # print(L7)

# ----------------------End of EXERCISE 3 --------------------------------------