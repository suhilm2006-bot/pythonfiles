'''print((30+6)//(3+10)+(10+2))
print((45+7)+(90*2)/(0+56))




age = 20

if age >=18:
    print("adult")
else:
    print("bts")
    



name = input("enter your name")
if name == "karthik":
    print("bts karthik")
else:
    print("karthik bts")
    
    
    
fruits = ["apple","bananna","mango","grapes"]

print(fruits[0])
print(fruits[1])

name = ["rahul","sumith","kathik","tousif"]

print(name[3])
print(name[1])

fruits = ["apple","bananna","mango","grapes"]

print(fruits[-1]) # grapes
print(fruits[-2]) # mango

numbers = [1,2,3,4,5,6,7,8,9]

print(numbers[0:5])

names = ["karthik","tousif"]
names.append("sneha")
names.insert(1,"priya")
names.remove("tousif")

print(names)

num =[1,10,8]
num.sort()
print(num)
numbers = [30,10,20]

numbers.sort()
numbers.reverse()
last = numbers.pop()
print(numbers)
print(last)

numbers = [20,15]
sum = numbers[0] - numbers[1]
print(sum)
names = ["asha","ravi","priya","neha"]
print = (names)
empty = set() 

student = {
    "name": "asha",
    "age":20,
    "marks":85
    
    
}
print(student["name"])


student = {"name":"kathik","marks":34}

student["marks"]=90
student["cuty"]="bangaluru"

print(student)
a = 10
b = 20
c = 30

sum = a + b + c

print("Sum =", sum)

numbers = [10, 20, 30]

print(numbers)
student = {
    "name": "suhil akthar ",
    "age": 21,
    "course": "B.Tech",
    "branch": "EEE",
    "year": 3
}

print(student)

numbers = [50, 20, 40, 10, 30]

numbers.sort()

print(numbers)


numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

class student: 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 
    
student1 = student("suhail", 80 )
student2 = student("karthik", 85 )
student3 = student("tousif", 100)

print(student1.name)
print(student1.marks)
print(student2.name)
print(student2.marks)
print(student3.name)
print(student3.marks)

class student:
    def study(self):
        print("student is studying")
s1 = student()
s1.study()


class Dog:
    def sound(self):
        print("bark")
        
class cat:
    def sound(self):
        print("meow")
        
class cow:
    def sound(self)    :
        print("moow")
        
class crow:
    def sound(self):
        print("ka   ka")
        
    
Dog().sound()
cat().sound()
cow().sound()
crow().sound()

class  BankAccount:
    def __init__(self, owner, balance=1110):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, 500):
        self.balance += amount
        
    def withdrow(self, 400                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ):
        if amount <= self.balance:
            self.balance -= amount
            
    def show_balance(self):
        print(self.balance)
        
        
list = [1, 25, 37, 4, 90]

print(list[-1])    
print(list[0])
print(list[-2])
print(list[-4])

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
    
    
numbers = [10,20,30,40,50]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
        
print(largest)



numbers = [1,2,5,8,9]
smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n
        
print(smallest)'



numbers = [1,2,3,4,5,6,9]

target = 9

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index", i)
    else:
        print("numbers not foundf")


arr = [10, 20, 30, 40, 50, 60, 70]

target = 60

low = 0
high = len(arr) - 1

while low <= high:
    middle = (low + high) // 2

    if arr[middle] == target:
        print("Target found at index:", middle)
        break

    elif target > arr[middle]:
        low = middle + 1

    else:
        high = middle - 1
        
number = [10,20,30,40,50]
target = 40
middel = 30
for i in range(len(number)):
    if i< middel:
        if number("number found at index",i)
        
    else:
        print("number not found")
        
#1>   
numbers = [10, 15, 20, 25, 30, 35, 40]

for num in numbers:
    if num % 2 == 0:
        #print(num)
        
#2>
numbers = [10, 20, 30, 40, 50, 60, 70]

numbers.insert(4, 45)
numbers.insert(6, 65)

print(numbers)

#3>
numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print(numbers)

#4>
student = {
    "name": "Tousif"
    "age": 21
    "course": "B.Tech"
}

print(student)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
numbers = [5,3,6,4,2,]
bubble_sort(numbers)
print(numbers)


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = 3
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = 1
                arr[1], arr[min_index] = arr [min_index], arr[i]
                
                
numbers = [1,2,5,4,8]
selection_sort(numbers)
print(numbers)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j-=1
        arr[j+1] = key 
        
numbers = [5,6,8,4,2,7]
insertion_sort(numbers)
print(numbers)


#1
numbers = [1,2,5,8,9]
smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n
        
print(smallest)

#2
numbers = [10, 20, 30, 40, 50]
target = 30

for i in range(len(numbers)):
    if numbers[i] == target:
        print("numbers found at index", i)
        break
else:
    print("numbers not found")
 
 #3  
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
numbers = [5,3,6,4,2,]
bubble_sort(numbers)
print(numbers)''

#4
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = 3
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = 1
                arr[1], arr[min_index] = arr [min_index], arr[i]
                
                
numbers = [1,2,5,4,8]
selection_sort(numbers)
print(numbers)

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

item = stack.pop() 
print(item)
print(stack)

queue = []

queue.append("asha")
queue.append("ravi")
queue.append("virat")

person = queue.pop(0)

print(person)
print(queue)'''


