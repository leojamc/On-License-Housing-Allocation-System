#CODE BY LEO MCCAFFERTY W24046037
#pyside6_main.py
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit, QDialog, QDialogButtonBox, QLabel, QStackedLayout, QHBoxLayout

import main
from main import check_login

class MainWindow(QMainWindow):
    """
    Subclass of PySide6's QMainWindow
    """
    def __init__(self):
        super().__init__() #Calls initialiser for QMainWindow to initialise all its attributes

        self.setWindowTitle("On License Housing Allocation System") #Sets the title for the application
        self.setFixedSize(QSize(1200, 600)) #Sets the screen size

        self.stacklayout = QStackedLayout()
        self.__screen = "login"
        self.create_window()

    def create_window(self):
        self.stacklayout = QStackedLayout()

        #LOGIN SCREEN
        self.__login_menu = LoginScreen()
        self.__login_menu.login_button.clicked.connect(self.__login_menu.button_click)
        self.stacklayout.addWidget(self.__login_menu.get_widget())

        self.__main_menu = MainMenu()
        self.stacklayout.addWidget(self.__main_menu.get_widget())

        if self.__screen == "login":
            self.stacklayout.setCurrentIndex(0)
        elif self.__screen == "main":
            self.stacklayout.setCurrentIndex(1)
        widget = QWidget()
        widget.setLayout(self.stacklayout)
        self.setCentralWidget(widget)
    
    def update_window(self, new_screen):
        self.__screen = new_screen
        self.create_window()


class ErrorMessage(QDialog):
    """
    Class for handling error message windows
    """
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Error")
        self.__error_message = "Error"
    def change_message(self, new_message):
        self.__error_message = new_message
        self.set_layout()
 
    def set_layout(self):
        QBtn = (QDialogButtonBox.Ok)
        self.popup = QDialogButtonBox(QBtn)
        self.popup.accepted.connect(self.accept)
        layout = QVBoxLayout()
        error_message = QLabel(self.__error_message)
        layout.addWidget(error_message)
        layout.addWidget(self.popup)
        self.setLayout(layout)     

class LoginScreen():
    """
    Holds The login screen widgets and functionality
    """
    def __init__(self):
        self.__layout = QVBoxLayout()
        self.login_box = QLineEdit()
        self.login_box.setPlaceholderText("Enter password")

        self.login_button = QPushButton("Login") #Creates a button with the text login
        
        self.__layout.addWidget(self.login_box)
        self.__layout.addWidget(self.login_button)

        self.__widget = QWidget()
        self.__widget.setLayout(self.__layout)
    def button_click(self):
        if check_login(self.login_box.text()) == True:
            print("Correct")
            window.update_window("main")
        else:
            popup = ErrorMessage()
            popup.change_message("Invalid Password")
            popup.exec()

    def get_widget(self):
        return self.__widget

class MainMenu():
    """
    Holds the main menu widgets and functionality
    """
    def __init__(self):
        #Parent layou
        self.__layout = QVBoxLayout()

        title = QLabel("MAIN MENU")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.__layout.addWidget(title)

        #Sub layout for buttons
        self.__layout2 = QHBoxLayout()

        #Sub-Sub layout for offender buttons
        self.__data_buttons_layout = QVBoxLayout()
        subtitle = QLabel("Database interaction")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.__data_buttons_layout.addWidget(subtitle)
        register_button = QPushButton("Register Offender")
        edit_offender = QPushButton("Edit Offender Details")
        rhu_button = QPushButton("Register new RHU")
        edit_rhu_button = QPushButton("Edit existing RHU")
        poi_button = QPushButton("Register new POI")
        edit_poi_button = QPushButton("Edit existing POI")
        self.__data_buttons_layout.addWidget(register_button)
        self.__data_buttons_layout.addWidget(edit_offender)
        self.__data_buttons_layout.addWidget(rhu_button)
        self.__data_buttons_layout.addWidget(edit_rhu_button)
        self.__data_buttons_layout.addWidget(poi_button)
        self.__data_buttons_layout.addWidget(edit_poi_button)
        data_buttons_widget = QWidget()
        data_buttons_widget.setLayout(self.__data_buttons_layout)

        #Sub-sub layout for data viewing buttons
        self.__view_data_layout = QVBoxLayout()
        subtitle = QLabel("License conditions")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.__view_data_layout.addWidget(subtitle)
        licensee_conditions_button = QPushButton("View Licensee's License Conditions")
        edit_licensee_conditions_button = QPushButton("Edit Licensee's License Condtitions")
        self.__view_data_layout.addWidget(licensee_conditions_button)
        self.__view_data_layout.addWidget(edit_licensee_conditions_button)
        view_data_widget = QWidget()
        view_data_widget.setLayout(self.__view_data_layout)

        #Sub-sub layout for housing allocation buttons
        self.__housing_allocation = QVBoxLayout()
        subtitle = QLabel("Licensee Housing allocation")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.__housing_allocation.addWidget(subtitle)
        view_housing_button = QPushButton("View Suitable housing")
        assign_housing_button = QPushButton("Assign housing")
        transfer_button = QPushButton("Transfer Licensee")
        self.__housing_allocation.addWidget(view_housing_button)
        self.__housing_allocation.addWidget(assign_housing_button)
        self.__housing_allocation.addWidget(transfer_button)
        housing_allocation_widget = QWidget()
        housing_allocation_widget.setLayout(self.__housing_allocation)

        #Sub-sub layout for Historical records
        self.__historical_records = QVBoxLayout()
        subtitle = QLabel("Historical Records")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.__historical_records.addWidget(subtitle)
        view_records_button = QPushButton("View Historical Records")
        edit_records_button = QPushButton("Edit Historical Records")
        self.__historical_records.addWidget(view_records_button)
        self.__historical_records.addWidget(edit_records_button)
        historical_records_widget = QWidget()
        historical_records_widget.setLayout(self.__historical_records)

        #Sub-sub layout for Report Generation
        self.__report_generation = QVBoxLayout()
        subtitle = QLabel("Report Generation")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.__report_generation.addWidget(subtitle)
        licensee_report_button = QPushButton("Licensee Report")
        rhu_report_button = QPushButton("RHU Report")
        poi_report_button = QPushButton("POI Report")
        self.__report_generation.addWidget(licensee_report_button)
        self.__report_generation.addWidget(rhu_report_button)
        self.__report_generation.addWidget(poi_report_button)
        report_generation_widget = QWidget()
        report_generation_widget.setLayout(self.__report_generation)

        self.__layout2.addWidget(data_buttons_widget)
        self.__layout2.addWidget(view_data_widget)
        self.__layout2.addWidget(housing_allocation_widget)
        self.__layout2.addWidget(historical_records_widget)
        self.__layout2.addWidget(report_generation_widget)

        widget = QWidget()
        widget.setLayout(self.__layout2)
        self.__layout.addWidget(widget)

        self.__widget = QWidget()
        self.__widget.setLayout(self.__layout)
    def get_widget(self):
        return self.__widget
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()