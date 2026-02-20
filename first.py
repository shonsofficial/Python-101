
age =25
print(age)

x =5**3 # exponential
print(x)

first_name ="Bro" # This is a variable that is a container for a value i.e string, integer, float, boolean. It behaves as if it were the actual value.
print(first_name)
print(f"Hello {first_name}") # this is a format string. it is used to print a variable with some text.

                     #FORMAT STRINGS EXAMPLES (They require double quotes)
food = "pizza"
print(f"You like {food}")

email = "bro123@fake.com"
print(f"Your email is: {email}")

                    #FORMAT INTEGERS EXAMPLES (These are whole numbers which can also be used in arithmetic expressions)
age = 25
print(f"You are {age} years old.")

quantity = 3
num_of_students = 30
print(f"You are buying {quantity} items for {num_of_students} people.")

                   # FORMAT FLOAT EXAMPLES (These contain a decimal part)
price = 10.99
print(f"The price is: ${price}")

gpa = 3.2
print(f"Your overall gpa score is {gpa}")

distance = 5.5
print(f"The total distance is {distance} km.")
                   # FORMAT BOOLEAN EXAMPLES (These are either true or false) NB: Always the first letter is capital.
is_student = True
print(f"Are you a student? : {is_student}")
#NB: Boolean statements are normally used when using if statements instead of printing output statements.
is_student = True
if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

for_sale = False
if for_sale:
    print("The commodity is for sale")
else:
    print("The commodity is NOT for sale")

is_online = True
if is_online:
    print("The user is online")    
else:
    print("The user is NOT online")    
                        #TYPE CASTING (This is the process of converting a variable from one data type to another)
name = "Bro Code"
age = 25
gpa = 3.2
is_student = True
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#Converting one data type to another
gpa = int(gpa)# converting float to integer
print(gpa)

age = float(age)# converting integer to float
print(age)

age = str(age)# converting integer to string
print(age)
print(type(age))
age+= "1"
print(age)

name = bool(name)# converting string to bool. If string is empty, you would get false. 
print(name)      # it can be used in program to check and see if someone enters their name or not.

                #USER INPUT(input() is a function that prompts the user to enter data then returns the data entered as a string)
input("What is your name?: ")
# You can assign the input function to a variable and print it.
name = input("What is your name?: ")
print(f"Hello {name}, i am very happy to meet you!")

age = int((input("How old are you?: ")))
print(f"Ohhh that's nice, You are {age} years old.")

                # CALCULATE THE AREA OF A RECTANGLE:
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area is {area} cm²")


               # CREATING A SHOPPING CART PROGRAM
item = input("What item would you like to purchase ?: ")
price = float(input("What is the price ?: "))
quantity = int(input("How many would you like ?: "))
total = price * quantity
print(f"You have bought {quantity} quantity(s) of {item}")
print(f"Your total is: ${total}")

               #CREATING A GAME OF MODULUS(It is a word game where you create a story by filling in blanks with random words.
                                          # (The aim of this game is to get familiar with user input)
adjective1 = input("Enter an adjective(descriptive word): ")
noun1 = input("Enter a noun(person,place,thing): ")
adjective2 = input("Enter an adjective(description): ")
verb1 = input("Enter a verb(word ending with 'ing'): ")
adjective3 = input("Enter an adjective(description): ")

print(f"Today i went to a {adjective1} bar.")
print(f"In an exibit, i saw a {noun1}.")
print(f"The {noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3}!!")

              # ARITHMETIC & MATH (These include arithmetic operators, math functions and exercises)
# e.g += -(augmented assignment operator), -=, *=, /=, **= -(augmented exponential), % -(modulus)

x =3.14 , y =4, z =5
round(x) # round function
abs(x)   # absolute function which is the distance away from zero as a whole number
pow(4,3) # power function
max(x,y,z) # maximum function
min(x,y,z) # minimum function

             #  CONSTANT AND FUNCTIONS
import math
print(math.pi)
print(math.e)

x = 9
result = math.sqrt(x)
print(result)

