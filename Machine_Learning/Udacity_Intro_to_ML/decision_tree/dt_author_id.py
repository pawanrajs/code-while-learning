#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




###################################################################
### Get Decision Tree Classifier up with min_samples_split=40.  ###

from sklearn.tree import DecisionTreeClassifier
clf1 = DecisionTreeClassifier(min_samples_split=40)

t0 = time()
clf1.fit(features_train, labels_train)

## 136.88 seconds with percentile=10 (3785 features)
## 10.124 seconds with percentile=1 (379 features)
print("Training Time for Decision Tree Classifier with min_samples_split=40: ", \
    round(time()-t0, 3), "s")

###   Find the accuracy (Percentile=10): 0.9778156996587031     ###
###   Find the accuracy (Percentile=1): 0.9664391353811149      ###
clf1_accuracy = clf1.score(features_test, labels_test)
print("Accuracy of clf1 with min_samples_split=40 is {}".format(clf1_accuracy))
##################################################################

########### What's the number of features in your data? ###########
### 3785 features with percentile=10, 379 features with percentile=1
print(features_train.shape[1])