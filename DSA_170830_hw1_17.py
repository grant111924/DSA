# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:00:54 2017

@author: Grant
"""

import numpy as np
import random as rand
#x=rand.random()
#print("x=%f"%(x))
dataList=[]
def GenerateData():
    for i in range(20):   
        tempX=rand.random()*2-1
        tempY=np.sign(tempX)
        tempArray=[tempX,tempY]
        #print("X=%f Y=%f"%(tempArray[0],tempArray[1]))
        print(tempArray)
        dataList.append(tempArray)
    


GenerateData()

print(dataList)