# LAP YEAR
'''
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


#swipe a number 
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

#simple calculater
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)


numbers = [10, 20, 5, 40, 30]

largest = numbers[0]
second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest number =", second)


# Program to check whether a year is a leap year or not

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
    
# Program to swap two values without using a third variable

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
'
n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()'
    
numbers = [10, 20, 50, 30, 40]

largest = numbers[0]
second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest number is:", second)''

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequency:", frequency)

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


# Create an object
calc = Calculator()

# Demonstrate all operations
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))

#1

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for num in numbers:
    if num % 2 == 0:
        print(num)
        
#2
numbers = [1,2,5,8,9]
smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n
        
print(smallest)    

#take a number  and divisor as the input and check if it is divisible by the divisor

number = int(input("Enter a number: "))
divisor = int(input("Enter the divisor: "))

if number % divisor == 0:
    print("The number is divisible by the divisor.")
else:
    print("The number is not divisible by the divisor.")
    
#revers a list of number from 1 to 20#
numbers = list(range(1, 21))

numbers.reverse()

print(numbers)    

#take a number as input and check if it is prime 
num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")'
        
#write a program to find positive number in a list of integers list 

numbers = [10, -5, 3, -7 , 0, -2, 8]

for num in numbers:
    if num > 0:
        print(num)

#list = [100,-5,32,-100,750,0,-2,81]
#find the count of number greater than 10 in the list

list = [100, -5, 32, -100, 750, 0, -2, 81]

count = 0

for num in list:
    if num > 10:
        count = count + 1

print("Count =", count)

#creat a list of 10 elements and find the average of its elements 

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

total = sum(numbers)
average = total / len(numbers)

print("Average =", average)

#creat a list 10 element and seperate it as even and odd numbers

numbers = [10, 15, 22, 33, 40, 51, 62, 73, 84, 95]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)

#creat a list of 10 elements and seperate it as even number and creat a list with thos even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Original list:", numbers)
print("Even numbers:", even_numbers)


#list [10,23,33,40,58,67,72,81,98,100]   replace the value 72 by 75 in this list

list1 = [10, 23, 33, 40, 58, 67, 72, 81, 98, 100]
list1[6] = 75

print(list1)

#consider a string "hello world" and write a python function that reaverse the string and returns it 
def reverse_string(text):
    return text[::-1]

string = "hello world"

result = reverse_string(string)

print(result)

#consider a string "artificialintelligence" and count the numbers os character in the string
string = "artificialintelligence"

count = len(string)

print("Number of characters:", count)

#take the input from the user and perfron sum of 2 number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)


#creat a list and perfrom insert(), append(), remove(),operation on it

my_list = [10, 20, 30, 40]

print("Original list:", my_list)

# append()
my_list.append(50)
print("After append:", my_list)

# insert()
my_list.insert(2, 25)
print("After insert:", my_list)

# remove()
my_list.remove(30)
print("After remove:", my_list)


# creat dirctionary and perform add, update, and delete operation on it
student = {
    "name": "Manoj",
    "age": 21,
    "course": "B.Tech"
}

print("Original dictionary:", student)

# Add
student["city"] = "Ballari"
print("After adding:", student)

# Update
student["age"] = 22
print("After updating:", student)

# Delete
del student["city"]
print("After deleting:", student)




#take the input from the user and build a calculater , list1=[10,30,48,867,88,86] list2=[48,86,78,45,885]find duplicate values

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result =", num1 + num2)
elif choice == 2:
    print("Result =", num1 - num2)
elif choice == 3:
    print("Result =", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")'''
    
    
    
# creat a mew list that contains only the non-zero element (input:[5,0,6,2,0,7,0,0,0,0])
    
numbers = [5, 0, 6, 2, 0, 7, 0, 0, 0, 0]

non_zero = [x for x in numbers if x != 0]

print(non_zero)




#seperate even and odd numbers into two different list  (input: [-2,5,-7,8,-1,0])

numbers = [-2, 5, -7, 8, -1, 0]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)


# sort the list in ascending order  (input: [10,50,28,5,80])

numbers = [10, 50, 28, 5, 80]

numbers.sort()

print("Ascending order:", numbers)                                                                                                                                                                                                                                                                          