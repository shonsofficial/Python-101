'''
                            # HOW TO CONNECT TO AN API USING PYTHON (We are going to connect to a pokemon api to get some info on a pokemon of our choosing)
# In this api, we can look up a pokemon such as pikachu, we can get the stats(name,height,id number,moves and abilities) 

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

                                 # PYQT5 GUI INTRODUCTION
import sys # system module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel # first is a package and second is a module.  Widgets are the building blocks of a pyqt5 application. Q distinguishes them from other widgets
# QApplication & QMainWindow are widgets   # Qlabel class is used for label widgets for text or images display
from PyQt5.QtGui import QIcon


# Boiler plate code
class MainWindow(QMainWindow): # We are inheriting from the parent Qmainwindow
    def __init__(self):    # constructor
        super().__init__()              # To pass any arguments to the parent window
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(600,300,500,500) # (x, y, width, height)
        self.setWindowIcon(QIcon("Hd Car.jpg"))     # NB: self is an object, setWindowIcon is a method     # To create an icon 

def main():  # We will call this main function to begin this application
    app = QApplication(sys.argv)   # QApplication is a class    # sys.argv meaning arguments sys-->module which allows PyQt5 to process any command line arguments intended for it.
                                   # That is if we use command prompt or terminal
    window = MainWindow()   # The default behaviour of a window is to hide it.   # Window is an object
    window.show()    # To show the window
    sys.exit(app.exec_())  # To ensure that the window stays until we interact with it or close it. app.exec_ waits around for user input, handles events e.g click buttons, press keys or close the window 

if __name__ == "__main__":        # Run only if we are running this program directly
    main()
'''
                                # PYQT5 LABELS
import sys # This module provides access to variables used and maintained by the python interpreter
# from QtWidgets module, widgets are the building blocks of a pyQt5 application
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel # Qlabel class is used to create label widgets for displaying text or images 
from PyQt5.QtGui import QFont # To work with fonts
from PyQt5.QtCore import Qt# To work with alignments

# Boiler plate code to get the app up and running
class MainWindow(QMainWindow): # inheriting from the parent window
    def __init__(self):
        super().__init__() 
        self.setGeometry(600,300,500,500)

        label = QLabel("Hello", self)   # label object  # Self refers to MainWindow() aka window which will be a parent widget
        label.setFont(QFont("Arial", 40))  # first argument is font type & second is font size
        label.setGeometry(0, 0, 500, 100) # (x, y, width, height)
        label.setStyleSheet("color: 292929;"
                             "background-color: #6fdcf7;"
                               "font-weight: bold;"
                               "font-style: italic;"
                               "text-decoration: underline;") # NB: PyQt5 has styles very similar to css # You can also use RGB values or hexadecimal values to be very specific
        #label.setAlignment(Qt.AlignTop)  # This will align text vertically to the top
        #label.setAlignment(Qt.AlignBottom) # This will align text vertically to the bottom
        #label.setAlignment(Qt.AlignVCenter) # This will align text vertically to the center which it was originally
        #label.setAlignment(Qt.AlignRight) # This will align text horizontally to the right
        #label.setAlignment(Qt.AlignHCenter) # This will align text horizontally to the center
        #label.setAlignment(Qt.AlignLeft) # This will align text horizontally to the left
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  # |(or bitwise operator) allows us to combine flags    # aligning horizontally center and vertically top
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)  # aligning horizontally center and vertically bottom
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # aligning horizontally center and vertically center
        #label.setAlignment(Qt.AlignCenter) # same(shortcut) of (Qt.AlignHCenter | Qt.AlignVCenter)  # aligning horizontally center and vertically center


        
def main():
    app = QApplication(sys.argv) # sys.argv argument allows pyQt to processs any CLI arguments intended for it if we use cmd prompt or terminal not now but someday in the future (Future-proofing our code) 
    window = MainWindow() 
    window.show()    
    sys.exit(app.exec_()) 

if __name__ == "__main__": 
    main()

















