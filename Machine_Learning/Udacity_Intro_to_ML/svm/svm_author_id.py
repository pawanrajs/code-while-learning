#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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


#########################################################
from sklearn.svm import SVC
clf = SVC(kernel='linear')
clf.fit(features_train, labels_train)

from sklearn.metrics import accuracy_score
acc = accuracy_score(clf.predict(features_test), labels_test)
print("Accuracy using Linear SVM is {}".format(acc))
#########################################################
# Accuracy using SVM is 0.9840728100113766
#########################################################
'''
You'll be Provided similar code in the Quiz
But the Code provided in Quiz has an Indexing issue
The Code Below solves that issue, So use this one
'''

# gamma='auto' matches answers with udacity course. 
# gamma='auto' was the default but isn't any more apparently.
clf3 = SVC(kernel='rbf', C=10000, gamma='auto')
clf3.fit(features_train, labels_train)
print("Accuracy on RBF, C=10000 with full dataset is {}".format(
    clf3.score(features_test, labels_test)))
#########################################################
# Accuracy on RBF, C=10000 with full dataset is 0.9908987485779295
#########################################################

features_train_small = features_train[:int(len(features_train)/100)]
labels_train_small = labels_train[:int(len(labels_train)/100)]
clf = SVC(kernel='linear')
clf.fit(features_train_small, labels_train_small)

acc = accuracy_score(clf.predict(features_test), labels_test)
print("Accuracy using SVM and Reduced Data Set is {}".format(acc))


for c in [1, 10, 100, 1000, 10000]:
    clf2 = SVC(kernel='rbf', C=c, gamma='auto')
    clf2.fit(features_train_small, labels_train_small)
    acc2 = clf2.score(features_test, labels_test)
    print("Accuracy using RBF SVM, C={}, Reduced Data Set is {}".format(c, acc2))

##################################################################
# Accuracy using SVM and Reduced Data Set is 0.8845278725824801
# Accuracy using RBF SVM, C=1, Reduced Data Set is 0.6160409556313993
# Accuracy using RBF SVM, C=10, Reduced Data Set is 0.6160409556313993
# Accuracy using RBF SVM, C=100, Reduced Data Set is 0.6160409556313993
# Accuracy using RBF SVM, C=1000, Reduced Data Set is 0.8213879408418657
# Accuracy using RBF SVM, C=10000, Reduced Data Set is 0.8924914675767918
##################################################################
