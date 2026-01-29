#CODE BY LEO MCCAFFERTY W24046037
#licensee.py
#File used for holding classes and methods relating to licensee information

import datetime
from location_handling import ContactInfo

class Prison_Info:
    """
    Class representing licensee information regarding prison sentence
    
    Attributes:
        release_date (datetime.date): Date released from prison e.g "2026-01-23"
        ID (str): Role ID from Prison e.g "KJ4GH"
        gender (str): Prison Gender, typically "Man" or "Woman" but stored as a string to accomodate other gender identities e.g "Man"
        sex (str): Prison Sex, either "Male" or "Female" e.g "Male"
    """
    def __init__(self, release_date: datetime.date, ID: str, gender: str, sex: str): #Initialiser for Prison_Info
        self.__release_date = release_date
        self.__ID = ID
        self.__gender = gender
        self.__sex = sex

    def get_ID(self): #Getter for ID attribute, note there is no setter as prison role ID should not change and is pivotal to data systems
        return self.__ID
    def get_release_date(self): #Getter for release_date attribute
        return self.__release_date
    def set_release_date(self, new_release_date): #Setter for release_date, note that under normal circumstances this should not need to be used as licensees will be entered onto the system after their prison release, but incase they aren't this function exists
        assert type(new_release_date) == datetime.date, "Release date set entry not in datetime.date type as required" #Checks that entry for new release date is in correct type
        self.__release_date = new_release_date
    def get_gender(self): #Getter for gender attribute
        return self.__gender
    def set_gender(self, new_gender): #Sets attribute for gender, needed incase licensee identifies to a different gender
        assert type(new_gender) == str, "Gender set entry not in string type as required" #Checks entry for new gender is in string format
        self.__gender = new_gender
    def get_sex(self): #Getter for sex attribute
        return self.__sex
    def set_sex(self, new_sex): #Setter for sex attribute, should not be used under regular circumstances, only incase of data misinput
        assert type(new_sex) == str, "Sex set entry not in string type as required" #Checks entry for new sex is in string format

class Licensee:
    """
    Class representing Licensees

    Attributes:
        contact_info (ContactInfo class): Contains info such as location, home address, email, phone number and name
        estimated_license_end (datetime.date): Date license is expected to end "2026-04-23"
        notes (list): List comprised of strings, containing notes related to the licensee e.g ["Note1", "Note2"...]
        category (str): One of 3 categories, "pending", "allocated" or "exited" e.g "pending"
        photo (Photo class): Photo of licensee, stored as an instance of the photo class
    """
    def __init__(self, name: str, home_address: str, phone: str, email: str, location: list, estimated_license_end: datetime.date, notes: list, category: str, prison_release_date: datetime.date, prison_ID: str, prison_gender: str, prison_sex: str): #Initialiser for licensee
        self.__contact_info = ContactInfo(location, "Licensee", home_address, phone, email, name)
        self.__estimated_license_end = estimated_license_end
        self.__notes = notes
        self.__category = category
        #Photo functionality to be added
    def get_licensee_name(self): #Getter for licensee_name
        return self.__contact_info.get_contact() #Gets name from contact_info
    def set_licensee_name(self, new_name): #Setter for licensee_name
        assert type(new_name) == str, "Set_licensee_name failed because input is not string type" #Checks input is string type
        self.__contact_info.set_contact(new_name)
    def get_contact_info(self): #Getter for contact info
        return self.__contact_info
    def set_contact_info(self, new_contact_info): #Setter for contact info
        assert type(new_contact_info) == ContactInfo, "Set contact info failed because input is not of type ContactInfo class" #Checks input is ContactInfo type
        self.__contact_info = new_contact_info
    def get_estimated_license_end(self): #Getter for estimated license end
        return self.__estimated_license_end
    def set_estimated_license_end(self, new_estimated_license_end):
        assert type(new_estimated_license_end) == datetime.date, "Set estimated license end failed because input not of datetime.date type" #Checks input is datetime.date type
        self.__estimated_license_end = new_estimated_license_end
    def get_notes(self): #Getter for notes
        return self.__notes
    def add_note(self, new_note): #Adds note to notes
        assert type(new_note) == str, "Add note failed because input is not string type" #Checks input is string type
        self.__notes.append(new_note) #Adds note
    def remove_note(self, note_index): #Removes note at specified index
        assert type(note_index) == int, "Remove note failed because input is not int type" #Checks input is int type
        assert note_index < len(self.__notes), "Remove note failed because index is outside notes list" #Checks if index specified is valid
        self.__notes.pop(note_index) #Removes note at specified index
    def get_category(self): #Getter for category
        return self.__category
    def set_category(self, new_category): #Setter for category
        assert type(new_category) == str, "Set category failed because input is not of string type" #Checks if input is of string type
        self.__category = new_category