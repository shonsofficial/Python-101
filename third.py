'''
                    # MODULE (Is a file containing code you want to include in your program)
# use 'import' to include a module(built-in or your own)
# sometimes it is useful to breakup a large program into reusable separate files
# print(help("modules"))  # A list of all modules found within the standard python library.
# print(help("math")) # To list all different functions and variables found within the module.
# import math as m  # m is the nickname given to math and is used in program to refer to math
# from math import pi  # To import only something specific from module instead of whole and you would no longer need the module name 
# e.g print(pi) instead of print(math.pi)/print(m.pi)
# NB: It is better to limit use of 'from' module so as to limit errors(confusion) with other variables e.t.c
import math
result =math.pi
print(result)
result =math.square(3)
result =math.cube(3)
result =math.circumfrence(3)
result =math.area(3)

pi =3.142
def square(x):
    return x**2
def cube(x):
    return x**3
def circumfrence(radius):
    return 2*pi*radius
def area(radius):
    return pi*radius**2
####### I need to rewatch this part of the video to understand in depth

                        # VARIABLE SCOPE AND SCOPE RESOLUTION
# A variable scope is where a variable is both visible and accessible
# Scope resolution, the order is LEGB (local enclosed global built-in) in-out order
# Variables declared with a function have a local scope
def func1():
    a =1
    print(a)

def func2():
    b =2
    print(b)
func1()    # invoke the functions
func2()
# NB: If you exchange print(a) with print(b), you would run into name error. Functions can't see inside other functions but can see inside their own.
# That is why we sometimes pass arguments two functions so that our functions are aware of them e.g

def happy_birthday(name,age):
    print(f"Happy birthday dear {name}")
    print(f"You are {age} years old")
def main():
    name ="Bro"
    age ="21"
    happy_birthday(name,age)
main()
# NB: Variables can share the same name as long as they are in different scope

                # IF NAME =='MAIN' (if__name__=='__main__') (This script can be imported or run standalone)
# Functions and classes in this module can be reused without the main block of code executing e.g
def main():
    # Your program goes here
if__name__=="__main__": # it means that if we are not running this program directly, do not do it(do not run this code)
   main()            # A call to a function named main/something similar
# Sometimes you would like the functionality of a program without executing the main body of code e.g a library
# ex.library = Import a library for functionality, when running library directly, display a help page
# But if were to run that library instead of importing it, we could display a help page
# print(dir()) # To display directory with all built-in attributes
# dunda means double underscore
# from script1 import* (meaning everything)
# if__name__=="__main__":  # We can check to see which file is running directly
def favorite_food(food):
   print(f"Your favorite food is {food}")
def main():
   print("This is script1")
   favorite_food("Pizza")  # calling function
   print("Goodbye!")
if__name__=="__main__":
   main()

# NB: Good practice(code is modular, helps readability,leaves no global variables, avoid unintended execution). Best example is ex.library

                          # PYTHON BANKING PROGRAM (The aim is help us get used with functions)
# The sections of this program are: show balance, deposit, withdraw
def show_balance(balance):
    print("********************************")
    print(f"Your balance is $ {balance:.2f}")
    print("********************************")

def deposit():
    print("********************************")
    amount =float(input("Enter an amount to be deposited: "))
    print("********************************")

    if amount<0:
        print("*************************")
        print("That's not a valid amount")
        print("*************************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("********************************")
    amount =float(input("Enter amount to be withdrawn: "))
    print("********************************")

    if amount > balance:
        print("******************")
        print("Insufficient funds")
        print("******************")
        return 0
    elif amount>0:
        print("********************************")
        print("Amount must be greater than zero")
        print("********************************")
        return 0
    else:
        return amount

def main():
    withdraw =0
    is_running =True

    while is_running:
        print("***********************")
        print("    Banking Program    ")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("***********************")
        
        choice =input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice =="2":
            balance += deposit()
        elif choice =="3":
            balance -= withdraw(balance)
        elif choice =="4":
            is_running = False
        else:
            print("**************************")
            print("That is not a valid choice")
            print("**************************")
    
    print("***************************")
    print("Thank you. Have a nice day!")
    print("***************************")
if __name__=='__main__':  # This means that this program can be imported or run standalone. If program is run indirectly, the code won't run.
main()

                                      # SLOT MACHINE
import random

def spin_row():
    symbols = ['🍒', '🍉','🍋', '🔔', '⭐']    # Press 'win' + ';' to use emoji's

    results =[random.choice(symbols) for _ in range(3)] # using _ as a placeholder for symbol
    # This is the longer version of the list comprehension explained below:
    # results =[]
    # for symbol in range(3):
    #    results.append(random.choice(symbols))
    # return results    
    
def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")
def get_payout(row, bet): # if somebody gets matching pairs on the slot machine
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet*3
        elif row[0]=='🍉':
            return bet*4
        elif row[0]=='🍋':
            return bet*5
        elif row[0]=='🔔':
            return bet*10
        elif row[0]=='⭐':
            return bet*20
        return 0 # if all symbols dont match , we dont give the users anything


def main():
    balance = 100 # starting balance
    print("*************************")
    print(" Welcome to python slots ")
    print(" Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance > 0:
        print(f"Current balance: $ {balance}")
        
        bet = input("Enter your bet amount: ")
        if not bet.isdigit():
            print("Please enter a valid number")
            continue  # This will skip the currrent iteration of this word and start from the beginning i.e while...
        
        bet = int(bet)
        if bet > balance:
            print("Insufficient funds!")
            continue
        if bet <= 0:
            print("Bet must be greater than zero") 
            continue

        balance-=bet

        row = spin_row()
        print("Spinning....\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print("You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()
        if play_again != 'Y':
            break

        print("*********************************************")
        print(f"Game Over! Your final balance is $ {balance}")  
        print("*********************************************")    

if __name__=='__main__':
    main()

                   # SUBSTITUTION CYPHER ENCRYPTION PROGRAM
# We are going to replace every instance of the charcater to hide the message chosen at random and using the same key to decrypt the message.   
import random
import string
chars = list(" " + string.punctuation + string.digits + string.ascii_letters)
key = chars.copy()

random.shuffle(key)

# print(f"Chars: {chars}")
# print(f"Key : {key}")

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter) # from the each letter of the plain text, we are assigning it to the specific index of the characters and storing it as index variable
    cipher_text+=key[index] # using the character's index of the plain text, we are substituting it with the key at that index and assigning it to cipher text variable
print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# DECRYPT
print("*******************************")
cipher_text_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text+=chars[index]
print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
print("Thank you for using our program!")
print("********************************")

                       # HANGMAN GAME  (NB: When creating a program, it is useful to first declare the variables and data structure first then functions)
# The rules of the game are, using the random module, we will guess one of the words at random, we won't see what the words are but shall guess from the place
#  where they are. Once we reach 6 incorrect guesses, we loose the game. Before each guess, we will display some ascii art (hangman art in this case in a dictionary).

import random

# a set of words
words = ("lion", "tiger", "elephant", "zebra", "giraffe", "cheetah", "leopard", 
    "kangaroo", "panda", "koala", "wolf", "fox", "bear", "deer", "camel", 
    "rhino", "hippo", "buffalo", "dolphin", "whale", "shark", "octopus", 
    "eagle", "hawk", "sparrow", "penguin", "owl", "peacock", "parrot", 
    "salmon", "trout", "tuna", "crocodile", "alligator", "snake", "frog",
    "turtle", "rabbit", "squirrel", "hedgehog", "bat", "monkey", "chimpanzee",
    "gorilla", "antelope", "ostrich", "flamingo", "turkey", "pigeon", 
    "rat", "mouse", "beaver", "otter", "seal", "walrus", "jaguar", "lynx")

# dictionary where the key represents the number of incorrect guesses and the value represents the ascii hangman art
hangman_art ={ 0:("  ",
                  "  ",
                  "  "),
               1:(" ° ",
                  "   ",
                  "   "),
               2:(" ° ",
                  " | ",
                  "   "),
               3:(" ° ",
                  "/| ",
                  "   "),
               4:("  °  ",
                  " /|\\",  # use double backslash to print one backslash because using a single backslash is an escape sequence
                  "     "),
               5:("  °  ",
                  " /|\\",
                  " /   "),
               6:("  °  ",
                  " /|\\",
                  " / \\")}
#for line in hangman[6]:    # To temporarily print our hangman art
 #   print(line)

def display_man(wrong_guesses):   # display the value hangman ascii art
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):  # it is going to be a list of underscore characters and it will flip to letter if guessed correctly
    print(" ".join(hint))

def display_answer(answer):   # It will display the answer either when we lose the game or when we win the game
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)

    wrong_guesses = 0
    
    guessed_letters =set()

    is_running =True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess =input("Enter a letter: ").lower()
        # display_answer(answer)   # to test display our answer

        if guess != 1 or not guess.isalpha():
            print("Invalid input")
            continue   # to skip this loop afterwards

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] == guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__=='__main__':
  main()
###### ERROR IN PROGRAM, ITS NOT FUNCTIONING PROPERLY

                           # PYTHON OBJECT ORIENTED PROGRAMMING
# An object is a "bundle" of related attributes (variables) and methods (functions). e.g phone, cup, book
# Methods are different from functions. A method is a function that belongs within an object 
# You need a cup to create many objects
# class = (blueprint) used to design the structure and layout of an object
# examples: phone(make call, receive call, turn on, turn off), cup(drink cup, fill cup, empty cup), book(open book, read book, close book)
class Car:               # object
    def __init__(self, model, year, color, for_sale ): # a constructor which is a special type of method which works similarly to a function. Self means this object we are creating right now.
        self.model = model                    # Attributes (variables)
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):           # methods (functions). They define what an object can do.
        print(f"You drive the {self.color} {self.model}")
    def stop(self):
        print(f"You stop the {self.color} {self.model}")
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car1 =Car("Mustang",2024,"Red",False)
car2 =Car("Corvette", 2025, "Blue", True)
car3 =Car("Charger", 2026, "Yellow", True)
print(car1.model)  # the dot is aka attribute access operator
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()        # You can do all the same for car2 and car3
car1.stop()
car1.describe()

# NB: With classes,they can take up alot of space, so you can place them within a new python file for better organization. Then you can import the module.
# Methods are actions which our objects can perform

                              # CLASS VARIABLES (They are shared among all instances(objects) of a class)
# They are defined outside the constructor. Allow you to share data among all objects created from that class while with instance variables,
# each object has their own version.
#  In the previous example, we used instance variables which were defined inside the class 
class Student:

    class_year = 2024    # class variable
    num_students =0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students+=1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(student1.name)
print(student1.age)

print(Student.class_year)
# NB: With class variable, you can access them through any one name of the object e.g student1,student2 but it's good practice to access them via the name of the class
# which helps with clarity and readability
print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

                          # INHERITANCE VARIABLES
# Allows a class to inherit all the attributes and methods from another class. It helps with code reusability and extensibility
#  e.g class Child(Parent) which is aka class sub(super)
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeek!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()                # Can do all the same with cat and mouse

dog.speak()
cat.speak()
mouse.speak()

                     # MULTIPLE INHERIITENCE & MULTI LEVEL INHERITENCE
# Multiple inheritence = inherit from more than one parent class e.g. C(A,B) 
#   Multi level inheritence = inherit from a parent which inherits from another parent. e.g. C(B) <-- B(A)  <---A  ie. C can inherit all attributes of A
class Animal:
     
     def __init__(self, name):  # define a constructor to assign these attributes
         self.name = name

     def eat(self):
         print(f"{self.name} is eating")

     def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")   # There are no parameters so we will not have to send any parameters to the argument 
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()   # but not hunt
hawk.hunt()     # but not flee
fish.hunt()
fish.flee()

# NB: Prey and predator will inherit everything that the animal class has, rabbit, hawk and fish will inherit everything that the prey and predator classes have.
rabbit.eat()
rabbit.sleep()
fish.eat()
fish.sleep()

                        # SUPER FUNCTION (This a function used in a child class (sub class) to call methods from a parent class(super class))
# It allows you to extend functionality of the inherited methods
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is a {self.color} and {"filled" if self.is_filled else "not filled" }")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):  # we need a constructor inorder to instantiate objects
        super().__init__(color, is_filled)         # The super function will take care of the attributes of shapes they have in common
        self.radius = radius

    def describe(self):
        super().describe()    # we are extending the functionality of the describe method
        print(f"It is a circle with an  area of {3.142* self.radius* self.radius} cm²")
        
class Square(Shape):
    def __init__(self, color, is_filled, width): 
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()    
        print(f"It is a square with an  area of {self.width* self.width} cm²")

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height): 
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()    
        print(f"It is a triangle with an  area of { 0.5 * self.width* self.height } cm²")

circle = Circle(color="Red", is_filled= True, radius= 5)
square = Square(color ="Blue", is_filled= False, width= 6)
triangle = Triangle(color="Yellow", is_filled= True, width = 7, height= 8)
print(circle.color)
print(circle.is_filled)
print(f"{circle.radius} cm")           # same with square and triangle

print(square.color)
print(square.is_filled)
print(f"{square.width} cm")   

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width} cm")
print(f"{triangle.height} cm")   
# That is how you can use the super function to reuse the constructor of a parent class,
#  without manually assign each of these attributes within each of the child classes.
# When using super(), imagine you replacing it with Shape in this case
circle.describe()
square.describe()
triangle.describe()
# There is also method overwriting if we create a similar method inside the child class, the child's version will be superior to the parent's version
# Not only are we printing this message from the parent, we are tacking on another print statement before that
'''

