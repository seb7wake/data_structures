import random
from time import process_time

#Linear search algorithm
def algorithmA(s, x):
    aList = []
    aList = s
    for i in range(len(aList)):
        #if list value is equal to target value
        if(aList[i] == x):
            return True
    return False

#Binary search algorithm
def algorithmB(s, x):
    aList = []
    aList = s
    low = 0
    high = len(aList) - 1
    mid = 0
    while low <= high: 
        mid = (high + low) // 2
        if s[mid] < x: 
             #mid value is less than target
            low = mid + 1
        elif s[mid] > x: 
            #mid value is greater than target
            high = mid - 1
        else: 
            #mid value is equal to target
            return True
    return False

#random even number generator function
def randomEvenNum(n):
    #getting random even number from 10 to n
    odd_rand_num = random.randrange(10,n,2)
    return odd_rand_num

#random odd number generator function
def randomOddNum(n):
    #random odd numbers from 11 to n
    odd_rand_num = random.randrange(11,n,2)
    return odd_rand_num

#heapsort helper function
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
        # Heapify the root. 
        heapify(arr, n, largest) 

#sorting function for algorithmB
def heapSort(arr): 
    n = len(arr) 
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0)
    return arr

#main function
def main():
    s = []
    targetValues = []
    for i in range(1000):
        #appending random even numbers to the s array
        s.append(randomEvenNum(1000))

    for n in range(146):
        #appending values within the s array as well as values not in s to the target value list
        if(n%2 == 0):
            #appending a value to the target values array that is within the s array
            targetValues.append(random.choice(s))
        else:
            #appending an odd number (won't be in the s array)
            targetValues.append(randomOddNum(1000))
    startTime1 = process_time() #starting timer
    for j in range(len(targetValues)):
        #calling algorithmA with every target value
        algorithmA(s, targetValues[j])
    endTime1 = process_time() # ending timer
    print("time elapsed for algorithmA:", endTime1-startTime1) #printing time elapsed
  
    startTime2 = process_time() #starting timer
    s = heapSort(s) #calling sort function to sort the s array for algorithmB
    for m in range(len(targetValues)):
        #calling algorithmB with every target value
        algorithmB(s, targetValues[m])
    endTime2 = process_time() #ending timer
    print("time elapsed for algorithmB:", endTime2-startTime2) #printing time elapsed
    # print(, algorithmB(s, 1))

if __name__ == '__main__':
    main()