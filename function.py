def add(num1: int, num2: int):
    num3 = num1 + num2
    return num3
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
def swap(a,b):
    temp = a
    a = b
    b = temp
    return (a,b)
