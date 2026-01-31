#CODE BY LEO MCCAFFERTY W24046037
#pyside6_main.py
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit, QDialog, QDialogButtonBox, QLabel, QStackedLayout, QHBoxLayout, QDateEdit, QCheckBox, QComboBox, QTableWidget, QTableWidgetItem

import main
import datetime
from main import check_login
from data_handling import register_offender, edit_offender, query_line, find_in, get_ID, set_ID, register_rhu, edit_rhu

offender_id_storage = ""
licensee_list_storage = ["", datetime.date(2000, 2, 2), "", "", "", datetime.date(2000, 2, 2)]
contact_list_storage = [0, "", "", "", "", 0, ""]

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
        self.__main_menu.register_button.clicked.connect(self.__main_menu.click_register_offender)
        self.__main_menu.edit_offender.clicked.connect(self.__main_menu.click_edit_offender)
        self.__main_menu.rhu_button.clicked.connect(self.__main_menu.click_register_rhu)

        self.stacklayout.addWidget(self.__main_menu.get_widget())

        self.__register_offender = registerOffender()
        self.__register_offender.submit_button.clicked.connect(self.__register_offender.click_submit)
        self.__register_offender.back_button.clicked.connect(self.__register_offender.click_back)
        self.stacklayout.addWidget(self.__register_offender.get_widget())

        self.__edit_offender = editOffender()
        self.__edit_offender.submit_button.clicked.connect(self.__edit_offender.click_submit)
        self.__edit_offender.back_button.clicked.connect(self.__edit_offender.click_back)
        self.stacklayout.addWidget(self.__edit_offender.get_widget())

        self.__register_rhu = registerRHU()
        self.__register_rhu.submit_button.clicked.connect(self.__register_rhu.click_submit)
        self.__register_rhu.back_button.clicked.connect(self.__register_rhu.click_back)
        self.stacklayout.addWidget(self.__register_rhu.get_widget())


        if self.__screen == "login":
            self.stacklayout.setCurrentIndex(0)
        elif self.__screen == "main":
            self.stacklayout.setCurrentIndex(1)
        elif self.__screen == "register_offender":
            self.stacklayout.setCurrentIndex(2)
        elif self.__screen == "edit_offender":
            self.stacklayout.setCurrentIndex(3)
        elif self.__screen == "register_rhu":
            self.stacklayout.setCurrentIndex(4)
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

class MainMenu:
    """
    Holds the main menu widgets and functionality
    """
    def __init__(self):
        #Parent layout
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
        self.register_button = QPushButton("Register Offender")
        self.edit_offender = QPushButton("Edit Offender Details")
        self.rhu_button = QPushButton("Register new RHU")
        self.edit_rhu_button = QPushButton("Edit existing RHU")
        poi_button = QPushButton("Register new POI")
        edit_poi_button = QPushButton("Edit existing POI")
        self.__data_buttons_layout.addWidget(self.register_button)
        self.__data_buttons_layout.addWidget(self.edit_offender)
        self.__data_buttons_layout.addWidget(self.rhu_button)
        self.__data_buttons_layout.addWidget(self.edit_rhu_button)
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

    def click_register_offender(self):
        window.update_window("register_offender")

    def click_edit_offender(self):
        window.update_window("edit_offender")

    def click_register_rhu(self):
        window.update_window("register_rhu")

    def get_widget(self):
        return self.__widget
    
class registerOffender:
    def __init__(self):
        self.__layout = QVBoxLayout()

        title = QLabel("Register Offender")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.__layout.addWidget(title)

        sub_text1 = QLabel("Prison Release date")
        self.__layout.addWidget(sub_text1)
        self.release_date = QDateEdit()
        self.__layout.addWidget(self.release_date)
        sub_text2 = QLabel("Expected end of license")
        self.__layout.addWidget(sub_text2)
        self.license_end = QDateEdit()
        self.__layout.addWidget(self.license_end)
        self.gender = QLineEdit()
        self.gender.setPlaceholderText("Gender")
        self.__layout.addWidget(self.gender)
        self.sex = QComboBox()
        self.sex.setPlaceholderText("Sex")
        self.sex.addItems(["Male", "Female"])
        self.__layout.addWidget(self.sex)
        self.category = QComboBox()
        self.category.setPlaceholderText("Category")
        self.category.addItems(["pending", "allocated", "exited"])
        self.__layout.addWidget(self.category)
        self.name = QLineEdit()
        self.name.setPlaceholderText("Full Name")
        self.__layout.addWidget(self.name)
        self.address = QLineEdit()
        self.address.setPlaceholderText("Address, HOUSENUM+STREETNAME/CITY/POSTCODE")
        self.__layout.addWidget(self.address)
        self.phone = QLineEdit()
        self.phone.setPlaceholderText("Phone number, LOCATIONCODE0XXXXXXXXXX")
        self.__layout.addWidget(self.phone)
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email address")
        self.__layout.addWidget(self.email)
        self.submit_button = QPushButton("Submit")
        self.__layout.addWidget(self.submit_button)
        self.back_button = QPushButton("Back")
        self.__layout.addWidget(self.back_button)
        #license_end, gender, sex, category, release,  name, address, phone, email
        self.__widget = QWidget()
        self.__widget.setLayout(self.__layout)
    def click_submit(self):
        #Validate here
        licensee_details = [str_to_date(self.release_date.textFromDateTime(self.release_date.dateTime())), self.gender.text(), str(self.sex.currentText()), str(self.category.currentText()), str_to_date(self.license_end.textFromDateTime(self.license_end.dateTime()))]
        contact_details = [self.name.text(), self.address.text(), self.phone.text(), self.email.text()]
        register_offender(licensee_details, contact_details)
        print("Data submitted")
    def click_back(self):
        window.update_window("main")
    def get_widget(self):
        return self.__widget
    
