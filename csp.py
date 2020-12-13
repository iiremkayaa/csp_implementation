# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:06:24 2020
@author: Irem
"""
import sys
import re

def getData(fileName,dictOfData): #adds the data read from the file to the array
    file1 = open(fileName, "r")    
    Lines = file1.readlines() 
    for line in Lines: 
        eachLine=line.replace("\n","").split(",")
        arr=[]
        for i in range(1,len(eachLine)):
            arr.append(eachLine[i])
        dictOfData[eachLine[0]]=arr

def getClues(fileName,clues): #adds the clues read from the file to the array
    file1 = open(fileName, "r")    
    Lines = file1.readlines() 
    for line in Lines: 
        eachLine=line.replace("\n","").split(" ")
        clues.append(eachLine)

def checkIsLeaf(dictOfData): #checks if all value lists have a single element
    flag= len(dictOfData["notSelected"])==0 
    for key in dictOfData:
        if(key =="notSelected"):
            continue
        if len(dictOfData[key])!=1:
           flag=False
           break
    return flag
def checkIsExist(dictOfData): #checks if empty value list is exist
    flag=True
    for key in dictOfData:
        if key=="notSelected":
            continue
        if len(dictOfData[key])==0:
            flag=False
            break
    return flag
def removeFromArray(arr,index,attr1,value):
    newDict=arr[index][attr1][:]
    newDict.remove(value)
    arr[index][attr1]=newDict
def MRV(dictOfData):  #return selected attribute according to Minimum Remaining Values 
    minLen=sys.maxsize      #if domain sizes are equal,it returns alphabetically smallest word
    minArr=[]
    resultArr=[]
    for i in dictOfData:
        
        if(i=="notSelected"):
            continue
        if i in dictOfData["notSelected"]:
            if(len(dictOfData[i])<=minLen):
                minLen=len(dictOfData[i])
                minArr.append(i)
    for v in dictOfData:
        if v=="notSelected":
            continue
        if(len(dictOfData[v])==minLen ):
            if (v in minArr):
                resultArr.append(v)
    return min(resultArr)
def checkEqual(clue,arr):
    firstCond=re.split('[()]',clue[0])
    attr1=firstCond[0].strip() 
    equality1=firstCond[1].strip() 
    equalityAttr1=equality1.split("=")[0] 
    equalityVal1=equality1.split("=")[1] 
    secondCond=re.split('[()]',clue[2])
    attr2=secondCond[0].strip() 
    equality2=secondCond[1].strip() 
    equalityAttr2=equality2.split("=")[0] 
    equalityVal2=equality2.split("=")[1]   
    for index in range(len(arr)):
        if attr1==attr2:
            if len(arr[index][equalityAttr1])==1 and arr[index][equalityAttr1][0]==equalityVal1:
                if equalityVal2 in arr[index][equalityAttr1]:
                    arr[index][equalityAttr2]=[equalityVal2]
                else:
                    arr[index][equalityAttr2]=[]
            if len(arr[index][equalityAttr2])==1 and arr[index][equalityAttr2][0]==equalityVal2:
                if equalityVal1 in arr[index][equalityAttr1]:
                    arr[index][equalityAttr1]=[equalityVal1]
                else:
                    arr[index][equalityAttr1]=[]
def removeFromNode(node,attribute,value):
    newDict=node[attribute][:]
    newDict.remove(value)
    node[attribute]=newDict
def checkDifferentPossibilities(currentNode,firstAttr,firstValue,secondAttr,secondValue):
    if firstValue in currentNode[firstAttr]:
        removeFromNode(currentNode, firstAttr, firstValue)
    if secondValue in currentNode[secondAttr]:
        removeFromNode(currentNode,secondAttr,secondValue)
def checkOneOfPossibilities(attr2,attr3,attr4,val2,val3,val4,dictionary):
                    if val2 in dictionary[attr2][0]:
                        removeFromNode(dictionary, attr2, val2)
                    if len(dictionary[attr3])==1 and dictionary[attr3][0]==val3:
                        if val4 in dictionary[attr4][:]:
                            removeFromNode(dictionary, attr4, val4)
                    if len(dictionary[attr4])==1 and dictionary[attr4][0]==val4:
                        if val3 in dictionary[attr3][:]:
                            removeFromNode(dictionary, attr2, val3)
                    if ( len(dictionary[attr4])==1 and dictionary[attr4][0]!=val4):
                        if (len(dictionary[attr3])==1 and dictionary[attr3][0]!=val3):
                            dictionary[attr3]=[] 
def checkIfNot(clue,arr):
    cond=clue[1].split("=")
    attr1=cond[0]
    value1=cond[1]
    cond2=clue[4].split("=")
    attr2=cond2[0]
    value2=cond2[1]
    for index in range(len(arr)):
                    if len(arr[index][attr1])==1 and arr[index][attr1][0]==value1 :
                        if len(arr[index][attr2])==1 and arr[index][attr2][0]==value2 :
                            arr[index][attr1]=[]
                    if len(arr[index][attr1])==1 and arr[index][attr1][0]==value1 :
                        result=clue[4].split("=")
                        resultAtr=result[0]
                        resultVal=result[1]
                        if resultVal in arr[index][resultAtr]:
                            removeFromArray(arr, index, resultAtr, resultVal)
                    if len(arr[index][attr2])==1 and arr[index][attr2][0]==value2 :
                        result2=clue[1].split("=")
                        resultAtr2=result2[0]
                        resultVal2=result2[1]
                        if resultVal2 in arr[index][resultAtr2]:
                            removeFromArray(arr, index, resultAtr2, resultVal2)    
def checkIfEither(clue,arr):
    cond=clue[1].split("=")
    attr1=cond[0]
    value1=cond[1]
    result1=clue[4].split("=") 
    resultAtr1=result1[0] 
    resultVal1=result1[1]  
    result2=clue[6].split("=")
    resultAtr2=result2[0]
    resultVal2=result2[1]
    for index in range(len(arr)):
                    if len(arr[index][attr1])==1 and arr[index][attr1][0]==value1 :
                        if len(arr[index][resultAtr2])==1 and arr[index][resultAtr2][0]!=resultVal2:
                            if len(arr[index][resultAtr1])==1 and arr[index][resultAtr1][0]!=resultVal1:
                                arr[index][attr1]=[]
                        elif len(arr[index][resultAtr2])==1 and arr[index][resultAtr2][0]==resultVal2:
                            if len(arr[index][resultAtr1])==1 and arr[index][resultAtr1][0]==resultVal1:
                                    arr[index][attr1]=[]
                        elif len(arr[index][resultAtr1])==1 and arr[index][resultAtr1][0]==resultVal1:
                            valueList=arr[index][resultAtr2][:]
                            if resultVal2 in valueList:  
                               removeFromArray(arr, index, resultAtr2, resultVal2)
                        elif len(arr[index][resultAtr2])==1 and arr[index][resultAtr2][0]==resultVal2:
                            valueList=arr[index][resultAtr1][:]
                            if resultVal1 in valueList:
                                removeFromArray(arr, index, resultAtr1, resultVal1)
                    if len(arr[index][resultAtr1])==1 and arr[index][resultAtr1][0]==resultVal1 and len(arr[index][resultAtr2])==1 and arr[index][resultAtr2][0]==resultVal2:
                        if value1 in arr[index][attr1]:
                           removeFromArray(arr, index, attr1, value1)
def checkIf(clue,arr):
    cond=clue[1].split("=") 
    attr1=cond[0] 
    value1=cond[1] 
    cond2=clue[3].split("=") 
    attr2=cond2[0] 
    value2=cond2[1] 
    for index in range(len(arr)):
                     if len(arr[index][attr1])== 1 and arr[index][attr1][0]==value1:
                         arr[index][attr2]=[value2]
                     if len(arr[index][attr2])== 1 and arr[index][attr2][0]==value2:
                         arr[index][attr1]=[value1]
def checkOneOf(clue,arr):
    cluster=clue[2].strip("{}").split(",")
    cluster1=cluster[0]
    cluster2=cluster[1]
    cluster3=clue[5]
    cluster4=clue[7]
    attr1=cluster1.split("=")[0]
    val1=cluster1.split("=")[1]
    attr2=cluster2.split("=")[0]
    val2=cluster2.split("=")[1]
    attr3=cluster3.split("=")[0]
    val3=cluster3.split("=")[1]
    attr4=cluster4.split("=")[0]
    val4=cluster4.split("=")[1]
    for index in range(len(arr)):
                if len(arr[index][attr1])== 1 and arr[index][attr1][0]==val1:
                    checkOneOfPossibilities(attr2, attr3, attr4, val2, val3, val4, arr[index]);            
                if len(arr[index][attr2])== 1 and arr[index][attr2][0]==val2:
                   checkOneOfPossibilities(attr1, attr3, attr4, val1, val3, val4, arr[index])
def checkDifferent(clue,arr):
    conds=clue[0].strip("{}").split(",")
    cond1=conds[0].split("=")
    attr1=cond1[0] 
    val1=cond1[1] 
    cond2=conds[1].split("=")
    attr2=cond2[0] 
    val2=cond2[1] 
    cond3=conds[2].split("=")
    attr3=cond3[0] 
    val3=cond3[1] 
    for index in range(len(arr)):
                if len(arr[index][attr1])== 1 and arr[index][attr1][0]==val1:
                    checkDifferentPossibilities(arr[index],attr2,val2,attr3,val3)
                if len(arr[index][attr2])== 1 and arr[index][attr2][0]==val2:
                    checkDifferentPossibilities(arr[index], attr1, val1, attr3, val3)
                if len(arr[index][attr3])== 1 and arr[index][attr3][0]==val3:
                    checkDifferentPossibilities(arr[index], attr2, val2, attr1, val1)
def checkPlusPossibilities(number, arr, equalityAttr1, equalityVal1, attr1, difference, equalityAttr2, equalityVal2,value,minOrMax):
    dataListClone=dataList[attr1][:]
    for indexFirst in range(len(arr)):     
                        if ((len(arr[indexFirst][equalityAttr1])==1) and (arr[indexFirst][equalityAttr1][0]==str(equalityVal1))):
                            while number>0:
                                if str(value) in arr[indexFirst][attr1]:
                                    removeFromArray(arr, indexFirst, attr1, value)
                                dataListClone.remove(value)
                                if minOrMax==1:
                                    value=min(dataListClone)
                                elif minOrMax==2:
                                    value=max(dataListClone)
                                number-=difference
                            if equalityVal2 in arr[indexFirst][equalityAttr2]:
                                    removeFromArray(arr, indexFirst, equalityAttr2, equalityVal2)

def checkPlusOrMinus(clue,arr,operation):
    firstCond=re.split('[()]',clue[0])#this function executes this elimination
    attr1=firstCond[0].strip() 
    equality1=firstCond[1].strip() 
    equalityAttr1=equality1.split("=")[0] 
    equalityVal1=equality1.split("=")[1] 
    difference=int(dictOfData[attr1][1])-int(dictOfData[attr1][0])   
    secondCond=re.split('[()]',clue[2])
    attr2=secondCond[0].strip() 
    equality2=secondCond[1].strip() 
    equalityAttr2=equality2.split("=")[0] 
    equalityVal2=equality2.split("=")[1]   
    number=int(clue[4]) #4
    minValue=min(dataList[attr1])
    maxValue=max(dataList[attr2])
    if operation=="+":
         checkPlusPossibilities(number, arr, equalityAttr1, equalityVal1, attr1, difference, equalityAttr2, equalityVal2,minValue,1)
         checkPlusPossibilities(number, arr, equalityAttr2, equalityVal2, attr1, difference, equalityAttr1, equalityVal1,maxValue,2)
    if operation=="-": # if n(x=a) = n(y=b) - m,  n(x=a) can be at most max(n)- m. n(y=b) can be at least min(n)+m
        checkMinusPossibilities(number, arr, equalityAttr1, equalityVal1, attr1, difference, equalityAttr2, equalityVal2,maxValue,1)
        checkMinusPossibilities(number, arr, equalityAttr2, equalityVal2, attr1, difference, equalityAttr1, equalityVal1,minValue,2)


def checkMinusPossibilities(number, arr, equalityAttr1, equalityVal1, attr1, difference, equalityAttr2, equalityVal2,value,minOrMax):
    dataListClone=dataList[attr1][:]
    for indexFirstMinus in range(len(arr)):
                        if ((len(arr[indexFirstMinus][equalityAttr1])==1) and (arr[indexFirstMinus][equalityAttr1][0]==equalityVal1)):
                            while number>0:
                                if str(value) in arr[indexFirstMinus][attr1]:
                                    removeFromArray(arr, indexFirstMinus, attr1, value)
                                dataListClone.remove(value)
                                if minOrMax==1:
                                    value=max(dataListClone)
                                if minOrMax==2:
                                    value=min(dataListClone)
                                number-=difference
                            if equalityVal2 in arr[indexFirstMinus][equalityAttr2]:
                                removeFromArray(arr, indexFirstMinus, equalityAttr2, equalityVal2)

def checkGreaterThanPossibilities(arr,equalityAttr1,equalityAttr2,equalityVal1,equalityVal2,value,attr1):
    for index in range(len(arr)):
                    if ((len(arr[index][equalityAttr1])==1) and (arr[index][equalityAttr1][0]==equalityVal1)):  
                        if str(value) in arr[index][attr1]:
                            removeFromArray(arr,index,attr1,value)
                        if equalityVal2 in arr[index][equalityAttr2]:
                            removeFromArray(arr, index, equalityAttr2, equalityVal2)

def checkSmallerThanPossibilities(arr, equalityAttr1, equalityAttr2, equalityVal1, equalityVal2, value, attr1):
    for index in range(len(arr)):
                    if ((len(arr[index][equalityAttr1])==1) and (arr[index][equalityAttr1][0]==equalityVal1)):  
                        if str(value) in arr[index][attr1]:
                            removeFromArray(arr,index,attr1,value)
                        if equalityVal2 in arr[index][equalityAttr2]:
                            removeFromArray(arr, index, equalityAttr2,equalityVal2)
def checkSmallerOrGreaterThan(clue,arr,operation):
    firstCond=re.split('[()]',clue[0]) #This function executes this elimination
    attr1=firstCond[0].strip() 
    equality1=firstCond[1].strip() 
    equalityAttr1=equality1.split("=")[0] 
    equalityVal1=equality1.split("=")[1] 
    secondCond=re.split('[()]',clue[2])
    attr2=secondCond[0].strip() 
    equality2=secondCond[1].strip() 
    equalityAttr2=equality2.split("=")[0] 
    equalityVal2=equality2.split("=")[1]     
    minValue=min(dataList[attr1])
    maxValue=max(dataList[attr2])
    if operation==">": # if A is greater than B, B can not have maximum number and A can not have minimum number
        checkGreaterThanPossibilities(arr, equalityAttr1, equalityAttr2, equalityVal1, equalityVal2, minValue, attr1)
        checkGreaterThanPossibilities(arr, equalityAttr2, equalityAttr1, equalityVal2, equalityVal1, maxValue, attr1)
    if operation=="<": # if A is smaller than B, A can not have maximum number and B can not have minimum number
        checkSmallerThanPossibilities(arr, equalityAttr1, equalityAttr2, equalityVal1, equalityVal2, maxValue, attr1)
        checkSmallerThanPossibilities(arr, equalityAttr2, equalityAttr1, equalityVal2, equalityVal1, minValue, attr2)

def removeUnnecessaryValues(arr):
    for clue in clues:
        if clue[0]=="if":
            if ((clue[0].lower()=="if") and (clue[2].lower()=="then") and (clue[3].lower()=="not")):
                checkIfNot(clue,arr)
            elif((clue[0].lower()=="if") and (clue[2].lower()=="then") and (clue[3].lower()=="either")):
                checkIfEither(clue, arr)
            elif((clue[0].lower()=="if") and (clue[2].lower()=="then") ):
                checkIf(clue,arr)
        elif clue[0]=="one" and clue[1]=="of":
            checkOneOf(clue, arr)
        elif clue[1]=="are" and clue[2]=="all" and clue[3]=="different":
            checkDifferent(clue, arr)
        elif clue[1] == "=":
            if clue[3]=="+":
                checkPlusOrMinus(clue,arr,"+")
            elif clue[3]=="-":
                checkPlusOrMinus(clue,arr,"-")
            else:
                checkEqual(clue, arr)
        elif clue[1]==">":
            checkSmallerOrGreaterThan(clue, arr, ">")
        elif clue[1]=="<":
            checkSmallerOrGreaterThan(clue, arr, "<")
    return arr
                
        
def checkCond(attr,node):
    arr=[]
    for key in node[attr]:
        valueArr={}
        for attribute in node:
            if attribute==attr:
                valueArr[attribute]=[]
                valueArr[attribute].append(key)
                continue
            if attribute=="notSelected":
                notSelectedArr=[]
                for i in node["notSelected"]:
                    if i != attr:
                        notSelectedArr.append(i)
                valueArr["notSelected"]=notSelectedArr #selected attribute is removed from notSelected list
                continue                          #and sub-nodes is occured from given node
            valueArr[attribute]=node[attribute]
        arr.append(valueArr)
    arr=removeUnnecessaryValues(arr) #eliminate values according to clues
    
    return arr
def eliminateNode(array): #removed zero-length value list 
    newArray=array[:]
    for currentNode in newArray:
        for key in currentNode:
            if key=="notSelected":
                continue
            if len(currentNode[key])==0:
                if currentNode in array:
                    array.remove(currentNode)
    array=newArray
    return array
def applyCsp(node): #until reaching leaf node, applyCsp function is called
    if checkIsExist(node) ==False: #if node has zero-length value list, it's not accepted
        return -1 
    elif checkIsLeaf(node): #leaf nodes are added to lists according to the groups it's in/its value for the first selected attribute
            if node[firstGroupedItem][0]==firstGroupedItemList[0]:
                    group1.append(node)
            if node[firstGroupedItem][0]==firstGroupedItemList[1]:  
                    group2.append(node)
            if node[firstGroupedItem][0]==firstGroupedItemList[2]: 
                    group3.append(node)
            if node[firstGroupedItem][0]==firstGroupedItemList[3]:  
                    group4.append(node)
            resultSet.append(node)
            return
    else:
        attr=MRV(node) #applies MRV and returns selected attribute
        array=checkCond(attr,node) #nodes are divided into different sub-nodes according to the selected attribute and the values of the nodes are selected or eliminated according to clues
        array=eliminateNode(array) # if node has zero-length value list, it is removed from array
        for selectedNode in array:
            applyCsp(selectedNode)         
                
def eliminateLeaf(): #according to solutions array, nodes within groups are eliminated
    while True: # elimination is executed until  no change
        flag=False
        for solution in solutions:
            for key in solution:
                if solution[key]=="":
                    continue
                for key2 in solution:
                    if solution[key2]=="":
                        continue
                    
                    for groupIndex in range(len(groups)):
                        copyGroup=groups[groupIndex][:]
                        for leaf in groups[groupIndex]:
                            if (leaf[key][0]==solution[key] and
                                leaf[key2][0]!=solution[key2]):
                                copyGroup.remove(leaf)
                                groups[groupIndex]=copyGroup
                                flag=True
                            if (leaf[key][0]!=solution[key] and
                                leaf[key2][0]==solution[key2] ):             
                                copyGroup.remove(leaf)
                                groups[groupIndex]=copyGroup
                                flag=True
        if flag==False:
            break
def checkSolutionForMinusOrPlus(clue,nodeList,operation):
    firstCond=re.split('[()]',clue[0])
    attr1=firstCond[0].strip() 
    equality1=firstCond[1].strip() 
    equalityAttr1=equality1.split("=")[0] 
    equalityVal1=equality1.split("=")[1] 
    secondCond=re.split('[()]',clue[2])
    attr2=secondCond[0].strip() 
    equality2=secondCond[1].strip() 
    equalityAttr2=equality2.split("=")[0] 
    equalityVal2=equality2.split("=")[1] 
    number=int(clue[4])
    value1=0
    value2=0
    flag=True
    for node in nodeList:
        if node[equalityAttr1][0]==equalityVal1:
                 value1=int(node[attr1][0])
        if node[equalityAttr2][0]==equalityVal2:
                 value2=int(node[attr2][0])
    if operation=="+":
        if value1 != number+value2:
                     flag=False
    elif operation=="-":
        if value1 != value2-number:
            flag=False
    return flag
def checkSolutionForSmallerOrGreaterThan(clue,nodeList,operation):
    firstCond=re.split('[()]',clue[0])
    attr1=firstCond[0].strip() 
    equality1=firstCond[1].strip() 
    equalityAttr1=equality1.split("=")[0] 
    equalityVal1=equality1.split("=")[1] 
                        
    secondCond=re.split('[()]',clue[2])
    attr2=secondCond[0].strip() 
    equality2=secondCond[1].strip() 
    equalityAttr2=equality2.split("=")[0] 
    equalityVal2=equality2.split("=")[1] 
    flag=True
    for node in nodeList:
           if node[equalityAttr1][0]==equalityVal1:
                   value1=int(node[attr1][0])
           if node[equalityAttr2][0]==equalityVal2:
                   value2=int(node[attr2][0])
    if operation==">":
        if value1 <= value2:
               flag=False
    elif operation=="<":
        if value1 >= value2:
               flag=False
    return flag
def checkSolutionForAllDifferent(clue,nodeList): #if node provides "{x=a,y=b,z=c} are all different", it returns true, or false otherwise
    conds=clue[0].strip("{}").split(",")
    cond1=conds[0].split("=")
    attr1=cond1[0] 
    val1=cond1[1] 
                    
    cond2=conds[1].split("=")
    attr2=cond2[0] 
    val2=cond2[1] 
                    
    cond3=conds[2].split("=")
    attr3=cond3[0] 
    val3=cond3[1] 
    index1=0
    index2=0
    index3=0
    flag=True
    for index in range(len(nodeList)):
        if nodeList[index][attr1][0]==val1:
                index1=index
        if nodeList[index][attr2][0]==val2:
                index2=index
        if nodeList[index][attr3][0]==val3:
                index3=index
    if index1==index2 or index1==index3 or index2==index3:
                flag=False
    return flag
def checkSolutionForCorresponding(nodeList,clue): #if node provides "one of {x=a,y=b} corresponds to z=c other t=d ", it returns true, or false otherwise
    cluster=clue[2].strip("{}").split(",")
    cluster1=cluster[0]
    cluster2=cluster[1]
    cluster3=clue[5]
    cluster4=clue[7]
    attr1=cluster1.split("=")[0]
    val1=cluster1.split("=")[1]
    attr2=cluster2.split("=")[0]
    val2=cluster2.split("=")[1]
    attr3=cluster3.split("=")[0]
    val3=cluster3.split("=")[1]
    attr4=cluster4.split("=")[0]
    val4=cluster4.split("=")[1]
    flag=True
    for node in nodeList:
         if node[attr1][0]==val1:
                flag2=False
                for node2 in nodeList:
                    if node[attr3][0]==val3:
                               flag2=True
                    if node[attr4][0]==val4:
                               flag2=True
                if flag2==False:
                     flag2=False
                     break
         if node[attr2][0]==val2:
              flag2=False
              for node2 in nodeList:
                     if node[attr3][0]==val3:
                             flag2=True
                     if node[attr4][0]==val4:
                             flag2=True
              if flag2==False:
                    flag=False
    return flag
def checkSolution(node1,node2,node3,node4): #checks clues by comparing nodes
    nodeList=[node1,node2,node3,node4]
    result=True
    for attribute in attributes:
            for i in range(4):
                  for j in range(i+1,4):
                      if nodeList[i][attribute]==nodeList[j][attribute]:
                          result=False #if same values are selected in different nodes, it's incorrect
    if result==True:
        for clue in clues:
                if clue[1] == "=":
                    if clue[3]=="+":
                        result=checkSolutionForMinusOrPlus(clue,nodeList,"+") #if node provides "n(x=a) = n(y=b) + m", it returns true, or false otherwise
                        if result==False:
                            break
                    if clue[3]=="-":
                        result=checkSolutionForMinusOrPlus(clue,nodeList,"-")#if node provides "n(x=a) = n(y=b) - m", it returns true, or false otherwise
                        if result==False:
                            break
                elif clue[1]==">":
                        result=checkSolutionForSmallerOrGreaterThan(clue, nodeList,">")
                        if result==False:
                            break
                elif clue[1]=="<":
                        result=checkSolutionForSmallerOrGreaterThan(clue, nodeList,"<")
                        if result==False:
                            break
                elif clue[1]=="are" and clue[2]=="all" and clue[3]=="different":
                    result=checkSolutionForAllDifferent(clue, nodeList)
                    if result==False:
                        break
                elif clue[0]=="one" and clue[1]=="of":
                    result=checkSolutionForCorresponding(nodeList, clue)
                    if result==False:
                        break  
    return result   
def getGroupedItem(): #returns first selected attributes according to Minimum Remaining Values
        minLen=sys.maxsize     
        minArr=[]
        resultArr=[]
        for i in dictOfData:
            if(i=="notSelected"):
                continue
            if i in dictOfData["notSelected"]:
                if(len(dictOfData[i])<=minLen):
                    minLen=len(dictOfData[i])
                    minArr.append(i)
        for v in dictOfData:
            if v=="notSelected":
                continue
            if(len(dictOfData[v])==minLen ):
                if (v in minArr):
                    resultArr.append(v)
        return min(minArr)
def createSolutionArray(group1,group2,group3,group4): #return solution after checking nodes among themselves
    solutionArr=[]
    for g1 in group1:
        for g2 in group2:
            for g3 in group3:
                for g4 in group4:
                    if checkSolution(g1,g2,g3,g4)==True:
                        solutionArr.append(g1)
                        solutionArr.append(g2)
                        solutionArr.append(g3)
                        solutionArr.append(g4)
                        return solutionArr
    return solutionArr
 
def sortSolution(e):
    return e[keys[0]] 
if __name__ == "__main__":
    
    print("The problems available in this directory: 1 2 3")
    print("\nChoose a problem:")
    inputNumber = input()
    dataFileName="data-"+inputNumber+".txt"
    cluesFileName="clues-"+inputNumber+".txt"
    print("Here is the solution to the problem defined in ",dataFileName," and ",cluesFileName,".\n")
    resultSet=[] #contains leaf nodes that occur after checking clues
    dictOfData={} #contains attributes and their values
    clues=[] #contains clues line by line
    getClues(cluesFileName,clues)
    getData(dataFileName,dictOfData) 
    firstGroupedItem="" #first selected attribute to divide into 4 groups
    firstGroupedItemList=[] #values that belongs to the first selected attribute
    group1=[] 
    group2=[]
    group3=[]
    group4=[]
    dataList=dictOfData
    dictOfData["notSelected"]=[]
    for key in dictOfData:
        if key == "notSelected":
            continue
        dictOfData["notSelected"].append(key)
    firstGroupedItem=getGroupedItem()
    firstGroupedItemList=dictOfData[firstGroupedItem]

    applyCsp(dictOfData)
    
    
    groups=[group1,group2,group3,group4] #contains 4 groups separated by firstGroupedItem
    attributes=[] #list of attributes

    for attribute in dictOfData:
        if attribute=="notSelected":
            continue
        attributes.append(attribute)
    solutions=[]
    for i in range(4):
        dictionary={}
        for attribute in dictOfData:
            if attribute=="notSelected":
                continue
            dictionary[attribute]=""
        solutions.append(dictionary)
    for group in groups:
        attributeList=[]
        for attribute in attributes:
            firstNode=group[0]
            isSame=True
            selectedValue=""
            for node in group:
                selectedValue=node[attribute][0]
                if node==firstNode:
                    continue
                if node[attribute]!=firstNode[attribute]:
                    isSame=False
                    break
            if isSame:
                index=groups.index(group)
                solutions[index][attribute]=selectedValue
    #after reaching the depth nodes, the arrays of solutions contain the exact
        #results without comparing the groups among themselves
    #for example if years is 2007,hometown must be Ravendale
    eliminateLeaf() #according to exact results, nodes within groups are eliminated
    solutionArray=createSolutionArray(groups[0], groups[1], groups[2], groups[3]) #The result is obtained by considering the comparisons between nodes
    keys=list(solutionArray[0].keys())
    solutionArray.sort(key=sortSolution) #sorts by year/days etc.
    print("{}   |   {}   |   {}   |   {}".format(keys[0],keys[1],keys[2],keys[3]))                  
    print("----------------------------------------------------------------")
    for solution in solutionArray:
        print("{}   |   {}   |   {}   |   {}".format(solution[keys[0]][0],solution[keys[1]][0],solution[keys[2]][0],solution[keys[3]][0]))                  
