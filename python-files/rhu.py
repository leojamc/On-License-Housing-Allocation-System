#CODE BY LEO MCCAFFERTY W24046037
#rhu.py

from location_handling import ContactInfo

class Beds:
    """
    Class specifically for storing info about beds and holding bed related
    
    Attributes:
        cost_per_bed (float): Cost per bed of housing RHU's e.g "45.60"
        capacity (int): Number of beds in total e.g "500"
        overflow (int): Number of emergency capacity/overflow beds e.g "25"
        short_term_beds (int): Number of shirt-term beds in the RHU e.g "100"
    """
    def __init__(self, cost_per_bed: float, capacity: int, overflow: int, short_term_beds: int): #Initialiser for Beds
        self.__cost_per_bed = cost_per_bed
        self.__capacity = capacity
        self.__overflow = overflow
        self.__short_term_beds = short_term_beds
    def get_cost_per_bed(self): #Getter for cost_per_bed
        return self.__cost_per_bed
    def set_cost_per_bed(self, new_cost_per_bed): #Setter for cost_per_bed
        assert type(new_cost_per_bed) == float, "Setting cost per bed failed because input type wasn't a float" #Checks that input is a float
        self.__cost_per_bed = new_cost_per_bed
    def get_capacity(self): #Getter for capacity
        return self.__capacity
    def set_capacity(self, new_capacity):
        assert type(new_capacity) == int, "Setting capacity failed because input type wasn't an integer" #Checks that the input is an integer
        self.__capacity = new_capacity
    def get_overflow(self): #Getter for overflow
        return self.__overflow
    def set_overflow(self, new_overflow):
        assert type(new_overflow) == int, "Setting overflow failed because input type wasn't an integer" #Checks that the input is an integer
        self.__overflow = new_overflow
    def get_short_term_beds(self): #Getter for capacity
        return self.__short_term_beds
    def set_short_term_beds(self, new_short_term_beds):
        assert type(new_short_term_beds) == int, "Setting short_term_beds failed because input type wasn't an integer" #Checks that the input is an integer
        self.__short_term_beds = new_short_term_beds
    def calculate_cost(self, number_of_active_licensees):
        """
        Method for calculating total cost of RHU

        Arguments:
            self (Beds): Self object
            number_of_active_licensees (int): Number of licensees currently staying at RHU

        Example:
            self.__cost_per_bed = 45.32
            number_of_active_licensees = 101

            cost = 45.32 * 101 = 4577.32
            return 4577.32
        """
        assert type(number_of_active_licensees) == int, "Input for calculate_cost is not integer" #Checks input is integer
        cost = self.__cost_per_bed*number_of_active_licensees #Calculates cost by multiplying cost per bed by number of licensees staying in the rhu
        return cost
class RHU:
    """
    Class for handling information related to RHU's (Rehabilitating Housing Units)

    Attributes:
        contact_details (ContactDetails class)
        management (str): Management in charge of the RHU with email in the form NAME/EMAIL e.g "MGMT/mgmg@mgmg.com
        licensee_list (list): List of licensee ID's for licensee's currently staying in the RHU e.g ["RHF56", "RHDH56" ...]
        notes (list): List of notes related to the RHU
    """
    def __init__(self, location: list, location_type: str, address: str, phone: str, email: str, contact: str, management: str, licensee_list: list, notes: list): #Initialiser for RHU
        self.__contact_details = ContactInfo(location, location_type, address, phone, email, contact)
        self.__management = management
        self.__licensee_list = licensee_list
        self.__notes = notes
    def get_contact_details(self): #Getter for contact_details
        return self.__contact_details
    def set_contact_details(self, updated_contact_details): #Setter for contact details
        assert type(updated_contact_details) == ContactInfo, "Contact details set failed, input not in type ContactInfo class"
        self.__contact_details = updated_contact_details
    def get_management(self): #Getter for management
        return self.__management
    def set_management(self, new_management): #Setter for management
        assert type(new_management) == list, "Management set failed, input type not string" #Checks input type is string
    def get_licensee_list(self): #Getter for licensee_list
        return self.__licensee_list
    def add_licensee(self, new_licensee_id): #Adds a new licensee to the list
        assert type(new_licensee_id) == str, "Add_licensee failed because input was not type str" #Checks input type is string
        self.__licensee_list.append(new_licensee_id)
    def remove_licensee(self, licensee_id_to_remove): #Removes a licensee from the list
        assert type(licensee_id_to_remove) == str, "Remove licensee failed because input type was not str" #Checks input type is string
        assert self.__licensee_list.find(licensee_id_to_remove) != -1, "Remove licensee failed because licensee id not found in licensee_list" #Checks licensee id is in licensee_list
        self.__licensee_list.remove(licensee_id_to_remove) #Removes licensee from list
    def get_notes(self): #Getter for notes
        return self.__notes
    def add_note(self, new_note): #Adds note to notes
        assert type(new_note) == str, "Add note failed because input is not string type" #Checks input is string type
        self.__notes.append(new_note) #Adds note
    def remove_note(self, note_index): #Removes note at specified index
        assert type(note_index) == int, "Remove note failed because input is not int type" #Checks input is int type
        assert note_index < len(self.__notes), "Remove note failed because index is outside notes list" #Checks if index specified is valid
        self.__notes.pop(note_index) #Removes note at specified index