class editOffender:
    def __init__(self):
        self.__layout = QVBoxLayout()

        title = QLabel(f"Edit Offender")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.__layout.addWidget(title)

        self.ID = QLineEdit()
        self.ID.setPlaceholderText("ID")
        self.__layout.addWidget(self.ID)

        sub_text1 = QLabel("Prison Release date")
        self.__layout.addWidget(sub_text1)
        self.release_date = QDateEdit()
        self.__layout.addWidget(self.release_date)
        sub_text2 = QLabel("Expected end of license")
        self.__layout.addWidget(sub_text2)
        self.license_end = QDateEdit()
        self.__layout.addWidget(self.license_end)
        self.gender = QLineEdit()
        self.gender.setPlaceholderText("Gender")
        self.__layout.addWidget(self.gender)
        self.sex = QComboBox()
        self.sex.setPlaceholderText("Sex")
        self.sex.addItems(["Male", "Female"])
        self.__layout.addWidget(self.sex)
        self.category = QComboBox()
        self.category.setPlaceholderText("Category")
        self.category.addItems(["pending", "allocated", "exited"])
        self.__layout.addWidget(self.category)
        self.name = QLineEdit()
        self.name.setPlaceholderText("Full Name")
        self.__layout.addWidget(self.name)
        self.address = QLineEdit()
        self.address.setPlaceholderText("Address, HOUSENUM+STREETNAME/CITY/POSTCODE")
        self.__layout.addWidget(self.address)
        self.phone = QLineEdit()
        self.phone.setPlaceholderText("Phone number, LOCATIONCODE0XXXXXXXXXX")
        self.__layout.addWidget(self.phone)
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email address")
        self.__layout.addWidget(self.email)
        self.submit_button = QPushButton("Submit")
        self.__layout.addWidget(self.submit_button)
        self.back_button = QPushButton("Back")
        self.__layout.addWidget(self.back_button)

        self.__widget = QWidget()
        self.__widget.setLayout(self.__layout)       
    def click_submit(self):
        self.offender_id = self.ID.text()
        self.contact_id = query_line("data/contact.csv", find_in("data/contact.csv", 6, self.offender_id))[0]
        self.location_id = query_line("data/locations.csv", find_in("data/locations.csv", 6, self.contact_id))[2]
        #Validate here
        licensee_details = [self.offender_id, str_to_date(self.license_end.textFromDateTime(self.license_end.dateTime())), self.gender.text(), str(self.sex.currentText()), str(self.category.currentText()), str_to_date(self.release_date.textFromDateTime(self.release_date.dateTime()))] 
        contact_details = [self.contact_id, self.name.text(), self.address.text(), self.phone.text(), self.email.text(), self.location_id, self.offender_id]
        edit_offender(self.offender_id, licensee_details, contact_details)
    def click_back(self):
        window.update_window("main")
    def get_widget(self):
        return self.__widget
    
