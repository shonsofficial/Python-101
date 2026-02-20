'''
                                  # POLYMORPHISM (Greek word that means to have many forms or faces) (poly means many & morphe means forms)
# There are two ways to achieve polymorphism i.e inheritence and duck typing
# 1.Inheritence = an object would be treated of the same type as a parent class
# 2. Duck Typing = object must have necessary attributes/methods
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):    # abstract method
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
            return 3.142 * self.radius **2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base *self.height* 0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)  # previously was self.radius = radius
        self.topping = topping
        

# circle = Circle()  # A circle identifies as a circle and also considered a shape since it inherits from shape hence (2 forms) but it isnt a square or a triangle.
# square = Square()  # The same princilpe applies for the square and triangle as stated above
# triangle = Triangle()

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni",15)]   # Each of these forms has 2 forms/faces
# Our pizza class doesnt have an area method hence attribute error. Pizza is considered a pizza but not a shape because it doesnot inherit from the shape class

# afterwards, our pizza is considered a pizza and also considered a circle since it inherits from the circle, and our circle inherits from the shape class,
# hence our circle has 3 forms i.e pizza, circle and shape

for shape in shapes:
   print(f"{shape.area()} cm²")'

                                   # DUCK TYPING (Another way to achieve polymorphism besides inheritence.)
# Object must have the minimum necessary attributes/methods to be treated as a different type.
# ALso if an object resembles another, it also could be treated of that type.   "If it looks like a duck and quacks like a duck, then it must be a duck"
class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = False  # To assign(give) car the alive attribute

    def speak(self): # previously def horn(self)
        print("HONK!")

animals = [Dog(), Cat(), Car()]
# Car has no attribute to speak hence it lacks the minimum necessary attributes/methods
# Afterwards, if it has the minimum necessary attributes/methods, you could treat it as a different kind of object
for animal in animals:
    animal.speak()  # Do not use a print statement
    print(animal.alive)

                   # STATIC METHODS (A method that belongs to a class rather than any object from the class (instance))
# Usually used for general utility functions
# Instance methods = Best for operations on instances of the class(objects) . These are methods that belong to individual objects created from that class e.g
# def get_info(self):
#     return f"{self.name} = {self.position}"
# Static methods = Best for general utility functions that do not need access to class data e.g
# @staticmethod
# def km_to_miles(kilometers):
#     return kilometers * 0.621371

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):              # Instance method.  
        return f"{self.name} = {self.position}" 
    #Each object that we create from the above class will have their own get_info method to return the information on that object i.e object name and position

    @staticmethod
    def is_valid_position(position): # static methods dont have self as the first argument because we are not working with any objects created from this class. hence pass in position to check to see if a position is valid
        valid_positions = ["Manager", "Cashier","Cook", "Janiter"]
        return position in valid_positions # to check if position is in our list of valid positions.
    
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(employee1.get_info())    # To call an instance method, we have to access one of the class to use it
print(employee2.get_info())    # For instance method, you access the object then call the instance method
print(employee3.get_info())


    # In creating a static method, we do not need to rely on any objects to use this method i.e. we type Employee.is_valid_position() instead of employee1 = Employee()
print(Employee.is_valid_position("Rocket Scientist")) # Static method belongs to the class not any objects created from the class
# For static methods, you only need to access that class, you don't need to create any objects froms that class , it's general utility

                        # CLASS METHODS (Allow operations related to the class itself. They take "cls" as the first parameter which represents the class itself)
# NB: Whereas instance methods take self which refers to any object created from that class
class Student:
    count = 0      # class variable to count how many students we create
    total_gpa = 0

    def __init__(self, name, gpa):  # A constructor to construct some student objects
        self.name = name
        self.gpa = gpa
        Student.count += 1 # whenever we construct a student object, we will access the class of student to take our count variable +=1
        Student.total_gpa += gpa # whenever we construct a student object, we will access the class of student to take our total_gpa variable +=gpa

    def get_info(self):      # Instance method
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):  # a method to define the variable of count
        return f" Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:   # if not this if statement we would be dividing by zero then we will get an error
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count()) # When we call this class method, we can access or modify class data, this class variable of count
print(Student.get_average_gpa())

# NB: Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class Methods = Best for class-level data or require access to the class itself

                                # MAGIC METHODS (Dunder methods i.e. double underscore __init__, __str__, __eq__)
# They are automatically called by many of python's built-in operations e.g printing an object, seeing if 2 objects are equal, greater than ....e.t.c
# They allow developers to define or customize the behaviour of objects

class Student:
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
    
    def __str__(self):
        return f"Name: {self.name} gpa: {self.gpa}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self, other):
        return self.gpa > other.gpa

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)

print(student1)
print(student1 == student2)
print(student1 > student2)

class Book:
    def __init__(self, title, author, num_pages):   
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
       return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other): # self means book1 in this case and other means book2 in this case
        return self.title == other.title and self.author == other.author # Hence the equals statement would return true if both books have same title and author

    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self,other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key '{key}' was not found."

book1 = Book("The Hobbit", "J.R.R Tolkien", 310) # When we are calling the class of book and pass in our arguments, we are automatically calling the dunder/magic methods
book2 = Book("Harry Potter and the Philosopher's stone", "J.K Rowling", 223)
book3 = Book("The Lion, The Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)
print(book2)
print(book3)

print(book1 == book2) # If book1 and book2 had the same title, author and number of pages, they would still be not the same according to python, hence use __eq__ method

print(book2 < book3)   # would return a type error hence use __lt__ method (less than)

print(book2 > book3)

print(book2 + book3) #unsupported operand error hence use __add__

print("Lion" in book3) # uniterable error hence __contains__  . This is searching for a keyword in an object
print("Rowling" in book2)

print(book1['title']) # this will return a type error of unsubscriptable. This will search for a key(attribute) given an object. This is through indexing
print(book3['author'])
print(book2['num_pages'])
print(book3['audio'])

                               #  PROPERTY DECORATOR
# @property = decorator used to define a method as a property (it can be acccessed like an attribute)
# Benefits: Add additional logic when read, write or delete attributes.  Gives you getter, setter and deleter methods

class Rectangle:
    def __init__(self, width, height):
        self._width = width   # assigning...
        self._height = height  # The _ is to make these attributes private(internal and meant to be protected) hence shouldn't be accessed directly outside this class

    @property  # Whatever is within these methods will be returned when accessing width and height
    def width(self):
        return f"{self._width:.1f} cm"             # Getter method

    @property                                       # Getter method
    def height(self):
        return f"{self._height:.1f} cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(3, 4)   # constructing object

rectangle.width = 0
rectangle.height = -1

del rectangle.width
del rectangle.height

print(rectangle.width) # This gives a warning of access to a protected member _width and _height of a class
print(rectangle.height)  # if you use _height it's like they are raw 

                                # DECORATOR (A function that extends the behaviour of another function without modifying the base function)
# Pass the base function as an argument to the decorator
#  @add_sprinkles
#  get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs): # NB: Without this wrapper function, we will end up calling this function as soon as we apply the decorator without even calling the function.
                      # Hence we only want to execute this code when we want ice cream, not when we apply the decorator
        print("* You add sprinkles🎊 *")
        func(*args, **kwargs)     # imagine that we are replacing func() with print("Here is your ice cream🍧")
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("* You add fudge 🍫 *")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print("Here is your {flavor} ice cream🍧")                     # win + ; for emojis

get_ice_cream("Vanilla")

                                     # EXCEPTION HANDLING (An event that interupts the flow of a program)
# Types include: 1. ZeroDivisionError e.g 1/0 , 
# 2. TypeError (when performing an operation on a value that's of the wrong data type), 
# 3. ValueError (when you attempt to typecast a value of the wrong data type )         e.t.c.
# There are 3 steps to work with execptions: Try, except and finally
try: # for any code that is dangerous where it could cause an error
    pass
except: # To execute alternative code if we run into one of these exceptions
    pass
finally: # always executes regardless of whether there is an exception or not. It is usually used for any sort of cleanup you want to do.
    pass  # e.g. handling files to close a file after you done using it.

try:
   number = int(input("Enter a number: "))
   print(1/number)   # if userinput is 0 or pizza, you will get a value error
except ZeroDivisionError:
    print("You can't divide by zero, IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")

# NB: some people will type except exception: at once which will catch all exceptions, it is a bad practice because it is too broad of a cause.
# If you resort to using except exceptions: ,you will see an error message such as 'something went wrong'. 
# It is good practice to tell the user what went wrong exactly. Using the general method is only as a last option
# NB: There are many types of exceptions in python, look for them under the official python documentation for an extensive list.

                                   # PYTHON FILE DETECTION (It is under a mini-series of python file handling)
# We are first handling file detection before we cover read and write files
import os # This module provides a way for python to interact with the operating system 
# file_path = "test.txt" # Relative file path =>folder/test.txt and absolute file path => c:/Users/BroCode/desktop/test.txt
file_path = "C:\\Users\\Asus\\Downloads\\test" 
# use double backslashes since single one severes as an escape sequence of trying to print a tab character or you can use a forward slash too.
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path): # To check to see if a file is infact a file and not a directory
       print("That is a file")
    elif os.path.isdir(file_path): # To check to see if a location is a directory
        print("That is a directory")
else:
    print("That location doesn't exist")
# NB: If file extension is wrong, automatically the output will be that the file doesnot exist.
# If the file is in a folder, then you will have to preceed the relative file path with the folder name

                              # PYTHON WRITING FILES (.txt, .json, .csv) & OUTPUT
txt_data = "I like pizza!"   # Data to output
#file_path = "an output.txt"     # variable for file name
file_path = "D:/WK/CODE/PYTHON/an output.txt"

try:
    with open(file_path, "w") as file:               
        file.write(txt_data)  # file.write("\n" + txt_data) is for making a new line when appending text data                          
        print(f"Txt file '{file_path}' was created")       
# To create a file.  With is a statement used to wrap a block of text to execute. 
# with statement automatically closes a statement when we done with it. if you don't close it, you may run into unexpected behaviour.
# open() function will return a file object, 1st paremeter is the filepath, and the 2nd is the mode.
# x can also write best if file doesn't exist if file exists we will receive an error, a is for append and r is for read, w is for overwrite
except FileExistsError:   # to solve the x mode error
    print("That file already exists!")


employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
file_path = "D:/WK/CODE/PYTHON/output.txt"

try:
    with open(file_path, "w") as file:               
        for employee in employees:   # file.write(employees) cannot work due to type error of write argument must be a string not a list                      
            file.write(employee + " ")       
        print(f"Txt file '{file_path}' was created")
except FileExistsError: 
    print("That file already exists!")

                                                     # WRITING A JSON FILE (It is made of key value pairs)
import json

employee = {
    "Name":"Spongebob",
    "Age":"30",
    "Job":"cook"
}
file_path = "D:/WK/CODE/PYTHON/output.json"

try:
    with open(file_path, "w") as file:               
        json.dump(employee, file, indent=4)       
        print(f"Json file '{file_path}' was created")
except FileExistsError: 
    print("That file already exists!")

                                              # WRITING A CSV FILE (coma separated values)
import csv

employees = [["Name", "Age", "Cook"],  # Think of our 2D data structure as a table of rows and columns
            ["Spongebob", "30", "Cook"],
            ["Patrick", "37", "Unemployed"],
            ["Sandy", "27", "Scientist"]]
file_path = "D:/WK/CODE/PYTHON/output.csv"

try:
    with open(file_path, "w", newline="") as file:               
        writer = csv.writer(file)      # Writer is an object which provides methods for writing data to a csv file 
        for row in employees:
            writer.writerow(row)
        print(f"CSV file '{file_path}' was created")
except FileExistsError: 
    print("That file already exists!")

                                    # PYTHON READING FILES (.txt, .json, .csv)
file_path = "D:/WK/CODE/PYTHON/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read() # When we read our file object, it is going to return one long string which we shall assign to a variable named content 
        print(content)
except FileNotFoundError:  # If you miss to indicate the file extension
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")


                       # READING A JSON FILE
import json

file_path = "D:/WK/CODE/PYTHON/output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file) # content = file.read() cannot work for json files, it only words for .txt 
        print(content)
        #print (content["Name"]) # To access a value given its key
except FileNotFoundError:  
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

                         # READING A CSV FILE 
import csv

file_path = "D:/WK/CODE/PYTHON/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file) # content = json.load(file) cannnot work for csv files, it only works for json files
        for line in content:
           print(line)
           #print(line[0]) # You can access index to get a specified column ####ERROR!
except FileNotFoundError:  
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")


                                      # DATE & TIME
import datetime # This allows us to work with dates and times using our system(computer) clock
date = datetime.date(2025, 1, 2)  # created date object in year, month & day order
print(date)

today = datetime.date.today()   # date of today
print(today)

time = datetime.time(12, 30, 0)                # time object in hours, mins and seconds order
print(time)

now = datetime.datetime.now() # Current time
now = now.strftime("%H:%M:%S  %d-%m-%Y") # To format the string's appearance
print(now)

# QN: Check and see if the current date and time has passed a target date and time
import datetime
target_datetime = datetime.datetime(2030, 1, 2, 12, 30 ,1)   ####ERROR!
current_datetime = datetime.datetime.now()

if current_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")  

                                        # ALARM CLOCK
import time # because we will be updating our clock every second
import datetime # To work with string representations of a time
import pygame # To work with sound effects  NB: pip is python package manager

def set_alarm(alarm_time):  # alarm time parameter is going to be a string representation of a time
    print(f"Alarm set for {alarm_time}")
    sound_file = "Sound The Alarm - TrackTribe.mp3"
    is_running = True

    while is_running:
         current_time = datetime.datetime.now().strftime("%H:%M:%S")
         print(current_time)

         if current_time == alarm_time:
              print("WAKE UP!😴😫")

              pygame.mixer.init()   # init is another way to call the constructor e.g  frequency, size, buffer, channels, device name, allowed changes....
              pygame.mixer.music.load(sound_file)
              pygame.mixer.music.play()  #  our sound file originally stops playing when the sound file terminates
              
              while pygame.mixer.music.get_busy():
                   time.sleep(1)


              is_running = False

         time.sleep(1)


if __name__ =="__main__": # To start this program if running main python file directly
     alarm_time = input("Enter the alarm time(HH:MM:SS): ")
     set_alarm(alarm_time)

                                      # MULTI-THREADING
# Used to perform multiple tasks concurrently (multitasking). 
# Good for I/O bound tasks like reading files or fetching data from APIs threading. (Things that take some time and we don't know when they will end exactly)
# Thread(target=my_function)         (calling the threading constructor)  then later we shall pass in threading function

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

#walk_dog()
#take_out_trash()
#get_mail()
# These functions are running on the same thread, our main python program hence we have to complete these chores in order one by one.

chore1 = threading.Thread(target=walk_dog, args=("Scooby","Doo"))   # thread 1   #Thread is an object   # in args() is a tuple 
chore1.start()                                                 # the tuple must be ended with a comma if it has only one argument if not it gives an error assuming we no longer have a tuple

chore2 = threading.Thread(target=take_out_trash)   # thread 2
chore2.start()

chore3 = threading.Thread(target=get_mail)   # thread 3
chore3.start()
# We are executing these functions concurrently(sametime/multitasking). They finished in a different order

chore1.join() # the join method is used to wait for all threads to finish before continuing with the rest of the program
chore2.join()
chore3.join()
print("All chores are complete!")


# NB: When constructing a thread object and we have a key word argument of target, if some of these functions take parameters(accepts argument) e.g first ,
# then we shall need one more keyword argument which is args 
'''









