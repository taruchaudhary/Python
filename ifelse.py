age = int(input("enter age: "))
if age>=18:
    print("valid for vote")
else:
    print("not valid for vote")
if age>1 and age<=10:
    print("small kid")
elif age>10 and age<=20:
    print("school going")
elif age>20:
    print("adult")


