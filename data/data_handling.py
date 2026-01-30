#CODE BY LEO MCCAFFERTY W24046037
#data_handling.py
from data_creation import generate_ID
import csv
import datetime

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
    print(contact_entry)
    licensee_file_entry = [licensee_id, license_end, gender, sex, category, release]
    contact_file_entry = [contact_entry, name, address, phone, email, 1, licensee_id]
    write_to("data/licensee.csv", licensee_file_entry)
    write_to("data/contact.csv", contact_file_entry)
