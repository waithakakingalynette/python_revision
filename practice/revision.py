# Find the sum of two values
def find_sum(num):
    sum=0
    for i in num:
        sum+=i
    return sum  

# write a python function that takes a list and returns a new list with distinct 
# elements from the first list.   
def distinct_list(fruits):
    emptylist=[]
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    # num=[1,2,3,3,3,4,5,5,6,7,8]
    for i in fruits:
        if i not in emptylist:
            emptylist.append(i)
    return emptylist      

# Write a python program that accepts a string and counts the number of 
# uppercase and lowercase letters.             

def count_upper_and_lowercase(values):
    count_upper=0
    count_lower=0
    for i in values:
        if i.isupper():
            count_upper+=1
        elif i.islower():
            count_lower+=1
    return count_upper,count_lower 

# Write a Python function that takes a number as a parameter and checks whether 
# the number is prime or not.           
# def is_prime(num):
#      if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

def is_palindrome(str):
    return str==str[:: -1]    


# Finding vowels.
def get_vowels(string):
    vowels = []
    for char in string:
        if char in "aeiouAEIOU":
            vowels.append(char)
    return vowels

string = "Hello World"
vowels = get_vowels(string)
print(vowels)



# Write a python program that has a list days = [ “Monday”, “Tuesday”, “Friday”, “Monday”] and counts the number occurrences of Monday

days = ["Monday", "Tuesday", "Friday", "Monday"]
count = 0
for day in days:
    if day == "Monday":
        count += 1
print(count)  


days = ["Monday", "Tuesday", "Friday", "Monday"]
 count = days.count("Monday")
print(count)  



days = ["Monday", "Tuesday", "Friday", "Monday"]

 count = days.count("Monday")

 print(count) 
 print(count) 


days = ["Monday", "Tuesday", "Friday", "Monday"]
count = len([day for day in days if day == "Monday"])
print(count)  


days = ["Monday", "Tuesday", "Friday", "Monday"]
count = 0
i = 0
while i < len(days):
    if days[i] == "Monday":
        count += 1
    i += 1
print(count)

# Write a Python function named smallest that accepts a list of unsorted integers and returns the smallest number in the list. Example:
# smallest([3,6,8,2,4,1,5,7]) returns 1

def smallest(nums):
    return min(nums)

def smallest(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

 
def smallest(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return min(nums[0], smallest(nums[1:]))

def smallest(nums):
    min_num = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < min_num:
            min_num = nums[i]
    return min_num

# Write a python function named divisible_by_seven that; using the range function and a for loop returns a list containing all the numbers between 100 and 200 that are divisible by 7.

def divisible_by_seven():
    return [i for i in range(100, 201) if i % 7 == 0]

def divisible_by_seven():
    result = []
    for i in range(100, 201):
        if i % 7 == 0:
            result.append(i)
    return result

#5.Write a python program that takes two inputs(as integers) from a user and adds
#the 2 numbers, checks  if the sum is greater than than 10, less than 10 or equal 10 
#and prints a statement  after each check            

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_nums = num1 + num2


if sum_nums > 10:
    print("The sum of", num1, "and", num2, "is greater than 10.")
elif sum_nums < 10:
    print("The sum of", num1, "and", num2, "is less than 10.")

else:
    print("The sum of", num1, "and", num2, "is equal to 10.")


#  6.Write a python function that takes one argument which is a list,  a=[1,2,3,4,5] and returns    True if 4 is present in the list and False is 4 is not in the list

def check_for_4(a):
    if 4 in a:
        return True
    else:
        return False


# 7.Write a python function that takes one argument which is a list    
# fruits=["apples","grapes","pineapple"] and removes the last fruit  from the list then 
# returns the list without the removed fruit

def remove_last_fruit(fruits):
    fruits.pop()
    return fruits


def remove_last_fruit(fruits):
    new_list = []
    for i in range(len(fruits)-1):
        new_list.append(fruits[i])
    return new_list

#8.Write a python program that takes in a list of cars, cars = ['Ford', 'BMW', 'Volvo'] 
#and returns a sorted list 

cars = ['Ford', 'BMW', 'Volvo']

sorted_cars = sorted(cars)

print(sorted_cars)
