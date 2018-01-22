## 1) Using a for loop, write a program that prints out the decimal equivalents of 1/2,1/3,1/4,...,1/10.

print("Problem 1")
for i in range(2, 11):
    print(1/i)

## 2) Write code that prints out the odd numbers 1 through 20. Bonus: Use list comprehension

print("Problem 2")
[print(i) for i in range(1, 20, 2)]

## 3) Write a function to reverse a string. The string can be of any length and might be empty. Use the function to print a reverse version of your name

print("Problem 3")
def str_rev(input_str):
    return input_str[::-1]

print(str_rev("Dennis"))

## 4) Find the bugs

print("Problem 4")

def negate(num):
    return -num

def large_num(num):
    res = (num > 10000)
    return res

b = 50
neg_b = negate(b)
print("b:", b, "neg_b:", neg_b)
big = large_num(b)
print("b is big:", big)
