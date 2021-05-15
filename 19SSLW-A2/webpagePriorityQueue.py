import webPageIndex

class webpagePriorityQueue:
    def __init__(self, pages, query):  
        self.query = query
        self.heap = []
        if pages is not None:
            for page in pages:
                #creating heap
                self.push(page)
    
    #Push a new value onto the priority queue
    def push(self, page):
        query = self.query.split() #split query for each word
        count = []
        wpi = webPageIndex  
        wpq = webpagePriorityQueue 
        for i in range(len(query)): 
            #append the count of the query word in the page
            count.append(wpi.WebPageIndex.getCount(self, page, query[i]))
        s = sum(count) #sums values in the count array
        self.heap.append(s) #appending to heap
        self.bottom_up(self.heap, len(self.heap)-1) #sort heap from bottom up
    
    #returns highest value
    def peek(self):
        if len(self.heap) != 0:
            #return highest value whch is the value with index 0
            return self.heap[0]
        else:
            return None
    
    def poll(self):
        if len(self.heap)!=0:
        # swapping the root value with the last value.
 
            self.swap(self.heap, len(self.heap) - 1, 0)
        # storing the popped value in the root variable
 
            root = self.heap.pop()
 
        #Calling the top_down function to ensure that the heap is still in order 
            self.top_down(self.heap, 0)
             
        else:
            root="Heap is empty"
        return root
    
    def swap(self, L, i, j):
        L[i], L[j] = L[j], L[i]
    
    # This is a private function which ensures heap is in order after root is popped
    def top_down(self, heap, index):
        child_index = 2 * index + 1
        # If we are at the end of the heap, return nothing
        if child_index >= len(heap):
            return
    
        # For two children swap with the larger one
        if child_index + 1 < len(heap) and heap[child_index] < heap[child_index + 1]:
            child_index += 1
    
        # If the child node is smaller than the current node, swap them
        if heap[child_index] > heap[index]:
            self.swap(heap, child_index, index)
            self.top_down(heap, child_index)
    
    # This is a private function used for traversing up the tree and ensuring that heap is in order
    def bottom_up(self, heap, index):
        # Finding the root of the element
        root_index = (index - 1) // 2
        # If we are already at the root node return nothing
        if root_index < 0:
            return
    
        # If the current node is greater than the root node, swap them
        if heap[index] > heap[root_index]:
            self.swap(heap, index,root_index)
        # Again call bottom_up to ensure the heap is in order
            self.bottom_up(heap, root_index)
    
    def reheap(self, newQuery, wpi):
        #reinitializing priority queue
        return webpagePriorityQueue(wpi, newQuery)

if __name__ == '__main__': 
    wpi = [
    webPageIndex.WebPageIndex('data/doc3-binarysearchtree.txt'),
    webPageIndex.WebPageIndex('data/doc1-arraylist.txt'), 
    webPageIndex.WebPageIndex('data/doc2-graph.txt'), 
    webPageIndex.WebPageIndex('data/doc4-stack.txt'),
    ]
    wpq = webpagePriorityQueue(wpi, 'data structure')
    print(wpq.heap)
    print(wpq.peek())
    print("remove: ", wpq.poll())
    print('after remove: ', wpq.heap)
    wpq = wpq.reheap('in', wpi)
    print("after reheap: ", wpq.heap)