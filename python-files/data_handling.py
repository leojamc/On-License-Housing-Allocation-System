#CODE BY LEO MCCAFFERTY W24046037
#data_handling.py
from data_creation import generate_ID
import csv
import datetime
import math

temp_ID = ""

def set_ID(new_ID):
    temp_ID = new_ID
def get_ID():
    return temp_ID

def return_table(file_path):
    table_list = []
    file_path = file
    line_no += -1
    with open(file_path, 'r', encoding='utf-8') as file: #Opens file on read mode
        for line_number, line in enumerate(file, start = 1):
            table_list.append(line)              

def read_ID():
    ID_list = []
    with open("data/licensee.csv", 'r', encoding='utf-8') as file: #Opens file on read mode
        for line_number, line in enumerate(file, start = 2):
            line = line.strip() #Strips whitespace from line
            split_line = line.split(",")
            ID_list.append(split_line[0])
    return ID_list

def find_newest_index(file, column):
    with open(file, 'r', encoding='utf-8') as file: #Opens file on read mode  
        for line_number, line in enumerate(file, start = 2):          
            line = line.strip() #Strips whitespace from line
            split_line = line.split(",")
            newest_index = split_line[column]
    return newest_index

def query_line(file, line_no):
    file_path = file
    line_no += -1
    with open(file_path, 'r', encoding='utf-8') as file: #Opens file on read mode  
        for line_number, line in enumerate(file, start = 0):
            if line_number == line_no:
                line = line.strip() #Strips whitespace from line
                split_line = line.split(",")  
                return split_line              

def write_to(file, row):
    file_path = file
    final_list = []
    with open(file_path, 'r', encoding='utf-8') as file: #Opens file on read mode  
        for line_number, line in enumerate(file, start = 1):
            line = line.strip() #Strips whitespace from line
            line_split = line.split(",")
            final_list.append(line_split)        
    final_list.append(row)      
    with open(file_path, "w") as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerows(final_list)

def write_to_specific(file, row, line_to_edit):
    file_path = file
    final_list = []
    line_no = line_to_edit
    with open(file_path, 'r', encoding='utf-8') as file: #Opens file on read mode  
        for line_number, line in enumerate(file, start = 1):
            if line_number == line_no:
                final_list.append(row)
            else:
                line = line.strip() #Strips whitespace from line
                line_split = line.split(",")
                final_list.append(line_split)            
    with open(file_path, "w") as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerows(final_list)

def find_in(file, column, key):
    file_path = file
    found = False
    final_line = 0
    with open(file_path, 'r', encoding='utf-8') as file: #Opens file on read mode 
        for line_number, line in enumerate(file, start = 1):
            line = line.strip() #Strips whitespace from line
            line_split = line.split(",")
            if column > (len(line_split)-1):
                pass
            elif str(line_split[column]) == str(key):
                found = True
                final_line = line_number
    if found == False:
        return -1
    else:
        return final_line
    
def find_in_combo(file, column_1, key_1, column_2, key_2):
    file_path = file
    found = False
    with open(file_path, 'r', encoding='utf-8') as file: #Opens file on read mode 
        for line_number, line in enumerate(file, start = 1):
            line = line.strip() #Strips whitespace from line
            line_split = line.split(",")  
            if line_split[column_1] == key_1 and line_split[column_2] == key_2:
                found = True
                return line                                      
    if found == False:
        return -1

def register_offender(licensee_details, contact_details):
    used_ID = read_ID()
    licensee_id = generate_ID(used_ID)
    license_end = licensee_details[0]
    gender = licensee_details[1]
    sex = licensee_details[2]
    category = licensee_details[3]
    release = licensee_details[4]
    name = contact_details[0]
    address = contact_details[1]
    phone = contact_details[2]
    email = contact_details[3]
    contact_entry = str(int(find_newest_index("data/contact.csv", 0)) + 1)
    licensee_file_entry = [licensee_id, license_end, gender, sex, category, release]
    contact_file_entry = [contact_entry, name, address, phone, email, 1, licensee_id]
    write_to("data/licensee.csv", licensee_file_entry)
    write_to("data/contact.csv", contact_file_entry)

def edit_offender(offender_id, licensee_details, contact_details):
    line_no = find_in("data/licensee.csv", 0, offender_id)
    if line_no >= 2:
        write_to_specific("data/licensee.csv", licensee_details, line_no)
        line_no = find_in("data/contact.csv", 6, offender_id)
        write_to_specific("data/contact.csv", contact_details, line_no)
        return "Success"
    else:
        return "Not found"
    
