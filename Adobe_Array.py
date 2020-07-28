# ===========================================================================
# Sort an array 0,1,2
# ===========================================================================

# def sorting(arr, n):
#     count0 = 0
#     count1 = 0
#     count2 = 0
    
#     for i in range(n):
#         if arr[i] == 0:
#             count0 += 1
#         if arr[i] == 1:
#             count1 += 1 
#         if arr[i] == 2:
#             count2 += 1
                   
#     for i in range(0, count0):
#          arr[i] = 0
#     for i in range(count0, count0+count1):
#         arr[i] = 1 
#     for i in range(count0+count1 , n):
#         arr[i] = 2
#     return

# arr = [0,1,0]
# n = len(arr)
# sorting(arr, n)
# print("Counting 0 - 1 -2 number")
# for i in range(n):
#     print(arr[i], " ", end = " ")
    
# print("\n")    


# ===========================================================================
# Count pair with given sum
# ===========================================================================  



# def counting(arr,n, sum):
#     temp = sorted(arr)
#     print(temp)
#     print(n-1)
#     count = 0
#     i,j = 0, n-1
#     left = temp[i]
#     right = temp[j]
#     while i < j:
#         if (left + right) > sum:
#             j -= 1
#         elif (left + right) < sum:
#             i += 1
#         else:
#             i += 1
#             count += 1        
#     return count    

# arr = [1,5,1,7]
# n = len(arr)
# sum = 6
# print(counting(arr, n , sum))



# ===========================================================================
# Remove all duplicates   ---   Hash map
# ===========================================================================  


# geeksforgeeks => geksfor

# from collections import defaultdict

# def duplicate(arr, n):
#     io = []
#     for i in arr:
#         io.append(i[0])
#     print(io[0])    


# arr = ["geeksforgeeks"]
# n = len(arr)
# duplicate(arr, n)



# ===========================================================================
# Peak element -- O(logn)
# ===========================================================================  


# def peak(arr, low, high, n):
#     mid = (high + low)/ 2
#     mid = int(mid)
#     if((mid == 0) or (arr[mid-1] < arr[mid]) and  (arr[mid] > arr[mid + 1]) or (mid == n-1)):
#         return arr[mid]
    
#     elif((arr[mid] < arr[mid+1]) and mid > 0):
#         return peak(arr, (mid+1),high, n)
    
#     else:
#         return peak(arr, low, (mid-1), n)

# def util(arr, n):
#     return peak(arr, 0, n-1, n)      
                    
        
# arr = [1,3,20,4,1,0]
# n = len(arr)
# print(util(arr, n))

# ===========================================================================
# Rain water 
# ===========================================================================  





# ===========================================================================
# Product of maximum in first array and minimum in second 
# ===========================================================================  

# NAIVE APPROACH - O(nlogn)


# def pairing(arr1, arr2, n1, n2):
#     t1 = sorted(arr1)
#     t2 = sorted(arr2)
#     a = t1[n1-1]
#     b = t2[0]
#     return a*b
    
# arr1 = [1,4,2,3,10,2]
# arr2 = [4,2,6,5,2,9]
# n1 = len(arr1)
# n2 = len(arr2)
# print(pairing(arr1, arr2, n1, n2))

# OPTIMIZED - O(n)

# def pairing_opt(arr1, arr2, n1, n2):
#     i = 1
#     max = arr1[0]
#     min = arr2[0]
    
#     while(i < n1 and i < n2):
#         if arr1[i] > max:
#             max =  arr1[i]
#         if arr2[i] < min:
#             min = arr2[i]
       
#         i += 1
        
#     while i < n1:
#         if arr1[i] > max:
#             max = arr1[i]
#             i += 1
            
#     while i < n2:
#         if arr2[i] < min:
#             min = arr2[i]                         
#             i += 1 
        
#     return min*max


# arr1 = [10, 2, 3, 6, 4, 1]
# arr2 = [5, 1, 4, 2, 6, 9]
# n1 = len(arr1)
# n2 = len(arr2)
# print(pairing_opt(arr1, arr2, n1, n2))



