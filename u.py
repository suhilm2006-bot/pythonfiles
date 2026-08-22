'''
#1)[3,10,15,54,75,25,23] print number divisible by 3,5,8 if none print none

numbers = [3, 10, 15, 54, 75, 25, 23]

found = False

for num in numbers:
    if num % 3 == 0 or num % 5 == 0 or num % 8 == 0:
        print(num)
        found = True

if not found:
    print("None")
    
    
#2)[10,3,5,6,7,8,9,24,3,5,6,7,89] find the smallest and largest elements and swap them

numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

smallest = min(numbers)
largest = max(numbers)

small_index = numbers.index(smallest)
large_index = numbers.index(largest)

numbers[small_index], numbers[large_index] = numbers[large_index], numbers[small_index]

print("Smallest:", smallest)
print("Largest:", largest)
print("After swapping:", numbers)


#3)[-1,3,34,-8,-9,1] replace -1 by 100

numbers = [-1, 3, 34, -8, -9, 1]

numbers[numbers.index(-1)] = 100

print(numbers)

#4)[1,2,3,4] [3,4,5,6] find the average of 2 list
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

avg1 = sum(list1) / len(list1)
avg2 = sum(list2) / len(list2)

print("Average of list 1:", avg1)
print("Average of list 2:", avg2)

#5)take the number as input and add 5 if it is divisible by 3

num = int(input("Enter a number: "))

if num % 3 == 0:
    num = num + 5
    print(num)
else:
    print(num)
    
    
    
#6. [3, 10, 15, 54, 75, 25, 23] Numbers divisible by 3 but not 5  
numbers = [3, 10, 15, 54, 75, 25, 23]

for num in numbers:
    if num % 3 == 0 and num % 5 != 0:
        print(num)

#7. [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 8, 9]`1 Elements greater than 20

elements = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 8, 9]

for elem in elements:
    if elem > 20:
        print(elem)

#8. [-1, 3, 34, -8, -9, 1] Print only negative numbers python  
nums = [-1, 3, 34, -8, -9, 1]

for n in nums:
    if n < 0:
        print(n)

#9 [1, 2, 3, 4, 5, 6, 7, 8, 9]Find the count (length) of the list python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = len(my_list)
print("Count of list:", count)

#10. Input a number and multiply by 5 if divisible by 3 python

user_num = int(input("Enter a number: "))

if user_num % 3 == 0:
    result = user_num * 5
    print("Result:", result)
else:
    print("The number is not divisible by 3.")'''
    
#11)Take 2 numbers as input from user and check whether the sum is divisible by 5
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

if sum % 5 == 0:
    print("Sum is divisible by 5")
else:
    print("Sum is not divisible by 5")
    
#12)[10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]Find prime numbers from the list 
a = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

for num in a:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
#13)[-1, 3, 34, -8, -9, 1]Perform list operations on 
a = [-1, 3, 34, -8, -9, 1]

print("List:", a)
print("Length:", len(a))
print("Maximum:", max(a))
print("Minimum:", min(a))

a.append(10)
print("After append:", a)

a.remove(3)
print("After remove:", a)

a.sort()
print("After sorting:", a)

a.reverse()
print("After reverse:", a)


#14 [1, 2, 3, 4, 5, 6, 7, 8, 9]Find the average of the list 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

average = sum(a) / len(a)

print("Average =", average)

 
#15)Take the divisors from 1 to 10 and check whether 1578693 is divisible. If divisible, create a list of divisors that divide it
num = 1578693
divisors = []

for i in range(1, 11):
    if num % i == 0:
        divisors.append(i)

print("Divisors:", divisors)