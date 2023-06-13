#Write a Python program that accepts the user's first and 
#last name and prints them in reverse order with a space between them.

# def names():
#     first_name='Lynette'
#     last_name='Kinga'
#     word=first_name+" "+last_name
#      word.reverse()
#     print(word)

#     word='Lynette Kinga'[::-1]
#     print(word)



#2.Write a Python program that accepts a sequence of comma-separated numbers 
#from the user and generates a list and a tuple of those numbers.
def a(list_numbers):
    return tuple(list_numbers)

    list_numbers=[10,20,30,40,50,60,70]
    list_tuples=input("10","20","30","40","50","60","70")
    print(a(list_numbers))
    print(list_tuples)

# def b(i):
#     return tuple(i for i in list)

#     i=[1,2,3,4,5]
#     print(b(i))

#Write a Python program that prints long text, converts it to a list, 
#and prints all the words and the frequency of each word.

#Write a Python function that returns the Nth Fibonacci number.
# def solve(n):
#    if n <= 2:
#       return n - 1
#    else:
#       return solve(n - 1) + solve(n - 2)

# n = 8
# print(solve(n))
#Write a Python function that takes a list of numbers and returns the sum of all even numbers in the list.
# def even_numbers():
#         result = 0
#         for i in even_list:
#             if i % 2 == 0:
#                 result += i
#         return result        
#         even_list=[10,23,35,67,42,34,86,75]
#         even=even_numbers(even_list)
#          print(even_numbers)      
        # my_list = [1, 3, 5, 6, 8, 10, 34, 2, 0, 3]
        # even_list = filter(lambda x: x%2 == 0, my_list)  
        # sum (even_list)
#Write a Python function that takes two strings and returns True if they are anagrams, False otherwise.
# def str(a,b):
#         if(sorted(a)== sorted(b)):
#             print("true")
#         else:
#             print("false")
# a='i am able'
# b='able i am' 
# str(a,b)   
#Write a Python function that takes a string and returns the reverse of the string.
# def reverse_string(word):
#     word_list = list(word)
#     word_list.reverse()
#     reversed_word = "".join(word_list)
#     return reversed_word
 
    # reverse=word.list('').reverse('').join('')
    # text="Lynette"
    # reversed_string=reverse_string(word)
    # print(reversed_string)

#Write a Python function that takes a list of strings and returns the longest string in the list.
# def length():
#     text1="I am born of God"
#     text2="This is my dog"
#     if(text1== text):
#         return both
#          else:
#              text1
#Write a Python function that takes a list of integers and returns the second largest number in the list.
# def integers(num):
#     num=[1,23,3,45,35,79,67,89,100,34,56]
#     integers.sort(num)
#     print(num[-2])
#Write a Python function that takes a string and returns True if the string is a palindrome, False otherwise.
def is_palindrome(str):
    return str==str[:: -1]    

#Write a Python function that takes a list of integers and returns the sum of all the numbers in the list.
#Write a Python function that takes a list of numbers and returns the product of all the numbers in the list.
# Write a Python function that takes a list of strings and returns the number of strings in the list that contain the substring 'abc'.
# Write a Python function that takes a list of integers and returns the difference between the maximum and minimum numbers in the list.
# Write a Python function that takes a list of integers and returns a new list with only the even numbers from the original list.
# Write a Python function that takes a list of integers and returns a new list with only the odd numbers from the original list.
# Write a Python function that takes a list of strings and returns a new list with only the strings that start with the letter 'a'.
# Write a Python function that takes a list of strings and returns a new list with the strings sorted in alphabetical order.
# Write a Python function that takes a list of integers and returns a new list with the numbers sorted in descending order.
# Write a Python function that takes a list of integers and returns a new list with the numbers sorted in ascending order.
# Write a Python function that takes a list of strings and returns a new list with the strings sorted in reverse alphabetical order.
# Write a Python function that takes a list of integers and returns True if the list is sorted in ascending order, False otherwise.
# Write a Python function that takes a list of integers and returns True if the list is sorted in descending order, False otherwise.


# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 
def evenn_numbers():
    num=0
    while num<100:
        if num %2==0:
            print(num)
        num+=1
        continue    

# Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
# def prime_numbers():
#     num =1
#     for i in num<=10:
#         if i%2==0
#          print("not prime")  
#     else:
#         print("prime")    

# Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
# Write a function that takes any two integers as input, and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.

# python program that takes in a list and returns the list with the second item is removed.

# a=[2,4,6,8]
# def remove_digits(num):
#     a=num
#     a.remove(num[-2])
#     return num

def remove_second_digit(lst):
    # """
    # This function takes in a list and returns the list with the second digit removed from each element.
    # """
    new_lst = []
    for num in lst:
        num_str = str(num)
        if len(num_str) > 1:
            new_num_str = num_str[0] + num_str[2:]
            new_lst.append(int(new_num_str))
        else:
            new_lst.append(num)
    return new_lst


lst = [123, 456, 7890, 1, 23, 4]
new_lst = remove_second_digit(lst)
print(new_lst)

# Python program that calculates the ocurences of a days.
defr calculate_occurences(days):
    count=0
    for day in days:
        if day=="Monday"
        count+=1
    return count 

days=["Maonday","Tuesday","Friday","Monday"]
print(calculate_occurences(days))


class Products :
    def __init__(self,name,category,price,description):
        self.name=name
        self.category=category
        self.price=price
        self.description=description

    def add_to_cart(self,cart):
        cart.append(self)

    def remove_from_cart():
        cart.remove(self)
     
    def total_cost():
        return self.price *quantity
     