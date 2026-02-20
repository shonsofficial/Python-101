'''
# How to connnect to an API using python
import requests # To make requests to API

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url) # response is a response object which the get method returns
    #print(response)

    if response.status_code == 200: # status_code is an attribute
        #print("Data retrieved!")
        pokemon_data = response.json()  # json method to convert it to a python dictionary(key value pairs like a json file)
        #print(pokemon_data)
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name) # pokemon_name is an attribute

if pokemon_info: # if our dictionary exists
    print(f"Name: {pokemon_info["name"].capitalize()}") # Using a key to access the value of a dictionary
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")



                                # PYQT5 (GUI) -  Creating a basic window
# pip install PyQt5
import sys # This module provides access to variables used and maintained by the python interpreter and to functions that interact strongly with the interpreter
from PyQt5.QtWidgets  import QApplication, QMainWindow # widgets are the building blocks of a pyqt5 application
from PyQt5.QtGui import QIcon # To work with icons

# Boiler plate code to get app up and running
class MainWindow(QMainWindow): # Inheriting from the main class qmainwindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First Cool GUI APP")
        self.setGeometry(700, 300, 500, 500) # Setting the geometry of where the window first appears and the size of the window # (x, y, width, height)
        self.setWindowIcon(QIcon("D:\IT\PROGRAMMING LANGUAGES\PYTHON\Python Full Course - Bro Code\Hd Car.jpg"))

def main():
    app = QApplication(sys.argv) # creating an app object, calling the constructor for QApplication # sys.argv allows pqt to process any command line arguments intended for it if we use command prompt or terminal
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__": # If we are runnning this function directly, call the function of main to begin
    main()


                                                # PYQT5 - Creating Labels
import sys
from PyQt5.QtWidgets  import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont # For fonts
from PyQt5.QtCore import Qt # For positioning / Alignment

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First Cool GUI APP")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("D:\IT\PROGRAMMING LANGUAGES\PYTHON\Python Full Course - Bro Code\Hd Car.jpg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Comic Sans", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: gray;" "background-color: #6fdcf7;" "font-weight: bold;" "font-style: italic;") # "text-decoration: underline;"

        #label.setAlignment(Qt.AlignTop) # Vertically Top
        #label.setAlignment(Qt.AlignBottom) # Vertically Bottom
        #label.setAlignment(Qt.AlignVCenter) # Vertically Center (Original Position)
        #label.setAlignment(Qt.AlignRight) # Horizontally Right
        #label.setAlignment(Qt.AlignHCenter) # Horizontally Center
        #label.setAlignment(Qt.AlignLeft) # Horizontally Left

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Center & Top
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Center & Bottom
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Center & Center
        #label.setAlignment(Qt.AlignCenter) # Center & Center


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
'''

                                        # PYQT5 IMAGES
import sys
from PyQt5.QtWidgets  import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First Cool GUI APP")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("D:\IT\PROGRAMMING LANGUAGES\PYTHON\Python Full Course - Bro Code\Hd Car.jpg"))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()