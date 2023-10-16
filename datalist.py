import os
import numpy as np

LR_set= []
HR_set= []

LR_path='train_LR'
HR_path='train_HR'

def traversal_files(path, files):
    for item in os.listdir('training_set'+'/'+path):
            files.append(path+'/'+item)

traversal_files(HR_path, HR_set)
traversal_files(LR_path, LR_set)

HR_set.sort()
LR_set.sort()

text=''

for i in range(len(HR_set)):
    text=text+HR_set[i]+' '+LR_set[i]+'\n'
    
datalist=open('datalist_HE.txt', 'w')
datalist.write(text)
datalist.close()
