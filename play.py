'''
def holiday_celebration(name, age, time, phone):
    print(f"Happy holidays to you {name}")
    print(f"You are officially {age} years old")
    print(f"Your holidays are for {time} weeks")
    print(f"Your mobile number is {phone}")
    print()
holiday_celebration("Peter",20,6,+8123456789)
holiday_celebration("Paul",39,5,+4342356789)
holiday_celebration("Sarah",34,7,+5776756789)
holiday_celebration("Diana",23,9,+34542656789)
holiday_celebration("Jules",35,3,+4656566789)
'''
'''
import time
def count(start,end):
    for x in range(start,end+1): # It is because the second argument is exclusive
       print(x)
       time.sleep(1)
    print("DONE!")
#count(15,30)   # Also try (30,15)

doubles =[]
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

doubles = [x*2 for x in range(1,11)]
print(doubles)

fruits =["apple","orange","banana","coconut"]
fruits =[fruits.upper() for fruit in fruits]
print(fruits)

grades =[85,42,79,90,56,61,30]
passing_grades =[grade for grade in grades if grade>=60]
print(passing_grades)


foods =[]
prices =[]
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        print("Bye!. Thank you for using our program.")
        break
    elif food == "":
        print("Food name cannot be blank. Please enter a valid food name.")
        continue
    elif food.isdigit():
        print("Food name should not be a number. Please enter a valid food name.")
        continue
    else:
        price = float(input(f"Enter the price of a {food}:$ "))
        foods.append(food)
        prices.append(price)
        print("----------------Your Cart----------------")
        for food in foods:
            print(food, end =", ")
        for price in prices:
            total+=price
        print() # for new line of price
    print(f"Your total is: ${total}")


                  # SUBSTITUTION CYPHER ENCRYPTION PROGRAM
# We are going to replace every instance of the character to hide the message chosen at random and using the same key to decrypt the message.   
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
print()
cipher_text_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text+=chars[index]
print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
print("Thank you for using our program!")
print("********************************")
print()
'''

# How to connect to an API using python i.e poke API in this example to get some pokemon info of our choosing
# In this API, we can look up a pokemon such as pikachu and get the stats like name, height ,id number, moves and abilities

import requests # to make an api request 
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name): 
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url) # This method is going to return a response object which is assigned to response
    
    if response.status_code == 200:
        #print(response) # The output is an http status code which means the response was okay
        #print("Data retrieved!") 
        pokemon_data = response.json() # Our response is a json format, using this method, we will convert it to a python dictionary consisting of key value pairs much like a json file
                #print(pokemon_data)
        return pokemon_data

    else:
        print(f"Failed to retrieve data {response.status_code}")

#pokemon_name = "pikachu"
pokemon_name = "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name) # parameters can be named different than your arguments, when you send data to a function, you can rename it to something else

if pokemon_info:  #boolean
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")











