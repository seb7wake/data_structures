from data import *
import webPageIndex
import webpagePriorityQueue
import os

def readFiles(folder):
    files = os.listdir(folder) #get list of files in the folder
    filesContent = [] 
    for file in files:
        #appending the contents of each file
        filesContent.append(webPageIndex.WebPageIndex('data/'+file).contents) #appending contents
    return filesContent

if __name__ == '__main__': 
    wpq = webpagePriorityQueue
    data = readFiles('data') #list of contents from each files
    filenames = os.listdir('data') #list filenames
    file = open('queries.txt', 'r') 
    lines = file.readlines() 
    queries = []
    for query in lines:
        #list of query strings
        queries.append(query.replace('\n', ''))
    for i in queries:
        #printing heaps
        print('Query:', i)
        heap = wpq.webpagePriorityQueue.reheap(wpq, i, data).heap
        for i in range(len(filenames)):
            print(filenames[i], ": ", heap[i])
        print('\n')