def register_rhu(rhu_details, contact_details, co_ordinates):
    info_key = str(int(find_newest_index("data/rhu.csv", 0)) + 1)
    cost_per_bed = rhu_details[0]
    capacity = rhu_details[1]
    emergency_capacity = rhu_details[2]
    short_term_beds = rhu_details[3]
    location_key = find_newest_index("data/locations.csv", 0) + 1
    contact_key = find_newest_index("data/contact.csv", 0) + 1
    name = contact_details[0]
    address = contact_details[1]
    phone = contact_details[2]
    email = contact_details[3]
    location_type = "RHU"
    co_ords = co_ordinates
    rhu_file_entry = [info_key, cost_per_bed, capacity, emergency_capacity, short_term_beds, location_key]
    contact_file_entry = [contact_key, name, address, phone, email, location_key]
    location_file_entry = [location_key, location_type, contact_key, co_ords, info_key]
    write_to("data/rhu.csv", rhu_file_entry)
    write_to("data/contact.csv", contact_file_entry)   
    write_to("data/locations.csv", location_file_entry) 

def edit_rhu(rhu_key, rhu_details, contact_details, location_details):
    line_no = find_in("data/rhu.csv", 0, rhu_key)
    if line_no >= 2:
        write_to_specific("data/rhu.csv", rhu_details, line_no)
        location_key = query_line("data/rhu.csv", line_no)[5]
        line_no = find_in("data/locations.csv", 0, location_key)
        write_to_specific("data/locations.csv", location_details, line_no)
        line_no = find_in("data/contact.csv", 5, location_key)
        write_to_specific("data/contact.csv", contact_details, line_no)
        return "Success"
    else:
        return "Not found"
    
def register_poi(poi_details, contact_details, co_ordinates):
    info_key = find_newest_index("data/poi.csv", 0) + 1
    location_key = find_newest_index("data/locations.csv", 0) + 1
    contact_key = find_newest_index("data/contact.csv", 0) + 1
    place_significance = poi_details[0]
    name = contact_details[0]
    address = contact_details[1]
    phone = contact_details[2]
    email = contact_details[3]
    location_type = "POI"
    co_ords = co_ordinates
    poi_file_entry = [info_key, place_significance]
    contact_file_entry = [contact_key, name, address, phone, email, location_key]
    location_file_entry = [location_key, location_type, contact_key, co_ords, info_key]
    write_to("data/poi.csv", poi_file_entry)
    write_to("data/contact.csv", contact_file_entry)   
    write_to("data/locations.csv", location_file_entry) 

def edit_poi(poi_key, poi_details, contact_details, location_details):
    line_no = find_in("data/poi.csv", 0, poi_key)
    if line_no >= 2:
        write_to_specific("data/rhu.csv", poi_details, line_no)
        location_key = find_in_combo("data/locations.csv", 1, "POI", 4, poi_key)[0]
        line_no = find_in("data/locations.csv", 0, location_key)
        write_to_specific("data/locations.csv", location_details, line_no)
        line_no = find_in("data/contact.csv", 5, location_key)
        write_to_specific("data/contact.csv", contact_details, line_no)
        return "Success"
    else:
        return "Not found"
    
def score_closeness(list_of_rhus_co_ords, base_co_ords):
    best_rhu_co_ords = []
    best_dist = 0
    for rhu in list_of_rhus_co_ords:
        dist = math.dist(rhu, base_co_ords)
        if rhu > best_dist:
            best_rhu_co_ords = rhu
            best_dist = dist
    return best_dist, best_rhu_co_ords

def get_co_ords(list_of_poi):
    co_ord_list = []
    for poi in list_of_poi:
        index = find_in_combo("data/locations.csv", 1, "POI", 4, poi)
        co_ord_list.append(query_line("data/locations.csv", index)[3])
    return co_ord_list

class data_co_ordinate:
    def __init__(self, point_list):
        self.__dimension_list = point_list
        if self.__dimension_list[4] != -1:
            index = find_in("data/exclusions/Victim.csv", 0, point_list[4])
            poi_list = query_line("data/exclusions/Victim.csv", index)
            poi_list = poi_list[:1]
            self.__dimension_list[4] = score_closeness()
