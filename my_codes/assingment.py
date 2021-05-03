"""What are the default data types in python? What is typecasting in python?
Give two examples each of typecasting between each of the following types:
a. string to boolean
b. integer to boolean
c. boolean to string
d. string to integer"""

# Datatype in Python.  
"""4 basic datatypes: integer/number, string/text, float/decimals, boolean/true and false
integer: int
float: float 
boolean: bool 
string: str"""

# Typecasting in pyhton
"""The process of converting the value of one data type (integer, string, float, etc.) to another data type is
called type conversion or type casting."""
 
# Two examples each of typecasting between each of the following types:

# a. string to boolean
#example 1
pr = "True"
print(pr, type(pr))
pr = bool(pr)
print(pr, type(pr))

# example 2
pr = "Hello"
print(pr, type(pr))
pr = bool(pr)
print(pr, type(pr))


# b. integer to boolean
# example 1
pr = 5
print(pr, type(pr))
pr = bool(pr)
print(pr, type(pr))

# example 2
pr = 105
print(pr, type(pr))
pr = bool(pr)
print(pr, type(pr))

#c. boolean to string
# example 1
pr = True
print(pr, type(pr))
pr = str(pr)
print(pr, type(pr))

# example 2
pr = false
print(pr, type(pr))
pr = str(pr)
print(pr, type(pr))
 
#d. string to integer
# example 1
pr = "2134942034"
print(pr, type(pr))
pr = int(pr)
print(pr, type(pr))

# example 2
pr = "123"
print(pr, type(pr))
pr = int(pr)
print(pr, type(pr))
