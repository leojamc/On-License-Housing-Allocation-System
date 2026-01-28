#CODE BY LEO MCCAFFERTY W24046037
#rhu.py
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
        location (RHULocation class): Co-ordinate location of the RHU
        address (str): Address in the format Building num/City/Postcode e.g "23 Cavendish Road/Newcastle upon Tyne/ NE2 1TZ"
        phone (str): Phone number for the RHU in the format +00PHONENUMBER e.g +4402994325092
        email (str): Email address for the RHU e.g rhu@rhu.com
        contact (str): Person to contact in regards to the RHU e.g "Leo McCafferty"
        management (str): Management in charge of the RHU with email in the form NAME/EMAIL e.g "MGMT/mgmg@mgmg.com
        licensee_list (list): List of licensee ID's for licensee's currently staying in the RHU e.g ["RHF56", "RHDH56" ...]
        notes (list): List of notes related to the RHU
    """
    def __init__(self):
        pass