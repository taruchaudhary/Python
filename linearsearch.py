def linear_Search(list1, n, key):   
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
  
list1 = [1 ,3, 5, 4, 7, 9]  
key = 7  
  
n = len(list1)  
a = linear_Search(list1, n, key)  
if(a == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ",a) 