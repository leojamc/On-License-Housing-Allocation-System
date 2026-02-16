#CODE BY LEO MCCAFFERTY W24046037
#main.py
"""
Changes made on 16/2/26 include
main.py: File rewritten to facilitate running the project effectively and easily, no project functionality changes
data_creation.py: 1 line changed in the runtime code to change it into a function that can be called from main.py, no project functionality changes
pyside6_main.py: Function check_login() that was originally located in main.py moved to pyside6_main.py to prevent circular import error, no project functionality changes
All changes do not alter scope or functionality or internal workings of the project and are exclusively made to make running the project easier

The project can now (and is recommended to be) exclusively run from this file.
Chnanges made do not add to the scope of the project, and do not include new content from the brief that was not included in the original submission
This new code will check if a data file exists, if not it will run data_creation.py first to generate the data, then run the main program
A toggle is included (generate_data) that when switched to True, will generate a new set of data each time regardless, overwriting any data already there
"""

generate_data = False #Change this to toggle new data creation each time the program is run

import sys
from data_creation import data_generation
from pyside6_main import MainWindow
from PySide6.QtWidgets import QApplication
from pathlib import Path

def check_data_exists():
    path = Path("data/contact.csv")
    if path.exists():
        return True
    else:
        return False
    
#Runtime Code
if generate_data == True or check_data_exists() == False:
    data_generation()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
#