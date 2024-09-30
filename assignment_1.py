#!/usr/bin/env python
# coding: utf-8

# Assignment 1

# ![Screenshot%202024-09-30%20103304.png](attachment:Screenshot%202024-09-30%20103304.png)

# In[1]:


a = "HELLO , PYTHON WORLD" 
print(a)


# Part 2: Basic Python Syntax
# 
# String Operations
# #.  Write a Python program that takes a user's first and last name as input and prints them in reverse order with a space between them

# In[15]:


# taking a user first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Printing the names in reverse order
print(f"{last_name} {first_name}")


# #.  Use at least two string methods and explain their purpose in the comments.

# In[3]:


full_name = input("Enter your full name: ").strip()  


full_name = full_name.replace(" ", "_")  # Replaces all spaces with underscores
full_name = full_name.upper()  # Converts all characters in the name to uppercase


print(f"Modified name: {full_name}")


# # Numeric Data Types and Conversion Functions

# # Write a Python program that takes an input number from the user, converts it to different numeric data types (integer, float, and complex), and displays the converted values. 

# In[4]:


user_input = input("Enter a number: ")

# Converting the input to different numeric data types
integer_value = int(float(user_input))  
float_value = float(user_input)         
complex_value = complex(user_input)     

# Displaying the converted values
print(f"Integer value: {integer_value}")
print(f"Float value: {float_value}")
print(f"Complex value: {complex_value}")


# # . Explain the difference between these data types in comments.

# Integer (int): Used for whole numbers without a fractional part.
# 
# Float (float): Used for numbers with decimal points .
# 
# Complex (complex): Used for numbers with both a real and an imaginary component.

# Simple Input and Output
# 
# Create a Python script that calculates the area of a rectangle. The script should:
# 
# Prompt the user to enter the length and width of the rectangle.
# 
# Calculate the area.
# 
# Display the result using the print function.

# In[5]:


# the user to enter the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))  
width = float(input("Enter the width of the rectangle: "))    

# Calculating the area of the rectangle
area = length * width 

# Displaying the result using the print function
print(f"The area of the rectangle is: {area}")


# Using the format Method
# 
# 

# #. Modify the rectangle area program to format the output so that it displays the area with two decimal places.

# In[6]:


#  the user to enter the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))  
width = float(input("Enter the width of the rectangle: "))    

# Calculating the area of the rectangle
area = length * width  # using formula

# Displaying the result with two decimal places
print(f"The area of the rectangle is: {area:.2f}")


# The % Method and print Function
# #. Write a Python script that takes three numbers as input and prints their average using the % method for string formatting.
# 

# In[7]:


# Taking three numbers as input from the user
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))  

# Calculating the average of the three numbers
average = (num1 + num2 + num3) / 3

# Printing the average using the % method for string formatting
print("The average of the three numbers is: %.2f" % average)


# Part 3: Language Components
# Control Flow (if Statements and Loops)
# 

# 
# #. Write a Python program that asks the user for a number and determines whether it is positive, negative, or zero.

# In[9]:


# Asking the user for a number
number = float(input("Enter a number: ")) 

# Determining whether the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# #. Implement a loop that continues to ask the user for a number until they enter 'exit'.

# In[10]:


while True:
    # Asking the user for input
    user_input = input("Enter a number (or type 'exit' to quit): ")

    # Checking if the user wants to exit
    if user_input.lower() == 'exit':  
        print("Exiting the program.")
        break

    try:
        # Converting input to a float and determining if it is positive, negative, or zero
        number = float(user_input)

        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number or type 'exit' to quit.")


# # .  Use break to exit the loop and continue to prompt for a new number if the input is not 'exit'.

# Relational and Logical Operators
# 
# #. 
# Create a Python script that takes two numbers as input and prints whether both numbers are even, odd, or one of each using relational and logical operators
# .

# In[12]:


# Taking two numbers as input from the user
num1 = int(input("Enter the first number: "))  
num2 = int(input("Enter the second number: ")) 

# Using logical AND operator to check if both are even
if num1 % 2 == 0 and num2 % 2 == 0:  
    print("Both numbers are even.")

# Using logical AND operator to check if both are odd
elif num1 % 2 != 0 and num2 % 2 != 0:  
    print("Both numbers are odd.")

# Checking if one number is even and the other is odd
else:
    print("One number is even, and the other is odd.")


# For Loop and Bitwise Operators
# 
# #. Write a Python program that takes an integer input and prints its binary, octal, and hexadecimal equivalents using a for loop and bitwise operators
# 

# In[13]:


# Function to convert integer to binary using bitwise operators
def to_binary(n):
    if n == 0:
        return '0'
    binary_str = ''
    while n > 0:
        binary_str = str(n & 1) + binary_str
        n = n >> 1
    return binary_str

# Function to convert integer to octal using bitwise operators
def to_octal(n):
    if n == 0:
        return '0'
    octal_str = ''
    while n > 0:
        octal_str = str(n & 7) + octal_str
        n = n >> 3
    return octal_str

# Function to convert integer to hexadecimal using bitwise operators
def to_hexadecimal(n):
    if n == 0:
        return '0'
    hex_digits = '0123456789ABCDEF'
    hexadecimal_str = ''
    while n > 0:
        hexadecimal_str = hex_digits[n & 15] + hexadecimal_str
        n = n >> 4
    return hexadecimal_str

# Taking an integer input from the user
number = int(input("Enter an integer: "))

# Converting the number to binary, octal, and hexadecimal
binary_equivalent = to_binary(number)
octal_equivalent = to_octal(number)
hexadecimal_equivalent = to_hexadecimal(number)

# Printing the results
print(f"Binary equivalent: {binary_equivalent}")
print(f"Octal equivalent: {octal_equivalent}")
print(f"Hexadecimal equivalent: {hexadecimal_equivalent}")

