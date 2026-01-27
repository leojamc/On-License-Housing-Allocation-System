#CODE BY LEO MCCAFFERTY W24046037
#licensee.py
#File used for holding classes and methods relating to licensee information

import datetime

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
        name (str): Licensee name, "John Doe" if no name given e.g "John Doe"
        home_address (str): Licensee home address, stored as a string e.g "12 Northumberland Street/Newcastle upon Tyne/NE1 5GH"
        location (Location class): Licensee location, stored as an instance of location class
        estimated_license_end (datetime.date): Date license is expected to end "2026-04-23"
        notes (list): List comprised of strings, containing notes related to the licensee e.g ["Note1", "Note2"...]
        category (str): One of 3 categories, "pending", "allocated" or "exited" e.g "pending"
        photo (Photo class): Photo of licensee, stored as an instance of the photo class
    """
    def __init__(self):
        __name = 
 