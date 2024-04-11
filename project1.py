#Print Numbers from 1 to 10
for i in range(1, 11):
    print(i)

#Reverse a String by input your name
name = input("Enter your name: ")
reversed_name = ""
for i in range(len(name)-1, -1, -1):
    reversed_name += name[i]
print("Reversed name: " + reversed_name)

#Find the Largest and Smallest Number in a List [10, 20, 5, 40, 30, 72, 34]
numbers = [10, 20, 5, 40, 30, 72, 34]
min_num = min(numbers)
max_num = max(numbers)
print("Smallest number: " + str(min_num))
print("Largest number: " + str(max_num))


#Remove Duplicates from a List
numbers = [1, 2, 3, 4, 2, 3, 5, 6, 1]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Unique numbers: " + str(unique_numbers))