y = 1234.56789
print(math.ceil(y)) # round off upwards
print(math.floor(y)) # round off downwards


           #CIRCUMFRENCE OF A CIRCLE PROGRAM
import math
radius = float(input("Enter the radius of a circle: "))
circumfrence = 2 * math.pi * radius
print(f"The circumfrence of the circle is: {round(circumfrence,4)} cm")

           # CALCULATE THE AREA OF A CIRCLE
import math
radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area,4)} cm²")

          # CALCULATE THE HYPOTENUSE OF A RIGHT ANGLED TRIANGLE
import math
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt( pow(a,2) + pow(b,2))
print(f"The hypotenuse of the triangle is: {round(c,4)} cm")

           #IF STATEMENTS (They do some code if the condition is true or else they something else. NB: = is assignment operator and == is equals operator)
age = int(input("Enter your age: "))
if age >=100:
    print("You are too old to sign up.")
elif age >=18:
    print("You are now signed up.")
elif age <0:
    print("You must be 18+ to sign up. You have not been born.")
else: # previously was else == "":
    print("Please enter your age to continue!!")


response = input("Would you like some food? (Y/N): ")
if response == "Y" or "y":
    print("Have some food!")
elif response == "N" or "n":
    print("No food for you!!")
else:
    print("Please insert a value to continue!!")

name = input("Enter your name:")
if name == "":
    print("You did not enter your name.")
else:
    print(f"Hello {name}, Welcome to my app!!")

         #BOOLEAN IF STATEMENTS
for_sale = True
if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")

is_online = False
if is_online:
    print("The user is online.")
else:
    print("The user is offline.")

                 #CALCULATOR PROGRAM
