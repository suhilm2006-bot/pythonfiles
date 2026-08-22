#suhil m
#KUB25EEE684
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
    print("The number is not divisible by 3.")
    
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

#16)take 2 num as input from user and if it divisible by 5 square the number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 5 == 0:
    print(num1 * num1)

if num2 % 5 == 0:
    print(num2 * num2)


#17) [10,3,5,6,7,8,9,24,3,5,6,7,89] find the prime number even number and odd numbers
numbers = [10,3,5,6,7,8,9,24,3,5,6,7,89]

prime = []
even = []
odd = []

for n in numbers:
    # Check even and odd
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

    # Check prime
    if n > 1:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1

        if count == 2:
            prime.append(n)

print("Prime numbers:", prime)
print("Even numbers:", even)
print("Odd numbers:", odd)
#18)[-1, 3, 34, -8, -9,-1]remove negative numbers and numbers divisible by 3

numbers = [-1, 3, 34, -8, -9, -1]

result = []

for num in numbers:
    if num >= 0 and num % 3 != 0:
        result.append(num)

print(result)'

#19)1, 2,3, 4, 5, 6, 7, 8, 9]find the average sum count of list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = sum(numbers)
count = len(numbers)
average = total / count

print("Sum:", total)
print("Count:", count)
print("Average:", average)


#20)take the divisors from 1 to 10 and check 1578693 is divisible or not if divisible -100 from it

num = 1578693

for i in range(1, 11):
    if num % i == 0:
        num = num - 100
        print(i, "Divisible")
    else:
        print(i, "Not divisible")

print("Final number:", num)


#21)"univesity"count vowels in it

word = "univesity"

count = 0

for ch in word:
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)'''

#22)[10,3,5,6,7,8,9,24,3,5,6,7,89] print 89 using index and add 59 to the list in 9th index

"""numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# Print 89 using index
print(numbers[12])

# Add 59 at 9th index
numbers.insert(9, 59)

print(numbers)"""

#23)[-1,3,34,-8,-9,1] square elements of the list  

"""numbers = [-1, 3, 34, -8, -9, 1]

result = [x ** 2 for x in numbers]

print(result)"""


#24)take 2 numbers as input and 2 floor division 

"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a // b

print("Floor division:", result)"""

#25)[10,3,5,6,7,8,9,24,3,5,6,7,89,7,8,54,621,57,24,3,5,6,4,] fine unique values 

"""numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89, 7, 8, 54, 621, 57, 24, 3, 5, 6, 4]

unique = list(dict.fromkeys(numbers))

print(unique)"""