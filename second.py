'''
                        # LIST, SETS & TUPLES (COLLECTION TYPES)   (A collection is a single "variable" used to store multiple values.)
# List[] is an ordered and changeable. Duplicates ok (repititions)
# Set{} is an unordered and immutable, but add/remove ok. With no duplicates
# Tuple() is ordered and unchangeable. Duplicates ok. Faster than list.
# NB: There are 4 types of collection including dictionary too but its kind of complicated hence saved for next time.
# e.g fruits=["apple","orange","banana","coconut"]             #( It is better to name in plural for variable names)
# print(fruits)   # if you want to access one of the elements, use[] and the index no. in the parenthesis e.g print(fruits[0]),
#  the no.s begin with 0,1,2,3..i.e natural numbers.
# Each value in collection is aka element. You can also do string indexing in collections e.g print(fruits[0:3]), [::2], [::-1] NB: 2nd element beginning frm index zero
# You can also iterate over them using for loop e.g  for x in fruits:           NB: X stands for fruit which is a more descriptive counter
#                                                       print(fruit)
# What are all the different methods avaliable we can use with collections, to list them we can use this function in this case: print(dir(fruits))
# If you want a clear description of all (each) these methods and attributes, use the help function i.e print(help(fruits))
# If you want the length of how many attributes are used in the collection, i.e print(len(fruits))
# Using 'in' operator we can see if a value is in our function e.g print("appple" in fruits)  and it returns boolean data.
# To add an element to the end of the list, use append method i.e fruits.append("pineapple")
# fruits.remove("apple") is used to remove an element
# fruits.insert(0,"pineapple") is used to insert a value at a specific(given) index
# With lists we can change one of the value after we create our list e.g fruits[0] ="pineapple"
#                                                                           for fruit in fruits:
#                                                                               print(fruit)                # NB: This iterates over the fruit, you can also reassign.
# fruits.sort() will sort a list
# fruits.reverse() will reverse a list based on order we placed them not alphabetically
# fruits.clear() will clear a list
# print(fruits.index("coconut")) will print the index of a particular fruit. If the value is not in list you will get an error.
# print(fruits.count("banana")) will count the number of times that a fruit is found within a list bcoz duplicate values are okay
                                        
                            # SET
# To display the different attributes and methods of a set, use print(dir(fruits)) & print(help(fruits)) for indepth description
# You cannot use indexing on sets like fruits[0] on lists because they are unordered
# fruits.add("pineapple") is to add elements
# fruits.remove("apple") is to remove elements
# fruits.pop is to remove whatever element is first but is random thou
# fruits.clear
                            # TUPLE
# dir, help, len, in, count, index are all found in tuples.
# In any of these collections, they are iteratable, so you can iterate over them using a for loop i.e for fruit in fruits
#                                                                                                         print(fruit)

                                    #  SHOPPING CART PROGRAM (based on lists,sets and tuples)
foods =[]
prices =[]
total = 0
while True:
    food = input("Enter a food to buy(q to quit): ")
    if food.lower()=="q":
        break
    else:
        price = float(input(f"Enter the price of a {food}:$ "))
        foods.append(food)
        prices.append(price)
        print("----------------Your Cart----------------")
        for food in foods:
            print(food, end =" ")
        for price in prices:
            total+=price
        print() # for new line of price
    print(f"Your total is: ${total}")

                  # TWO DIMENSION LISTS(2D) e.g . is 1 dimension, square is 2 dimension and cuboid is 3 dimension.
# A 2-D list is simply a list made of lists. e.g sdlist =[list1,list2,list3]. Like a spreadsheet, it is really useful if you need a list or a matrix of data. 
fruits =["apple","orange","banana","coconut"]
vegetables =["celery","carrots","potatoes"]
meats =["chicken","fish","turkey"]
groceries =[fruits,vegetables,meats]
print(groceries) # In output, we have individual lists separated by commas all enclosed by a set of square brackets.
# The arrangement of lists kind of represents a greater matrix, each list resembles a row, each individual element resembles a column.
# The row and column countings begin with zero i.e 0,1,2,3... i.e natural numbers
print(groceries[0])
# You don't necessarily have to name each inner list. e.g groceries =["apple","orange","banana","coconut"]
#                                                                    ["celery","carrots","potatoes"]
#                                                                    ["chicken","fish","turkey"]
# If you ever need to iterate over the elements of a 2D list, you can use nested loops. If you use a single loop, you would iterate over the rows i.e
# for collection in groceries:
#    print(collection)
# But to iterate over the elements found in each row, we would use a nested loop i.e
# for collection in groceries:
#     for food in collection:
#         print(food, end =" ")
#     print()

# NB: You can make a tuple made up of sets, loops of tuples, sets of tuples, etc... based on your programs.

# Qn: Create a 2D num pad (normally found on a phone)
num_pad = ((1,2,3),   # 2-D Tuple  ..... it is a collection made up of collections
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()
# NB: If you ever need a grid or a matrix of data, a 2D collection would work perfect.

                        # PYTHON QUIZ GAME
questions =("How many elements are in the periodic table?: "
            "Which animal lays the largest eggs?: ",
            "What is the most abundant gas in the atmosphere?: ",
            "How many bones are in the human body?: ",
            "Which planet in the solar system is the hottest?: ")
options =(("A. 116","B. 117","C. 118","D. 119"),
          ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
          ("A. Nitrogen","B. Oxygen","C. Carbondioxide","D. Hydrogen"),
          ("A. 206","B. 207","C. 208","D. 209"),
          ("A. Mercury","B. Venus","C. Earth","D. Mars"))
answers = ("C","D","A","A","B")
# we will be appending guesses to our list, that is why we are using [] rather than (). #### i need to confirm if there is a zero after guesses in video(next line)
guesses = 0
score = 0
question_num = 0

for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_num]:  # question_num is for given row number
        print(option)

guess =input("Enter (A,B,C,D): ").upper()
guesses.append(guess)
if guess==answers[question_num]:
    score+=1
    print("CORRECT!")
else:
    print("INCORRECT!")
    print(f"{answers[question_num]} is the correct answer")
question_num=+1 # Before we iterate the qtn num, we need to ask the user for a guess

print("-------------------------------")
print("            RESULTS            ")
print("-------------------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end= " ")
print()

print("guesses: ", end =" ")
for guess in guesses:
    print(guess, end =" ")
print()

score =int(score/len(questions) * 100)
print(f"Your score is: {score}%")
###### Error in program, something is not right

                             # DICTIONARY (Is a collection of {key:value} pairs ordered and changeable). No duplicates e.g id & name, item & price.
# We use {} similarly with sets.
# Qn: Create a dictionary of countries with capitals respectively
capitals = {"USA":"Washington D.C",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}
# print(dir(capitals)) to see the different attributes and methods of dictionary
# print(help(capitals)) provides indepth description of all attributes and methods
# print(capitals.get("USA")) to get one of those values from our dictionary, check to see if a key is in our dictionary.if value not found, it will return none.
# it can aslo be used in if statement e.g if capitals.get("Japan"):
#                                            print("That capital exists")
#                                         else:
#                                             print("That capital doesnt exist")
# print(capitals.update({"Germany": "Berlin"})) to insert a new key value pair or update an existing pair
# capitals.pop("China") to remove a key value pair
# capitals.popitem() removes the latest key value pair that was inserted
# capitals.clear() clears the dictionary

# capitals.keys() return all the keys within a dictionary leaving out values. NB: Keys is an object which resembles a list. related to object oriented programming
# for key in capitals.keys():
#    print(key):  # To iterate over all the keys that is returned from the key method of your dictionary.

# values =capitals.values()    # Returns all values without any keys. Will return an object which resembles a list in output.
#   print(values)

# for value in capitals.value():               # Iterate and print over every value in our dictionary
#     print(value)

# items =capitals.items()               # items returns a dictionary object which resembles a 2D list of tuples
#    print(items)

# for key, value in capitals.items():
#     print(f"{key}:{value}")

                                       # CONCESSION STAND PROGRAM (application of dictionaries)
menu ={"Pizza":3.00,
       "nachos":4.50,
       "popcorn":6.00,
       "fries":2.50,
       "chips":1.00,
       "pretzel":3.50,
       "soda":3.00,
       "lemonade":4.25}
cart =[]
total =0
print("-------------MENU--------------")
for key, value in menu.items():
    print(f"{key:10}:${value:.2f}")
    print("---------------------------")

while True:
    food =input("Select an item(q to quit): ").lower()
    if food== "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----------YOUR ORDER----------")
for food in cart:
    total=+menu.get(food)
    print(food, end =" ")
    print() # print a new line
print(f"Total is: ${total:.2f}")

                           # RANDOM NUMBERS
import random # random module type
print(help(random))  # comprehensive list
number = random.randint(1,6) # You can also place variables as long as they contain numbers
print(number)
random.random() # Return a float no. btn 0-1

import random
low =1
high =100
number =random.randint(low,high)
print(number)

import random
options =("rock","paper","scissors")
option =random.choice(options)  # sequence in ()
print(option)

import random
cards =["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)

# Qn: Create a number guessing game
import random
lowest_num =1
highest_num =100
answer = random.randint(lowest_num,highest_num)
guesses = 0    # Keep track of the number of wrong guesses
is_running = True  # We want the user to keep guessing as long as is running = True
print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess =int(input("Enter your guess: "))
    if guess.isdigit():
        guesses+=1
    if guess<lowest_num or guess>highest_num:
        print("That number is out of range")
        print(f"Please select a number between {lowest_num} and {highest_num}")
    elif guess < answer:
        print("Too low! Try Again!")
    elif guess < answer:
        print("Too High! Try Again!")
    elif guess == answer:
        print(f"CORRECT! The answer was{answer}")
        print(f"Number of guesses: {guesses}")
        is_running = False
    else:
        print("Invalid Guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")
#### Attrribute error, program not running properly

                      # ROCK, PAPER, SCISSORS GAME
import random
options = ("rock", "paper","scissors")
player = None
computer =random.choice(options)

while player not in options:
    player =input("Enter a choice(rock,paper,scissors): ")
    print(f"Player : {player}")
    print(f"Computer : {computer}")

if player == computer:
    print("It's a tie!")
elif player =="rock" and computer=="scissors":
    print("You win!")
elif player =="paper" and computer=="rock":
    print("You win!")
else:
    print("You lose!")

play_again = input("Play again?(Y/N): ").lower()  # in short form is ---> if not input("Play again(Y/N): ").lower()=="y":
if not play_again == "y":                         #                            running = False
    running = False
print("Thanks for playing!")

                        # DICE ROLLER PROGRAM (ascii art is in video description)
import random
# print("\u25CF\u250C\u2500\u2510\u2502\u2514\u2518") # To utilize(enter) uni code characters hence create ascii code art, it depends on your os.
# ●    ┌          ─          ┐        │            └            ┘

dice_art ={1:("┌────────────┐",                # This is a dictionary {} with key(number):value(tuple made of string) pairs
              "│            │",
              "│     ●      │",
              "│            │",
              "└────────────┘"),                                    
           2:("┌────────────┐",
              "│  ●         │",
              "│            │",
              "│         ●  │",
              "└────────────┘"),
           3:("┌────────────┐",
              "│  ●     ●   │",
              "│            │",
              "│     ●      │",
              "└────────────┘"),
           4:("┌────────────┐",
              "│  ●      ●  │",
              "│            │",
              "│  ●      ●  │",
              "└────────────┘"),
           5:("┌────────────┐",
              "│ ●        ● │",
              "│      ●     │"
              "│ ●        ● │",
              "└────────────┘"),
           6:("┌────────────┐",
              "│ ●   ●   ●  │",
              "│            │",
              "│ ●   ●   ●  │",
              "└────────────┘"),}

dice =[]
total = 0
num_of_dice =int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

# for die in range(num_of_dice):                 # To visually display the die vertically
# for line in dice_art.get(dice[die]):
# print(line)

for line in range(5):                            # This is the most important part of the code
    for die in dice:
        print(dice_art.get(die)[line], end =" ")
    print()

for die in dice:
    total+=die
print(f"Total: {total}")

                       # FUNCTIONS (A block of reusable code)
# place () after a function name to invoke it
# Any data you send a function is known as arguments
# A temporary variable used within a function is known as parameter
# You call a function to invoke it
# A return is a statement used to end a function and send a result back to the caller e.g

def happy_birthday (name,age):
    print(f"Happy Birthday to you {name}!")
    print(f"You are {age} years old!")
    print("Happy Birthday to you!")
    print()
happy_birthday("bro",20) # call it 2 more times to execute 3 times instead of repeating code or using loops
happy_birthday("Steve",18)
happy_birthday("Joe",25)

# NB: With functions you are able to send data directly to a function using arguments. You can send values/variables directly to a function in ().
# You can also name parameters with something unique

# Qn: Create an invoice
def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
display_invoice("Bro Code", 42.50, "01/01")
display_invoice("Joeshmo", 100.01, "01/02")

# Qn: Creating functions to add, multiply, divide and subtract two(2) numbers together
def add(x,y):
    z= x+y
    return z
def subtract(x,y):
    z= x-y
    return z
def multiply(x,y):
    z= x*y
    return z
def divide(x,y):
    z =x/y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

# Arithmetic Function plus user input
def add(x,y):
    z= x+y
    return z
def subtract(x,y):
    z= x-y
    return z
def multiply(x,y):
    z= x*y
    return z
def divide(x,y):
    z =x/y
    return z

digit1 = int(input("Enter a first value: "))
digit2 = int(input("Enter a second value: "))

print(f"The Addition of {digit1} and {digit2} is : {add(digit1, digit2)}")
print(f"The subtraction of {digit1} and {digit2} is : {subtract(digit1,digit2)}")
print(f"The Multiplication of {digit1} and {digit2} is : {multiply(digit1, digit2)}")
print(f"The Division of {digit1} and {digit2} is : {divide(digit1, digit2)}")


def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first+" "+last  # Concatenate them together and return as a single string
full_name = create_name("bro","code")
print(full_name)  # Using return function, you can return some data back to the place in which you call the function

# Function rewritten with user input
def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first+" "+last

start = input("Enter your first name: ")
second = input("Enter your second name: ")

full_name = create_name(start,second)
print(f"Hello, Welcome {full_name}")

                     # DEFAULT ARGUMENTS
# These are the default value for certain parameters
# Default is used when that argument is omitted (when you invoke a function)
# They make your functions more flexible and reduce the number of arguments
# 1. Positional  2. Default  3. keyword  4. Arbitrary
# NB: In last video we discussed positional arguments
# Used if values are consistent most of the time

def net_price(list_price,discount =0,tax =0.05):
    return list_price *(1-discount)*(1+tax)  # formula
print(net_price(500))
print(net_price,0.1,0) # It will prioritize the arguments given than the fixed parameter up. Adv is that it can accept upto additional arguments

# Qn: Create a count-up timer
import time
def count(start,end):
    for x in range(start,end+1): # It is because the second argument is exclusive
       print(x)
       time.sleep(1)
    print("DONE!")
count(0,10)   # Also try (30,15)
# NB: We can change the parameter to make a default argument by arranging starting with non default arguments then default ones next,
#  then remove it from the argument below.

# this code is to allow user input
first = int(input("Enter a starting number: "))
last = int(input("Enter an ending number: "))

print(count(first,last))

                   # KEYWORD ARGUMENTS
# An argument preceeded by an identifier. Adv is it helps with readability
# Order of arguments doesn't matter
def hello(greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")
hello("Hello", last="Squarepants", title="Mr.", first="Spongebob")
# NB: Positional arguments without title/description follow keyword arguments
for x in range(1,11): # because the second value is exclusive
    print(x, end =" ") # end is a key word argument found within the built-in print statement
print("1","2","3","4","5", sep="-")
# Alot of buit-in key functions e.g print have keyword arguments you can use

# Creating a function to generate a phone number, but we are going to pass in a country code, area code, first 3 digits and last 3 digits.
def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"
phone_num =get_phone(country =1, area =123, first =456, last =7890)
print(phone_num)

                  # ARBITUARY ARGUMENTS (vary amount of arguments)
# When you don't know how many arguments that the user is going to pass in when they invoke a function.
# *args --> allows you to pass multiple non-key arguments
# **kwargs---> allows you to pass multiple keyword-arguments
#  * is unpacking operator
# 1.Positional  2. Default  3. Keyword  4. Arbitrary
# When you invoke a function that has *args or *kwargs, you will pack all of those arguments into a tuple if its args or a dictonary if its kwargs
def add(*args): # instead of a,b
    print(type(args))  # to prove that the type is a tuple. We can use its built in methods/itertae over it

total =0
for every arg in args:
    total+=arg
    return total
print(add(1,2,3))   # you can also change arg for hums(plural & singluar) in all cases but the * is most important
############### ERROR

def display_name(*args):
    for every arg in args:
        print(arg, end=" ")
display_name("Spongebob","Harold","Squarepants","III")
############### ERROR

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_address(street = "123fake St.", apt ="100", city ="Detroit", state ="MI", zip ="54321")  # It can pass in varying number of pairs

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end =" ")
    print()

#for value in kwargs.values():      # To print the kwargs in one line
#   print(value, end =" ")
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}{kwargs.get('state')}{kwargs.get('zip')}")
shipping_label("Dr.", "Spongebob","Squarepants", street = "123fake St.", apt ="100", city ="Detroit", state ="MI", zip ="54321")
# NB: You can place the 2nd print in an if statement to avoid displaying none is a value is missing in  a kwarg
# Pseudocode example:
if apt in kwarg
   print street and apt
elif pobox in kwargs
    print street & pobox
else
    print street

                       # ITERABLES 
# An iterable is a category. It is an object/collection that can return its elements one at a time, allowing it to be iterated over in a loop.
# e.g list, tuples, set, strings, dictionary

                      # MEMBERSHIP OPERATORS
# It is used to test whether a value/variable is found in a sequence (string,list,tuple,set,dictionary)
# i.e      1. in       2. notin
word = "APPLE"
letter = input("Guess a letter in the secret word: ").upper()
if letter in word:  # will return a boolean value
    print(f"There is a(an) {letter}")
else:
    print(f"{letter} was not found")

students ={"Spongebob","Patrick","Sandy"}
student = input("Enter the name of a student: ")
if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")

grades = {"Sandy":"A","Squidward":"B","Spongebob":"C","Patrick":"D"}
student = input("Enter the name of a student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found.")

email ="Brocode@gmail.com"
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

                               # LIST COMPREHENSHION (A conise way to create lists in python)
# They are compact and easier to read than traditional loops
# Formula: (expression for value in iterable if condition)
doubles =[]
for x in range(1,11):
    doubles.append(x*2)
print(doubles)
# The above code is similarly summarized in list comprehension
doubles=[x*2 for x in range(1,11)]
print(doubles)

triples =[y*3 for y in range(1,11)]
print(triples)

squares =[z*z for z in range(1,11)]
print(squares)

fruits =["apple","orange","banana","coconut"]
fruits =[fruits.upper() for fruit in fruits]
print(fruits)
####### Attribute error
# NB: Or you can substitute the first line of code for the last 'fruits' in [].

fruits =["apple","orange","banana","coconut"]
fruit_chars =[fruit[0] for fruit in fruits]  # To print the first letter in every string
print(fruit_chars)

numbers =[1,-2,3,-4,5,-6]
positive_nums =[num for num in numbers if num>=0] # If we are not modifying any value, we can just return the value of num in the place of expression.
print(positive_nums)
negative_nums =[num for num in numbers if num<0]
print(negative_nums)
even_nums =[num for num in numbers if num%2==0]
print(even_nums)
odd_nums =[num for num in numbers if num%2==1]
print(odd_nums)

grades =[85,42,79,90,56,61,30]
passing_grades =[grade for grade in grades if grade>=60]
print(passing_grades)

                        # MATCHCASE STATEMENT (switch) (It is a newly added feature in python 3.10)
# An alternative to using many elif statements.  Execute some code if a value matches a 'case'.   Adv is that it is cleaner and the syntax is more readable.
def day_of_week(day):
    if day==1:
        return"It is Sunday"
    elif day==2:
        return"It is a Monday"
    elif day==3:
        return"It is a Tuesday"
    elif day==4:
        return"It is a Wednesday"
    elif day==5:
        return"It is a Thursday"
    elif day==6:
        return"It is a Friday"
    elif day==7:
        return"It is a Saturday"
    else:
        return"Not a valid day"
print(day_of_week(1))

# To convert it to a matchcase statement, place 'matchday:' above it and substitute [if day== ] for[case],[elif day== ] for case and [else] for case.
def is_weekend(day):
    match day:
       case "Sunday":
        return True
       case "Monday":
        return False
       case "Tuesday":
        return False
       case "Wednesday":
        return False
       case "Thursday":
        return False
       case "Friday":
        return False
       case "Saturday":
        return True
       case _:
        return False
print(is_weekend("Saturday"))
'''
# In short form, the same code can be written as shown below:
def is_weekend(day):
    match day:
      case "Saturday","Sunday":
        return True
      case "Monday","Tuesday","Wednesday","Thursday","Friday":
        return False
      case _:
       return False
print(is_weekend("Saturday")) 


















