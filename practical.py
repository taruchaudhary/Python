list1=[10,24,7,54,34,99,21] 

maxn=0

for i in list1:

    if(i>maxn):

        maxn=i
print("Maximum Number using loop is:", maxn)
print("Maximum number using function:",max(list1))