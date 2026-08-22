'''#1)[10,3,5,6,7,8,9,24,3,5,6,7,89] find even number and store it in new list


numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

#2)Consider a string "university"and reverse it without using ::-1


text = "university"

reverse = ""

for i in range(len(text) - 1, -1, -1):
    reverse = reverse + text[i]

print(reverse)

#3)[10,3,5,6,7,8,9,24,3,5,6,7,89]find the average of the list of element

numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)

print("Average =", average)

#4)[-1,3,34,-8,-9,1]find the smallest number

numbers = [-1, 3, 34, -8, -9, 1]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number =", smallest)


#5)[1,2,3,4] [3,4,5,6] [4,5,6,7]find common elementin 3list

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]

common = []

for num in list1:
    if num in list2 and num in list3:
        common.append(num)

print(common)


#6)[3,10,12,54,75,25,23]print the number not divisible by 3


numbers = [3, 10, 12, 54, 75, 25, 23]

for num in numbers:
    if num % 3 != 0:
        print(num)
        
#7)Consider a string "university"and count the character

text = "university"

print(len(text))

#8)[10,3,5,6,7,8,9,24,3,5,6,7,89]find the second smallest number

numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Second smallest number:", unique_numbers[1]

#9)[-1,3,34,-8,-9,1]swap only the frist and last elements

numbers = [-1, 3, 34, -8, -9, 1]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

#10)[1,2,3,4] [3,4,5,6]find repeating values in both the list

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for num in list1:
    if num in list2:
        common.append(num)

print(common)
#11)[3,10,12,54,75,25,23]print the number not divisible by 3 and 5

numbers = [3, 10, 12, 54, 75, 25, 23]

for num in numbers:
    if num % 3 != 0 and num % 5 != 0:
        print(num)
        
#12)[10,3,5,6,7,8,9,24,3,5,6,7,89]find the smallest and largest element

numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

print("Smallest:", min(numbers))
print("Largest:", max(numbers))

#13)[-1,3,34,-8,-9,1]swap only the frist and third elements

numbers = [-1, 3, 34, -8, -9, 1]

numbers[0], numbers[2] = numbers[2], numbers[0]

print(numbers)

#14)[1,2,3,4] [3,4,5,6]find repeating values in both the list

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = []

for num in list1:
    if num not in list2:
        result.append(num)

for num in list2:
    if num not in list1:
        result.append(num)

print(result)

#15)take the number as input and square it if if divisible by 3

num = int(input("Enter a number: "))

if num % 3 == 0:
    print("Square:", num ** 2)
else:
    print("Number is not divisible by 3")'''
    