# ===========================================================================
# Inversion of an array
# ===========================================================================  

# def Inversion(arr, n):
#     count = 0      
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i] > arr[j]:
#                 count += 1
#     return count            
        
# arr = [2,4,1,3,5]
# n = len(arr)
# print(Inversion(arr, n))

# OPTIMIZED

def temperory(arr, n):
    count = [0]*n
    return mergesort(arr,count, 0 ,n-1)



def mergesort(arr,count, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += mergesort(arr, count, left, mid)
        count += mergesort(arr, count, mid+1, n)
        count += merge(arr, count, left, right, mid)
    return count  
          
def merge(arr, temp_arr, left, mid, right): 
    i = left 
    j = mid + 1 
    k = left     
    count = 0
    while i <= mid and j <= right: 
        if arr[i] <= arr[j]: 
            temp_arr[k] = arr[i] 
            k += 1
            i += 1
        else: 
            temp_arr[k] = arr[j] 
            count += (mid-i + 1) 
            k += 1
            j += 1
    while i <= mid: 
        temp_arr[k] = arr[i] 
        k += 1
        i += 1
    while j <= right: 
        temp_arr[k] = arr[j] 
        k += 1
        j += 1
    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp_arr[loop_var] 
    return count 
  
arr = [2,4,1,3,5]
n = len(arr)
count = 0
temperory(arr,n)


# ===========================================================================
# Pascal's Triangle
# ===========================================================================  


# def pascal_triangle(n):
#     arr =[[0 for x in range(n)] for y in range(n)]
    
#     for level in range(0, n):
#         for i in range(0, level + 1):
#             if(i is 0 or i is level):
#                 arr[level][i] = 1
#                 # print(arr[level][i], " ", end = " ")
#             else:
#                 arr[level][i] = arr[level-1][i-1] + arr[level-1][i]
#                 # print(arr[level][i], " ", end = " ") 
#     print(arr[n-1])       
# n = 4
# pascal_triangle(n)




# ===========================================================================
# Equilibrium point
# ===========================================================================  

# def Equilibrium(arr, n):
#     left = 0
#     right = 0
#     i = 0
#     for i in range(0, n-1):
#         left = 0
#         right = 0
#         for j in range(i):
#             left += arr[j]
#         for j in range(i+1,n):
#             right += arr[j]
#         if left == right:
#             return i
#     return -1        
    
# arr = [-7,1,5,2,-4,3,0]
# n = len(arr)
# print(Equilibrium(arr, n))


# OPTIMIZED

# def Equilibrium(arr):
#     total = sum(arr)
#     leftsum = 0
#     for i, num in enumerate(arr):
#         total -= num
#         if leftsum == total:
#             return i
#         leftsum += num
#     return -1    
        

# arr = [-7,1,5,2,-4,3,0]
# print(Equilibrium(arr))


# ===========================================================================

# Missing number of an array
# ===========================================================================  


# def Missing(arr, n):
#     count = 1
#     listing = []
#     for i in arr:
#         listing.append(count)
#         count += 1
#     return listing[n-1]    


# def optimized(arr,n):
#     temp = sum(arr)
#     total = (n+1)*(n+2)/2
#     return int(total - temp)



# arr = [1,2,3,4,5,6,7,8,10]
# n = len(arr)
# print(Missing(arr, n))
# print(optimized(arr, n))


# ===========================================================================
# Bitonic
# ===========================================================================  

def Bitonic(arr, left, right):
    mid = (left + right) // 2
    
    while (left < right):
        if(arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]):
            return arr[mid]
        elif(arr[mid] < arr[mid-1]):
            return Bitonic(arr, left, mid)
        else:
            return Bitonic(arr, mid+1,right)    
    return -1





arr = [6,7,8,11,9,5,2,1]
n = len(arr)
print(Bitonic(arr,0, n-1))

