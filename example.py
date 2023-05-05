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
scaler_standard = skprepro.StandardScaler()
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
# Open the dataframe (Ex_2_price_to_plot_v1.parquet) with the read_parquet() function of the pandas package.
# If you upload your code to codepost use the the following path in the read_parquet() function : "Ex_2_price_to_plot_v1.parquet".
# Display 1 scatter (dots only) plot. Only datas between the 2010-09-27 00:00:00 and the 2012-03-27 00:00:00 must be plotted.
# The graph x axis is the "Close" column of the dataframe and the y axis is the "Open" column of the dataframe.
# Its y limits are 17.9 and 46.7.
# You can find the required plot in the file Ex_2_plot_V1.png

    f = pd.read_parquet('ICT\Ex_2_price_to_plot_v1.parquet')
    x1 = f['Date'].to_numpy().reshape(-1,1)
    open = f['Open'].to_numpy().reshape(-1,1)
    close = f['Close'].to_numpy().reshape(-1,1)

    x = np.array(open).reshape(-1,1)
    y = np.array(close).reshape(-1,1)
    poly2 = skprepro.PowerTransformer(4, include_bias = False)
    model = skmod.LinearRegression().fit(poly2.fit_transform(x), y)
    plt.plot(np.arange(17.9, 46.7), model.predict(poly2.fit_transform(np.arange(17.9, 46.7).reshape(-1,1))) )









    plt.show()
# ----------------------End of EXERCISE 2 --------------------------------------


elif input1 == '5':
# ----------------------EXERCISE 5 - Machine Learning III--------------------------------------
# Instructions:
# You have two features : feature1 and feature2. You objective is to make a two columns matrix and to standardized
# them by using the standardization equation or the standard Scaler of the scikit-learn package.
# You can find the desired matrix in the document Ex_5_standard_matrix_V1.txt

    feature1 = [-433, 19, 177, 460, -290, -445, 123, -403, -746, 248, -555, 319, -452, -714, 489, 62, -183, 46, -669, -97, -978, 256, -523, -873, -921, 495, -723, 1, -115, 246]
    feature2 = [2, -4, -4, -1, -8, -9, -2, -9, -5, -3, 3, 4, -6, 2, -7, -3, -4, -10, 1, -5, -5, 4, 0, -1, -10, -7, -6, -3, 4, 3]
    feature1 = np.array(feature1)
    feature2 = np.array(feature2)
    feature1 = feature1.reshape(-1,1)
    feature2 = feature2.reshape(-1,1)
    data_x = np.hstack([feature1, feature2])
    data_x_stan = scaler_standard.fit_transform(data_x)
    print(data_x_stan)








# Here is the print instructions to print the standardized matrix rounded.
	print(np.around(x_standard, 3))

# ----------------------End of EXERCISE 5 --------------------------------------