operator = input("Enter an operator (+-*/): ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
# NB: In print functions, only use double quotes when you are outputting string data type only i.e characters 
if operator == "+":
    result = num1 + num2
    print(round(result,4))
elif operator == "-":
    result = num1 - num2
    print(round(result,4))
elif operator == "*":
    result = num1 * num2
    print(round(result,4))
elif operator == "/":
    result = num1 / num2
    print(round(result,4))
elif operator == "":
    print("Please enter an operator.")
else:
    print("The operator you have eneterd is invalid.")


                # WEIGHT CONVERSION PROGRAM
weight = input("Enter your weight: ")
unit = input("Kilograms or Pounds (kgs/lbs): ")
if unit == "K" or "k":
    weight = weight * 2.205
    unit = "kgs"
    print(f"Your weight is: {round(weight,4)} {unit}")
elif unit == "L" or "l":
    weight = weight / 2.205
    unit = "lbs"
    print(f"Your weight is: {round(weight,4)} {unit}")
else:
    print("The unit {unit} is not valid. Try again.")  

              #TEMPERATURE CONVERSION PROGRAM
temp = float(input("Enter the temperature: "))
unit = input("Is the temperature in celsius or farenheit(C/F)?: ")

if unit == "C" or "c":
    temp = round((temp *9)/5 + 32 , 2)
    print(f"The temperature in farenheit is: {temp}°F")
elif unit == "F" or "f":
    temp = round((temp - 32) * 5/9 , 2)
    print(f"The temperature in celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement. Try again")

            # LOGICAL OPERATORS(They allow us to evaluate multiple conditions i.e or,and,not. We can link them together within if)
# "or" means atleast one of the conditions must be true
# "and" means both the conditions must be true
# "not" inverts the condition e.g notFalse, notTrue
# (Examples are in video)

            #CONDITIONAL EXPRESSIONS(This is a one line shortcut for if-else statement aka ternary operator)
# print or assign one of two values based on a condition
# return X if condition else Y

num = -5
print("Positive" if num >0 else "Negative")
print("Even" if num%2 ==0 else "odd")

a = 6 
b = 7
max_num = a if a>b else b
min_num = a if a<b else b
print(max_num)
print(min_num)

age = 25
status = "Adult" if age >=18 else "Child"
print(status)

temperature = 30
weather = "Hot" if temperature >20 else "Cold"
print(weather)

user_role = "Admin"
user_access = "Full access" if user_role =="Admin" else "Limited access"
print(user_access)


                       #STRING METHODS
name = input("Enter your full name: ")
result = len(name) # Length function will give us the length of a string including spaces
result2 = name.find(" ") # This will return the first occurance of a given character, the position in number form             !!!!!!!!!!!!!
# result = rfind(" ") # This will find the last occurance
print(result2)
# NB: Indexes always begin with zero, if python is unable to find a given character it will return -1

name = name.capitalize(" ") # will capitalize the first letter
name = name.upper(" ") # This will convert all string characters to upper case
name = name.lower(" ") # This will convert all string characters to lower case
name.isdigit() # This will return true/false if string contains only digits. The result is boolean
name.alpha() # This will return true/false if string contains only alphabetical characters.

phone_number = "0123456789" ##### This is an assumed value, i need to re cheeck the video
result = phone_number.count(" ") # This will count how many characters are in that string and it returns integers
phone_number.replace("-", " ") # It replaces the occurance of one character with another. It returns a new string
#NB: If you would like a comprehensive method to all the strings available to you, type print(help(str))

# e.g An exercise to validate user input, the rules are the username cannot connot contain more than 12 characters, no spaces and no digits.
username = input("Enter your username: ")
if len(username) >12 :
    print("Your username cannot be more than 12 characters.")
elif username.find(" ") == 0:
    print("Your username cannot contain spaces")
elif username.isdigit is False:
    print("Your username must not contain digits.")
else:
    print(f"Hello {username}, Welcome.")

                     # STRING INDEXING(This allows us to access the elements of a sequence using [] i.e indexing operator --->  [start:end:step] )
credit_number = "1234-5678-9012-3456"
# NB: also count the hyphens as positions.
print(credit_number[0]) # At index 0, the output would be 1 because the computers count in natural numbers i.e 0,1,2,3,4...
print(credit_number[0:4]) # from 1 upto 4 in 1234- , The first digit is inclusive and the last digit is exclusive oR [:4]
print(credit_number[5:9]) 
print(credit_number[5:])
print(credit_number[-1]) # last character in string, in this case -1=6, -2=5, -3=4....etc
print(credit_number[::2]) #Printing/pacing at 2 intervals in between i.e skipping between characters
print(credit_number[::-1]) # prints the inverse of credit card no.( backwards / reverse )
print(credit_number[::1]) #prints the actual credit card

#Qn: Print the last 4 digits of a credit card number
credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

                      #FORMAT SPECIFIERS
# When used in the context of a f-string, they allow us to format a value based on what flags are inserted. Following your value you while type a colon
# and flags. Depending on what flags you inserted, it will format your flag a certain way.  e.g 
# .(number)f --> round to that many decimal places(fixed point)
# (number) ---> allocate that many spaces e.g :10
# 03 ---> allocate and zero pad that many spaces
# < = justify left
# >  = justify right
# :^ = center align
# :+ = use a plus sign to indicate a positive value. use a space for positive numbers. They are lined up evenly even thou we have a negative in here.
# := insert a space before positive numbers
# :, = comma separator(thousands separator)  e.g

price1 = 3.14159
price2 = -987.65
price3 = 12.34
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2: .1f}")
print(f"Price 3 is ${price3:.1f}")
# NB: You can use multiple flags if you want to depending on your program. e.g
print(f"Price 1 is ${price1 :+,.2f}")
print(f"Price 2 is ${price2 :+,.2f}")
print(f"Price 3 is ${price3 :+,.2f}")

                  #WHILE LOOP (This will execute some code while some condition remians true.)(It is easy to understand when translated from if loop.)
name = input("Enter your name: ")
while name == "":
    print("You did not enter your name.")
    name = input("Enter your name: ")
    print(f"Hello, {name}")
#NB: If you dont find some way to exit the while loop, you will enter into an infinite loop. in this case it will be the name_input statement.

age = int(input("Enter your age: "))
while age < 0: # because we want the user to type a positive number 
    print("Age can't be less than zero.")
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")

food = input("Enter a food you like ( q to quit): ")
while not food == "q":
    print(f"You like {food}.")
    food = input("Enter another food you like (q to quit): ")
