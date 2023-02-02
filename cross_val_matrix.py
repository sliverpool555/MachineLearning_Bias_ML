# -*- coding: utf-8 -*-
"""
Created on Wed May  4 23:36:16 2022

@author: 253364
"""

from sklearn.linear_model import LogisticRegression

import numpy as np



def find_score(predictions, labels):
    
    conclude = zip(predictions, labels)

    score = 0
    
    correct_ans = []
    
    for i in labels:
      correct_ans.append(i)
    
    lists = zip(predictions, correct_ans)
    
    preds = []
    corrects = []
    
    score = 0
    
    for i in lists:
        if int(round(i[0])) == int(round(i[1])):
            score = score + 1
        else:
            pass
        
        var = round(i[0])
        preds.append(int(var))
        corrects.append(i[1])
      
    
    accuracy = score/len(labels)
    print("Model Accuracy", accuracy)
    


def cross_val_matrix(classifier, X_train, y_train, cv):
    
    divide = int(len(y_train)/cv)
    
    print(divide)
    
    end = divide
    start = 0
    
    validators = []
    labels = []
    
    for X in range(cv):
        validators.append((X_train[start:end]))
        labels.append(y_train[start:end])
        
        try:
            X = X_train[0:start] + X_train[end:len(X_train)]
            Y = y_train[0:start] + y_train[end:len(X_train)]
        except:
            X = np.concatenate([X_train[0:start], X_train[end:len(X_train)]])
            Y = np.concatenate([y_train[0:start], y_train[end:len(X_train)]])
        
        print(X)
        print(Y)
        
        LR = classifier.fit(X, Y) #fit all the data that is not in the test
        
        predictions = LR.predict(X_train[start:end])
        
        find_score(predictions, y_train[start:end])
        
        
        end = end + divide
        start = start + divide
        
        

    


X_train = [[8, 8] ,[9, 9], [2,2], [3,3], [4, 4], [5,5], [6,6], [7, 7] ,[0, 0], [1, 1]]
y_train = [1,1,0,0,0,1,1,1,0,0]


X_train = np.array(X_train)
y_train = np.array(y_train)


classifier = LogisticRegression(C=0.01, solver='liblinear' )

cross_val_matrix(classifier, X_train, y_train, 5)


    






    