class registerRHU:
    def __init__(self):
        self.__layout = QVBoxLayout()

        title = QLabel("Register RHU")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.__layout.addWidget(title)

        self.cpb = QLineEdit()
        self.cpb.setPlaceholderText("Cost Per bed")
        self.__layout.addWidget(self.cpb)
        self.capacity = QLineEdit()
        self.capacity.setPlaceholderText("Capacity")
        self.__layout.addWidget(self.capacity)
        self.em_capacity = QLineEdit()
        self.em_capacity.setPlaceholderText("Emergency Capacity")
        self.__layout.addWidget(self.em_capacity)
        self.stb = QLineEdit()
        self.stb.setPlaceholderText("Short Term Beds")
        self.__layout.addWidget(self.stb)
        self.name = QLineEdit()
        self.name.setPlaceholderText("RHU Manager Name")
        self.__layout.addWidget(self.name)
        self.address = QLineEdit()
        self.address.setPlaceholderText("Address, HOUSENUM+STREETNAME/CITY/POSTCODE")
        self.__layout.addWidget(self.address)
        self.phone = QLineEdit()
        self.phone.setPlaceholderText("Phone number, LOCATIONCODE0XXXXXXXXXX")
        self.__layout.addWidget(self.phone)
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email address")
        self.__layout.addWidget(self.email)
        self.co_ord = QLineEdit()
        self.co_ord.setPlaceholderText("Co_ordinates, (XX, XX)")
        self.__layout.addWidget(self.co_ord)
        self.submit_button = QPushButton("Submit")
        self.__layout.addWidget(self.submit_button)
        self.back_button = QPushButton("Back")
        self.__layout.addWidget(self.back_button)
        #license_end, gender, sex, category, release,  name, address, phone, email
        self.__widget = QWidget()
        self.__widget.setLayout(self.__layout)
    def click_submit(self):
        #Validate here
        co_ordinates = self.co_ord.text()
        co_ordinates_list = co_ordinates.split(",")
        rhu_details = [self.cpb.text(), self.capacity.text(), self.em_capacity.text(), self.stb.text()]
        contact_details = [self.name.text(), self.address.text(), self.phone.text(), self.email.text()]
        register_rhu(rhu_details, contact_details, co_ordinates_list)
        print("Data submitted")
    def click_back(self):
        window.update_window("main")
    def get_widget(self):
        return self.__widget
    
class editRHU:
    def __init__(self):
        self.__layout = QVBoxLayout()

        title = QLabel(f"Edit Offender")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.__layout.addWidget(title)

        self.ID = QLineEdit()
        self.ID.setPlaceholderText("ID")
        self.__layout.addWidget(self.ID)

        sub_text1 = QLabel("Prison Release date")
        self.__layout.addWidget(sub_text1)
        self.release_date = QDateEdit()
        self.__layout.addWidget(self.release_date)
        sub_text2 = QLabel("Expected end of license")
        self.__layout.addWidget(sub_text2)
        self.license_end = QDateEdit()
        self.__layout.addWidget(self.license_end)
        self.gender = QLineEdit()
        self.gender.setPlaceholderText("Gender")
        self.__layout.addWidget(self.gender)
        self.sex = QComboBox()
        self.sex.setPlaceholderText("Sex")
        self.sex.addItems(["Male", "Female"])
        self.__layout.addWidget(self.sex)
        self.category = QComboBox()
        self.category.setPlaceholderText("Category")
        self.category.addItems(["pending", "allocated", "exited"])
        self.__layout.addWidget(self.category)
        self.name = QLineEdit()
        self.name.setPlaceholderText("Full Name")
        self.__layout.addWidget(self.name)
        self.address = QLineEdit()
        self.address.setPlaceholderText("Address, HOUSENUM+STREETNAME/CITY/POSTCODE")
        self.__layout.addWidget(self.address)
        self.phone = QLineEdit()
        self.phone.setPlaceholderText("Phone number, LOCATIONCODE0XXXXXXXXXX")
        self.__layout.addWidget(self.phone)
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email address")
        self.__layout.addWidget(self.email)
        self.submit_button = QPushButton("Submit")
        self.__layout.addWidget(self.submit_button)
        self.back_button = QPushButton("Back")
        self.__layout.addWidget(self.back_button)

        self.__widget = QWidget()
        self.__widget.setLayout(self.__layout)       
    def click_submit(self):
        self.offender_id = self.ID.text()
        self.contact_id = query_line("data/contact.csv", find_in("data/contact.csv", 6, self.offender_id))[0]
        self.location_id = query_line("data/locations.csv", find_in("data/locations.csv", 6, self.contact_id))[2]
        #Validate here
        licensee_details = [self.offender_id, str_to_date(self.license_end.textFromDateTime(self.license_end.dateTime())), self.gender.text(), str(self.sex.currentText()), str(self.category.currentText()), str_to_date(self.release_date.textFromDateTime(self.release_date.dateTime()))] 
        contact_details = [self.contact_id, self.name.text(), self.address.text(), self.phone.text(), self.email.text(), self.location_id, self.offender_id]
        edit_offender(self.offender_id, licensee_details, contact_details)
    def click_back(self):
        window.update_window("main")
    def get_widget(self):
        return self.__widget


def str_to_date(str):
    split = str.split("/")
    return datetime.date(int(split[2]), int(split[1]), int(split[0]))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()