print("Bye.")
# NB: I need to figure out how to add a capital case for q in this program.

num = int(input("Enter a number between 1-10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1-10: "))
    print(f"Your number is {num}.")
# These while statements work by first executing the unwanted part then executing the desired part/output. '

             #COMPOUND INTEREST CALCULATOR (A=P(1+R/N)**T)
principle = 0
rate = 0
time = 0
while principle <=0:
    principle = float(input("Enter the principle amount: "))
    if principle<=0:
        print("The principle can't be less than or equal to zero.")
while rate <=0:
    rate = float(input("Enter the interest rate: "))
    if rate <=0:
        print("Interest rate can't be less than oe equal to zero.")
while time <=0:
    time = int(input("Enter the time in years: "))
    if time <=0:
        print("Time cannot be less than or equal to zero.")
total = principle *pow((1+rate/100),time)
print(f"Balance after {time} year(s): ${total:.2f}")
#NB: If principle, rate and time were simply <0, the program would just jump to the last print statement. So to include zero in our program,change the
# principle, rate and time <=0 to 'true' then add 'else:' and break within each.

                   #FOR LOOPS(These execute a block of code a fixed number of times)
# You can iterate over a range, string, sequence e.t.c 
# There is a lot of overlap btn for loop and while loop but for loop is better when you have to do something a fixed number of times.

for x in range(1,11): # x is the counter, 1 is the start and 11 is the stop.The stop is exclusive in nature.
    print (x)         # Range can be iterated

for x in reversed(range(1,11)):
    print (x)
    print("Happy new year!!")

for x in range(1,11,3): # Adding format strings
    print(x)

credit_card = "1234-5678-9102-3456" # Strings can be iterated too
for x in credit_card:
    print(x)
# NB: These 2 useful keywords aren't exclusive to for loops and can be used with while loops as well. They are 'continue' and 'break'.

for x in range(1,21): # This will skip over the number 13
    if x == 13:
        continue
    else:
        print(x)

for x in range(1,21): # printing from 1-12
    if x == 13:
        break
    else:
        print(x)

                #CREATING A COUNT-DOWN MACHINE (TIMER)  NB: Functions are within modules
import time
time.sleep(3) # Our program will sleep for the given no. of seconds
print("TIME'S UP!!")

import time
my_time = int(input("Enter the time in seconds: "))
for x in range(my_time,0,-1):     # or reversed(range(0,my_time))
    print(x)
    time.sleep(1)
print("TIME'S UP!!")

import time
my_time = int(input("Enter the time in seconds: "))
for x in range(my_time,0,-1):
    seconds = x%60
    minutes = int(x/60)%60
    hours = int(x/3600) # Where there is no. %24 is bcoz there are no days in program
print(f"{hours:02}:{minutes:02}:{seconds:02}")
time.sleep(1)
print("TIME'S UP!!") # ERROR IN CODE????
''' Code Correction
import time
my_time = int(input("Enter the time in seconds: "))
for x in range(my_time,0,-1):
    print(x)
    time.sleep(1)
    seconds = x%60
    minutes = int(x/60)%60
    hours = int(x/3600) # Where there is no. %24 is bcoz there are no days in program
    print(f"{hours:02}:{minutes:02}:{seconds:02}")    
print("TIME'S UP!!")

'''

                   # NESTED LOOP (This is a loop within another loop as one outer and another inner)
# You can have a for loop inside a for loop, a while loop inside a while loop, a for loop inside a while loop & a while loop inside a for loop.
for x in range(3): # The code in the outer loop will be executed 3 times
    for y in range(1,10): # The second value is exclusive
        print(y, end =" ") # end="" is for straight line(horizontal),make sure you change the inner loop to a different value.
print()                   # Repeat the iterations on a new line'

# Qn: Print a rectangle made of some symbol that we said, we have usertype input in how many rows & columns this symbol will have.
rows = int(input("Enter the no. of rows(#): "))
columns = int(input("Enter the no. of columns(#): "))
symbol = input("Enter the symbol to use: ")
for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()  # Move to the next line after each row
