# User_Instruction
# What preprocess method to use
We have two preprocessing methods. For preprocessing method #1, we replace the unknown data point with the mean value of the known data of that feature. For preprocessing method #2, we replace unknown data using IterativeImputer. The default method is method 1. However, if you want to try the second method, you can change "X = X1" to "X = X2" and "y = y1" to "y = y2". 

# What classifier to use
We have 6 classifiers in the project. The default classifier is xgboost. If you would like to see the behavior of the other classifiers, you can uncomment the corresponding classifier in "name" and "classifiers" lists. 
