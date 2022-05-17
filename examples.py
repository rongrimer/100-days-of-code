#Quiz 1 (section 1, question 1)
	#Running this will result in NameError
"""def a_function(a_parameter):    
    a_variable = 15    
    return a_parameter 
a_function(10)
print(a_variable)
"""



#Quiz 1 (section 1, question 4)
	#prints 15
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)



#Quiz 1 (section 1, question 4)
	#Question is: Given a Car Class has the following attributes and methods, 
	# which line of code in the answers will produce an error? Answer = C

#class car
#Methonds: drive() and break()
#Attributes: number_of_seats and speed

"""
A. car.drive()
B. car.num_of_seats = 2
C. car.break = 0
D. print(car.spe)
"""
#**Study more about Methods which are associated with objects (in OOP) and Functions are not.



#Quiz 1 (section 1, question 6)
	#What word would you use to describe my_toyota and my_fiat? Answer = C
"""
my_toyota = Car()
my_fiat = Car()
"""
"""
A. Class
B. Attribute
C. Object
D. Property
E. Method
"""


#Quiz 1 (section 1, question 8)
	#What is the output of this code? 
def foo(a, b=4, c=6):
    print(a, b, c)
 
foo(20, c=12)
#prints: 20, 4, 12


#Quiz 1 (section 1, question 9)
	#What is the output of this code? 
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)
#prints: 4 (7, 3, 0) {'x': 10, 'y': 64}


#Quiz 1 (section 1, question 10)
	#What's the print output for the following code? You do not need a computer to calculate this.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)
#prints: [5, 11, 37]
#Need to review this after going going through section 1/day 1