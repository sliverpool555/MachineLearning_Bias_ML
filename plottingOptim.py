# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:04:23 2022

@author: 253364
"""


#This is where the accuracy and the C need to be plotted to show how C effects accuracy for both normal and then fairness


import pandas as pd
import os
import matplotlib.pyplot as plt



def plot_optim(file):
    df = pd.read_csv(file)
    print(df.head)
    
    
    accuracy = df['Accuracy']
    
    newton = list(accuracy[:9])
    
    lbfgs = list(accuracy[9:18])
    
    liblinear = list(accuracy[18:])
    
    elements = ['lbfgs', 'liblinear', 'newton']
    
    labels = df['C']
    labels = labels[:9]
    
    fig, ax = plt.subplots()
    
    plt.title("Logistic Regression C value to Accuracy")
    plt.plot(liblinear)
    plt.plot(newton)
    plt.plot(lbfgs)
    plt.legend(elements)
    plt.xlabel('C Value')
    plt.ylabel('Average Cross Validation Accuracy')
    ax.set_xticklabels(labels)
    plt.show()
    
    
    
def smart_plot(file):
    df = pd.read_csv(file)
    print(df.head)
    
    heads = df.head()
    
    for h in heads:
    
        accuracy = df[h]
        
        newton = list(accuracy[:9])
        
        lbfgs = list(accuracy[9:18])
        
        liblinear = list(accuracy[18:])
        
        elements = ['lbfgs', 'liblinear', 'newton']
        
        labels = df['C']
        labels = labels[:9]
        
        fig, ax = plt.subplots()
        
        plt.title("Model {} | Graph of {}".format(file[-24:], h))
        plt.plot(liblinear)
        plt.plot(newton)
        plt.plot(lbfgs)
        plt.legend(elements)
        plt.xlabel('C Value')
        plt.ylabel('Average Cross Validation Accuracy')
        ax.set_xticklabels(labels)
        plt.show()
        
    
    
    

def plot_optim_fair(optim_file, fair_file):
    
    addr = "C:\\Users\\Student\\Documents\\y1sussexAI\\MachineLearning\\CourseWork\\Results\\"
    
    df = pd.read_csv(optim_file)
    df_fair = pd.read_csv(fair_file)
    
    accuracy = df['Accuracy']
    accuracyFair = df_fair['Accuracy']
    
    newton = list(accuracy[:9])
    
    lbfgs = list(accuracy[9:18])
    
    liblinear = list(accuracy[18:])
    
    newtonFair = list(accuracyFair[:9])
    
    lbfgsFair = list(accuracyFair[9:18])
    
    liblinearFair = list(accuracyFair[18:])
    
    labels = df['C']
    labels = labels[:9]
    
    fig, ax = plt.subplots()
    
    plt.title("Logistic Regression non-fair to Fair optimization")
    plt.plot(newton)
    plt.plot(newtonFair)
    plt.legend(['Optim', 'Fair'])
    plt.xlabel('C Value')
    plt.ylabel('Average Cross Validation Accuracy')
    ax.set_xticklabels(labels)
    plt.show()
    

def plot_cross_validation(file_name):
    
    print(file_name)
    cross = pd.read_csv(file_name)
    vals = []
    j = 0
    
    for ind in cross.index:
        row = [cross['crossVal1'][ind], cross['crossVal2'][ind], cross['crossVal3'][ind], cross['crossVal4'][ind], cross['crossVal5'][ind]]
        vals.append(row)
        

        if j == 9:
            break
        
        j = j + 1
        
    
    print()
    print()
    labels = cross['C']
    labels = labels[:9]
    
    fig, ax = plt.subplots()
    plt.plot(vals)
    plt.ylabel("Accuracy")
    plt.xlabel("C Value")
    ax.set_xticklabels(labels)
    plt.show()
    
    

def plot_accuracy_general(file):
    df = pd.read_csv(file)
    print(df.head)
    
    heads = df.head()
    
    print(heads)
    
    accuracy = df['Accuracy']
    test = df['general']
    fig, ax = plt.subplots()
    plt.title("Graph {} ".format(file[-24:]))
    plt.plot(accuracy)
    plt.plot(test)
    plt.ylabel('Accuracy')
    plt.xlabel("C")
    plt.legend(['train', 'test'])
    labels = df['C']
    labels = labels[:9]
    ax.set_xticklabels(labels)
    plt.show()
    
    

addr = "C:\\Users\\Student\\Documents\\y1sussexAI\\MachineLearning\\CourseWork\\ResultsV2\\"

files = os.listdir(addr)

print(files)




for f in files:
    
    file_addr = addr + f
    print(file_addr)
    #smart_plot(file_addr)
    #plot_optim(file_addr)
    #plot_cross_validation(file_addr)
    plot_accuracy_general(file_addr)



