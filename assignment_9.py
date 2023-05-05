'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    input3 = sys.argv[3]
except:
    # print("You didn't put any input when you run your code! Please add an input!")
    input1 = ""
    input2 = ""
    input3 = ""


'''
The objective of this assignment is to print the expected output.
You can find it in the instruction folder.
List of installed and authorized packages :
    - numpy
    - scikit-learn (import sklearn)
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
import numpy as np
import sklearn.linear_model as skmod

feature = [int(i) for i in input1.split(',')]
label = [i for i in input2.split(',')]
feature_predict = [int(i) for i in input3.split(',')]

feature = list(map(int, feature))
feature = np.array(feature).reshape((-1,1))

feature_predict = list(map(int, feature_predict))
feature_predict = np.array(feature_predict).reshape((-1,1))
        
model = skmod.LogisticRegression()
model = model.fit(feature, label)

predictions_proba = model.predict_proba(feature_predict)
predictions = model.predict(feature_predict)


#Use this code for your output where:
#        - feature_predict is the list of features given for prediction (=input3)
#        - predictions is the list of predictions made by your model with the feature_predict.
#        - Predictions_proba is the list a probability of each classes for each predictions (shape looks like [[0.2, 0.8], [0.5, 0.5], [0.6, 0.4]…..], it has two items per predictions, we take the maximum one).
 
for i in range(len(predictions)):
    print("For a feature egal to {}, the most probable result is {} with a probability of {:.2f}.".format(feature_predict[i][0], predictions[i], max(predictions_proba[i])))