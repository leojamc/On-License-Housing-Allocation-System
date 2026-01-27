#CODE BY LEO MCCAFFERTY W24046037
#location_handling.py
#File used for holding classes and methods related to location based services

#Co-ordinate description:
#Location is represented as a co-ordinate on a 2d topdown map of the area covered by the AO (in the case of this trial, area is greater Durham) which should include all RHU's and licensees affected
#Co-ordinates come in 3 types: Licensee, RHU (Rehabilitating Housing Units) and POI (Places of interest, e.g schools, other people)
#Only Licensees and RHU covered by the AO should appear on this area map, meaning they should always have positive co-ordinates, however POI's outside of the AO's coverage may be included if within 20 miles due to exclusion zones
#Note that a secondary set of co-ordinates is present although will default at (0,0), this is so that when the system is scaled outside of its pilot, each location can have a co-ordinate on an entire map of the UK, though this system is not included in this code yet as it is not required nor necessary for the pilot
#The map used for this trial has the origin set at 54.734506, -1.625365   It extends 7 miles both in positive X and Y and has the ratio of 100:1 co-ordinate:miles

class Region_Info:
    """
    Contains the relevant information for the regional co-ordinates system
    
    Attributes:
        area (str): Name of area covered e.g "Durham"
        miles_ratio (float): Number of co-ordinates distance per mile e.g 100.0
        AO (str): Name of AO for region e.g "James Mart"
        boundary_x (float): End of region map on x-axis represented by co-ordinate distance e.g "700.0"
        boundary_y (float): End of region map on y-axis represented by co-ordinate distance e.g "700.0"
    """
    def __init__(self, area: str, miles_ratio: float, AO: str, boundary_x: float, boundary_y: float): #Initiator for region_info
        self.__area = area
        self.__miles_ratio = miles_ratio
        self.__AO = AO
        self.__boundary_x = self.miles_to_co_ordinates(boundary_x) #Use of miles_to_co_ordinates() is because input is expected to be in miles but needs to be stored as co-ordinates distance
        self.__boundary_y = self.miles_to_co_ordinates(boundary_y) #Use of miles_to_co_ordinates() is because input is expected to be in miles but needs to be stored as co-ordinates distance
    
    def get_area(self): #Getter for area attribute. Note there is no setter for area attribute as it should not be changed as it acts as an ID
        return self.__area
    def get_miles_ratio(self): #Getter for miles_ratio attribute. Note there is no setter for miles_ratio attribute as changing it would result in a domino effect messing up co-ordinates
        return self.__miles_ratio
    def get_AO(self): #Getter for AO attribute
        return self.__AO
    def set_AO(self, new_AO): #Setter for AO attribute, takes string input
        assert type(new_AO) == str, "Setting for AO failed as input wasn't type string" #Checks input is string type
        self.__AO = new_AO
    def get_boundary_x(self): #Getter for boundary_x attribute
        return self.__boundary_x
    def set_boundary_x(self, new_boundary_x):
        assert type(new_boundary_x) == float, "Setting for boundary-x failed as input wasn't type float" #Checks input is float type
    def get_boundary_y(self): #Getter for boundary_y attribute
        return self.__boundary_y
    def set_boundary_y(self, new_boundary_y):
        assert type(new_boundary_y) == float, "Setting for boundary-y failed as input wasn't type float" #Checks input is float type
    
    def miles_to_co_ordinates(self, miles):
        """
        Returns the co-ordinate equivalent distance of the miles inputted
        
        Arguments:
            self (Region_Info class): Needs self to utilise miles_ratio attribute
            miles (float): Miles to be converted into co-ordinate distance

        Example:
            miles = 15
            miles_ratio = 100

            returns 15 * 100 = 1500
        """
        assert type(miles) == float, "Converting miles to co-ordinates failed as input wasnt in float type"
        co_ordinate_distance = miles*self.__miles_ratio #Multiplies miles input by miles_ratio to find new co-ordinate distance equivalent
        return co_ordinate_distance

class Location:
    """
    Class for holding generic location data

    Attributes:
        X (float): A number representing the precise X co-ordinate of the item relative to the area covered
        Y (float): A number representing the precise Y co-ordinate of the item relative to the area covered
        X_nw (float): A number representing the precise X co-ordinate of the item relative to the UK (currently unused)
        Y_nw (float): A number representing the precise Y co-ordinate of the item relative to the UK (currently unused)
    """
    def __init__(self, X: float, Y: float): #Initialiser for Location
        self.__X = X
        self.__Y = Y
        self.__X_nw = 0 #Unused for this trial, will interact with method to convert AO co-ordinated to nationwide co-ordinates when in use
        self.__Y_nw = 0 #Same as above
    def __repr__(self): #Defines what the class should return when called
        return f"[{self.__X, self.__Y}]" #Returns a string containing the co-ordinates e.g [1.2342, 21.8327]
    def get_co_ordinates(self): #Getter for co-ordinates, returns them as a list with x being in index 0 and y being in index 1
        return [self.__X, self.__Y]
    def set_co_ordinates(self, new_co_ordinates): #Setter for co-ordinates, takes input as a list containing [X, Y]
        assert type(new_co_ordinates) == list, "Setting co-ordinates failed as input not in list type" #Checks set input is in list type
        assert len(new_co_ordinates) == 2, "Setting co-ordinates failed as input does not contain only 2 values" #Checks set input only has 2 values
        assert type(new_co_ordinates[0]) == float, "Setting co-ordinates failed as X value is not a float" #Checks set input for X is a float
        assert type(new_co_ordinates[1]) == float, "Setting co-ordinates failed as Y value is not a float" #Checks set input for Y is a float
        self.__X = new_co_ordinates[0]
        self.__Y = new_co_ordinates[1]
    def nudge_location(self, nudge_distance):
        """
        Changes co-ordinates by amount inputter
        
        Arguments:
            self (Region_Info class): Needs Location class to change co-ordinate accordingly
            nudge_distance (list): The amount in co-ordinate distance that the co-ordinates will be changed by, can be negative e.g [1.3456, -5.7689]

        Example:
            co_ordinates = [13.4534, 378.9123]
            nudge_distance = [1.6439, -5.2133]

            X = 13.4534 + (1.6439)
            X = 15.0973
            Y = 378.9123 + (-5.2133)
            Y = 373.699 
        """
        assert type(nudge_distance) == list, "Co-ordinate nudge failed because input type is not list" #Checks input is list type
        assert len(nudge_distance) == 2, "Co-ordinate nudge failed because length of co-ordinate list is not 2" #Checks that input list has length 2
        assert type(nudge_distance[0]) == float, "Co-ordinate nudge failed because x co-ordinate is not type float" #Checks that x co-ordinate is type float
        assert type(nudge_distance[1]) == float, "Co-ordinate nudge failed because y co-ordinate is not type float" #Checks that y co-ordinate is type float
        self.__X += nudge_distance[0]
        self.__Y += nudge_distance[1]

class LicenseeLocation(Location):
    """
    Class for holding location data specific to a licensee, inherits from Location

    Attributes:
        Inherits all attributes from Location
        licensee_location_status (str): The status of the location of the licensee, either "Prison", "Home" or "RHU"
        
    """

