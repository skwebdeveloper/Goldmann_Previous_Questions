# OPtimaized it via Map

def Counting(arr, n, sum):
    count = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i] + arr[j] == sum:
                count += 1
                j += 1
    return count               
    
arr = [1,1,1,1]
n = len(arr)
sum = 2
print(Counting(arr, n, sum))    

# ===============================================================================================
# STACK VIA ARRAY
# ===============================================================================================

from sys import maxsize 

def Stack_via_array():
    stack = []
    return stack

def Empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("Stack", item)

def pop(stack, item):
    if (Empty(stack)): 
        return str(-maxsize -1) # return minus infinite 
      
    return stack.pop()  
      
stack = Stack_via_array()
push(stack, str(12))
push(stack, str(23))
pop(stack, 12)    
push(stack, str(30))


# ===============================================================================================
# Repeating number 
# ===============================================================================================


def Repeating(arr, size):
    mp = {}
    for i in range(size):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        mp[arr[i]] += 1
    
    
    for i in mp:
        if mp[i] == 1:
            print(i)        

arr = [9,4,6,9,4,2]
size = len(arr)
Repeating(arr, size)

# ===============================================================================================
# Smallest subarray with sum equal
# ===============================================================================================


def Smallest(arr, sum, size):
    max_so_far = 0 
    for i in range(size-1):
        if arr[i] == sum:
            print(arr[i])
        else:
            max_so_far = max_so_far + arr[i]
            if max_so_far > sum:
                    print(max_so_far)
            else:
                i += 1    
        

arr = [1,10,5,2,7]
sum = 9
size = len(arr)
Smallest(arr, sum, size)


# ===============================================================================================
# Sort 0 and 1 
# ===============================================================================================


def Sorting(arr, n):
    count0 = 0
    count1 = 0
    for i in range(0, n):
        if arr[i] == 0:
            count0 += 1      
        if arr[i] == 1:
            count1 += 1
    for i in range(0, count0):
        arr[i] = 0
    for i in range(count1, n):
        arr[i] = 1                
    return 

def printing(arr, n):
    for i in range(0,n):
        print(arr[i], " ", end = " ")
    print()    

  
arr = [1,1,1,1]
n = len(arr)
Sorting(arr, n)    
printing(arr,n)


# ===============================================================================================
# Two arrays are equal or not 
# ===============================================================================================


def equal(arr1,arr2,n1,n2):
    if n1 != n2:
        return
    else:
        while(n1 > 0):
            i = arr1[0]
            j = arr2[0]
            if i == j:
                i += 1
                j += 1
                return 1
            else:
                return 0      
        
               
arr1 = [1,2,5,4,0]
arr2 = [2,4,5,0,1]
arr1.sort()
arr2.sort()
n1 = len(arr1)
n2 = len(arr2)
print(equal(arr1, arr2, n1, n2))   


# ===============================================================================================
# Smallest and Second Smallest element in an array 
# ===============================================================================================




def Smallest(arr, n):
    if len(arr) < 2:
        print("-1")
        return 
    for i in range(0, n-1):
        j = i + 1
        if arr[i] == arr[j] and len(arr) > 2:
            i += 1
            j += 1
            print(arr[i], ' ', arr[j])
            return
        else:
            print(arr[i], ' ', arr[j])  
            return      
    

arr = [1,1,23,45,67,45,89,34,87,999,343,578,34546,34567,56789,3456783456789,2]
n = len(arr)
arr.sort()
Smallest(arr,n)    



# ===============================================================================================
# DO it Properly 
# ===============================================================================================

def Ugly_number(n):
    print(1, " ", end= '')
    for i in range(1,n):
            if i%2 == 0 or i%3 == 0 or i%5 == 0:
                    print(i, " ", end=" ")
                    i += 1                
                    
n = 150
Ugly_number(n)




# ===============================================================================================
# Stock buy and sell 
# ===============================================================================================

def Stock_and_sell(arr, n):
      if n == 1:
          break
    i = 0
    while (i < n-1):
        while(i < n-1 and arr[i] > arr[i+1]):
            i += 1
        if i == n-1:
            break    
        buy = arr[i]
        i += 1
        while(i < n and arr[i] > arr[i-1]):
            i += 1
        sell = arr[i - 1]
        print("But at = ",buy,"Sell at = ", sell)        
    
arr = [100,180,260,310,40,535,695]
n = len(arr)
Stock_and_sell(arr, n)
    

# ===============================================================================================
# Wave Array
# ===============================================================================================

def wave_array(arr, n):
    for i in range(0, n, 2):
        if(i>0 and arr[i] < arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]
        if(i<n-1 and arr[i] < arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]   
            
arr = [10, 90, 49, 2, 1, 5, 23]
n = len(arr)
wave_array(arr, n)
for i in range(n):
    print(arr[i], " ", end = "")



# ===============================================================================================
# Bitonic Array
# ===============================================================================================

def bitonic(arr, n):
    if n is None:
        return 0 
    for i in range(n-1):
        j = i + 1
        if arr[i] < arr[j]:
            i += 1
        else:
            print(arr[i])    
            return 

arr = [-3, -2, 4, 6, 10, 8, 7, 1]
n = len(arr)
bitonic(arr, n)

# Better Approach
# O(logn)


def Better_bitonic(arr, left, right):
    if(left < right):
        mid = left + right // 2
        if(arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]):
            return mid
        if(arr[mid] < arr[mid+1]):
            return Better_bitonic(arr, mid+1, right)
        else:
            return Better_bitonic(arr, left, mid-1)


arr = [-3, -2, 4, 6, 10, 8, 7, 1]
n = len(arr)
Better_bitonic(arr, 1, n-2)



# ===============================================================================================
# Count subarray having product equal K
# ===============================================================================================

def counting(arr, n, k):
    count = 0
    for i in range(0, n):
        if arr[i] <= k:
            count += 1 
        max = arr[i]
        for j in range(i+1, n):
            max = max*arr[j]
            if max < k:
                count += 1 
            else:
                break            
    return count       

arr = [1,2,3,4]
k = 10
n = len(arr)
print(counting(arr, n,k))



# ===============================================================================================
# Merge without extra space
# ===============================================================================================


def Merge(arr1, arr2, m, n):
    for i in range(n-1,-1,-1):
        last = arr1[m-1]
        j = m-2
        while(j >= 0 and arr1[j] > arr2[i]):
            arr1[j+1] = arr1[j]
            j -= 1
        if(j != m-2 or last > arr2[i]):
            arr1[j+1] = arr2[i]
            arr2[i] = last     

arr1 = [1,5,9,10,15,20]
arr2 = [2,3,8,13]
m = len(arr1)
n = len(arr2)
Merge(arr1, arr2, m, n)
print("First array")  
for i in range(m):  
    print(arr1[i], " ", end = " ")
print("\n")
print("Second array")    
for i in range(n):
    print(arr2[i], " ", end = " ")    

