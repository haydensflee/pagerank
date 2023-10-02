import numpy as np
import time

class node:
  def __init__(self, nodeNumber):
    self.nodeNumber = nodeNumber
    self.oldPR = -1.0
    self.newPR = -1.0
    self.outgoingNodes=[]
    self.incomingNodes=[]
    self.outgoingNodeCount=-1
    self.incomingNodeCount=-1


def main():
    start = time.time()
    for i in range(10):
        print(i)
    time.sleep(1)
    # filename="IBM.txt"
    filename="web-Google.txt"
    file1 = open(filename, 'r')
    count=0
    # count=5
    nodeDict={}
    fromNodeList=[]
    toNodeList=[]
    while True:
        
    
        # Get next line from file
        line = file1.readline()
    
        # if line is empty
        # end of file is reached
        if not line:
            break
        if(count>3):
            values = line.split("\t")
            # values = line.split(",")
            fromNodeList.append(int(values[0]))
            toNodeList.append(int(values[1]))
        count += 1
    file1.close()

    # ---------- READ IN TEXT FILE INFO AND POPULATE NODE OBJECT DICTIONARY <node number, node> ---------- #
    for i in range(len(fromNodeList)):
        if fromNodeList[i] in nodeDict:
            tempNode=nodeDict.get(fromNodeList[i])
            tempVec=[]
            tempVec=tempNode.outgoingNodes
            tempVec.append(toNodeList[i])
            tempNode.outgoingNodes=tempVec
            tempNode.outgoingNodeCount=len(tempVec)

            nodeDict[fromNodeList[i]]=tempNode
        else:
            tempNode=node(fromNodeList[i])
            tempVec=tempNode.outgoingNodes
            tempVec.append(toNodeList[i])
            tempNode.outgoingNodes=tempVec
            tempNode.outgoingNodeCount=len(tempVec)

            nodeDict[fromNodeList[i]]=tempNode
            

        if toNodeList[i] in nodeDict:
            tempNode=nodeDict.get(toNodeList[i])
            tempVec=[]
            tempVec=tempNode.incomingNodes
            tempVec.append(fromNodeList[i])
            tempNode.incomingNodes=tempVec
            tempNode.incomingNodeCount=len(tempVec)

            nodeDict[toNodeList[i]]=tempNode
        else:
            tempNode=node(toNodeList[i])
            tempVec=tempNode.incomingNodes
            tempVec.append(fromNodeList[i])
            tempNode.incomingNodes=tempVec
            tempNode.incomingNodeCount=len(tempVec)
            
            nodeDict[toNodeList[i]]=tempNode
        
    N=len(nodeDict)
    nodeList=list(nodeDict)

    # ---------- INITIALISE PAGERANK OF ALL NODES ---------- #
    for key, value in nodeDict.items():
        value.oldPR=1.0/N

    iterations=50
    damping=0.85
    counter=0
    unsortedDict={}
    sortedDict={}
    # ---------- PERFORM PAGERANK CALCULATION ---------- #
    for i in range(iterations):
        print(i)
            
        for key, value in nodeDict.items():
            incomingCount=value.incomingNodeCount
            incomingNodeList=value.incomingNodes
            sum=0
            for i in range(incomingCount):
                tempNode=nodeDict[incomingNodeList[i]]
                sum=sum+(tempNode.oldPR/tempNode.outgoingNodeCount)
            newPR=(1.0-damping)/N+damping*sum
            value.oldPR=newPR
            counter+=1
            unsortedDict[value.nodeNumber]=value.oldPR
    print("===================")   
        
    sorted_keys = sorted(unsortedDict, key=unsortedDict.get, reverse=True)  # [1, 3, 2]
    
    for i in sorted_keys:
        sortedDict[i] = unsortedDict[i]

    counter=0
    print("raw output")
    file1 = open("PageRank_Top10.txt","w")
    file1.write("PageRank Top 10:\nNode\tPageRank\n")
    file2 = open("PageRank_All.txt","w")
    file2.write("PageRank All:\nNode\tPageRank\n")
    
    # with open('readme.txt', 'w') as f:
    for key,value in sortedDict.items():
        tempStr=""
        tempStr=str(key)+"\t"+str(value)+"\n"
        file2.write(tempStr)
        if(counter<10):
            file1.write(tempStr)
        # print(key,"\t",value)
        
        counter+=1
    counter=0
    file1.close()
    file2.close()
    end = time.time()
    print(f"Runtime of the program is {end - start}")

if __name__ == "__main__":
    main()