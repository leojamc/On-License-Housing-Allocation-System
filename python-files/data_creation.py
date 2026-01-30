#CODE BY LEO MCCAFFERTY W24046037
#datacreation.py

#Information regarding sample_datset.ods
#Name dataset is a set of 995 forenames and 995 middle names i took from "A corpus of names drawn from the local birth registers of England and Wales, 1838-2014"
#This resource was accessed on 29/1/26 and is available at https://datashare.ed.ac.uk/handle/10283/3007. The dataset was collected by Bush, Stephen J
#All 995 forenames (first column) were taken from table 4 for the year 2000 as I thought this would be an accurate representation of names for offenders. The middle names were taken from table 5 for the year 1990 for added variance
#This dataset also includes 250 street names taken from OS NGD GB Address, Exeter
#This resource was accrssed on 29/1/26 and is available at https://osdatahub.os.uk/data/downloads/sample/NgdGbAddress (though login is required)
#This resource is by the Ordinance Survey


#Contact (Name)
#Address (HOUSE/CITY/POSTCODE)
#Phone number (+0000000000000)
#Email (info@server.com)
#Co-Ordinates [X, Y] X AND Y BETWEEN 0 AND 700

#Cost-Per-Bed float, 2d.p, betwen 10 and 75 inclusive
#Capacity, between 3 and 20 inclusive, 3/4 of the data will be between 3 and 10, with 20% more being between 11 and 15 and only 5% between 16 and 20
#Emergency-Capacity
#Short-term-beds
#Place-Significance

import random
import csv
import datetime

def random_float(lower_boundary, upper_boundary, dp):
    integer_element = random.randint(lower_boundary, upper_boundary)
    decimal_element = round(random.random(), dp)
    return float(integer_element) + decimal_element

#rhu_layout = list(0 , 0.00 , 0 , 0 , 0 , 0) Info key, Cost per bed, Capacity, Emergency capacity, Short term beds, Location
rhu_list = [] #List containing all RHU's being made

#poi_layout = list(0, "") #Info key, place significance
place_significance_dataset = ["Person", "School", "Public Order"]
poi_list = []

#location_layout = list(0, "", 0, [0,0], 0, 0) #Location key, Location type, contact key, co-ordinates, info key, notes key
location_list = []

#contact_layout = list(0, "", "", "", "", 0) #Contact key, Contact, Address, Phone number, Email, Location Entry, LicenseeID
contact_list = []

#Licensee_layout = list("", datetime.date, "", "", "", datetime.date) #LicenseeID, License End, Gender, Sex, Category, Prison Release
licensee_list = []

durham_prison_poi = [1, "Prison"]
poi_list.append(durham_prison_poi)
durham_prison_location = [1, "POI", 1, [350, 350], 1, 1] #Generates durham prison as a constant data entry
location_list.append(durham_prison_location)
durham_prison_contact = [1, "Warden McCalister", "45 PRISON DRIVE/DURHAM/DH4 5KL", "+4482649273078", "durhamprison@hmp.co.uk", 1]
contact_list.append(durham_prison_contact)

name_list = []
surname_list = []
street_name_list = []
with open("data/name_address_dataset.csv", "r", encoding='utf-8') as file: #Inputs data from name_dataset into lists name_list and surname_list
    for line_number, line in enumerate(file, start = 1):
        line = line.strip() #Strips whitespace from line
        stripped_line = line.split(",")
        if line_number <= 250:
            street_name_list.append(stripped_line[2])
        name_list.append(stripped_line[0])
        surname_list.append(stripped_line[1])

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
categories = ["pending", "allocated", "exited"]
ID_list = []

def generate_ID(Used_ID_list):
    ID = ""
    unique = False
    while not unique:
        for i in range (0, 5):
            random_num = random.randint(0, 34)
            ID += key[random_num]
        if ID not in Used_ID_list:
            unique = True
            ID_list.append(ID)
    return ID

def generate_dates():
    release_day = random.randint(1, 30)
    release_month = random.randint(8, 12)
    release_date = datetime.date(2025, release_month, release_day)
    license_end_date = release_date + datetime.timedelta(days = 186)
    return [release_date, license_end_date]

def generate_email(name):
    email = ""
    name = name.split(" ")
    name1_len = len(name[0])
    name2_len = len(name[1])
    chance = random.random()
    if chance < 0.5:
        email += (name[0] +name[1])
    else:
        email += (name[0][:(random.randint(1, name1_len-1))] + name[1][:(random.randint(1, name2_len-1))])
    email += "@"
    chance = random.random()
    if chance < 0.5:
        email += "gmail.com"
    elif chance <0.9:
        email += "outlook.com"
    else:
        email += "hotmail.com"
    return email

def generate_phone_number():
    phone_number = "+440"
    for i in range(1, 11):
        phone_number = phone_number + str(random.randint(1, 9))
    return phone_number

def generate_address():
    rand_street = random.randint(0, 249)
    street_name = street_name_list[rand_street]
    street_number = random.randint(1, 100)
    city = "Durham"
    postcode = "DH" + str(random.randint(1, 5)) + " " + str(random.randint(1, 9)) + str(alphabet[random.randint(0, 25)]) + str(alphabet[random.randint(0, 25)])
    return str(street_number) + " " + street_name + "/" + city + "/" + postcode

def generate_name():
    random_name = name_list[random.randint(0, 994)]
    random_surname = name_list[random.randint(0, 994)]
    return random_name + " " + random_surname


def generate_RHU(num):
    for incremental in range(1, num):
        info_index = incremental
        cost_per_bed = random_float(10, 76, 2) #Generates random float between 10 and 75 inclusive
        seed = random.random() # Generates random float between 0 and 1 non inclusive
        if seed > 0.75:
            if seed >0.95:
                capacity = random.randint(16, 20)
            else:
                capacity = random.randint(11, 15)
        else:
            capacity = random.randint(3, 10)
        emergency_capacity = random.randint(1, 2)
        short_term_beds = random.randint(1, 2)
        location_index = incremental + 1
        rhu_layout = [info_index, cost_per_bed, capacity, emergency_capacity, short_term_beds, location_index]
        rhu_list.append(rhu_layout)

def generate_POI(num):
    for incrimental in range(1, num):
        info_index = incrimental
        place_significance = place_significance_dataset[random.randint(0, 2)]
        poi_layout = [info_index, place_significance]
        poi_list.append(poi_layout)

def generate_locations():
    incrimental = 2
    for rhu in rhu_list:
        location_key = incrimental
        location_type = "RHU"
        contact_key = incrimental
        co_ordinates = [random_float(0, 700, 4), random_float(0, 700, 4)]
        info_key = rhu[0]
        notes_key = incrimental
        location_layout = [location_key, location_type, contact_key, co_ordinates, info_key, notes_key]
        location_list.append(location_layout)
        incrimental += 1
    for poi in poi_list:
        location_key = incrimental
        location_type = "POI"
        contact_key = incrimental
        co_ordinates = [random_float(0, 700, 4), random_float(0, 700, 4)]
        info_key = poi[0]
        notes_key = incrimental
        location_layout = [location_key, location_type, contact_key, co_ordinates, info_key, notes_key]
        location_list.append(location_layout)
        incrimental += 1      

def generate_contact_info():
    for location in location_list:
        contact_key = location[2]
        contact = generate_name()
        address = generate_address()
        phone_number = generate_phone_number()
        email = generate_email(contact)
        location_index = location[0]
        contact_list.append([contact_key, contact, address, phone_number, email, location_index])

def populate_with_licensees(num):
    index_start = location_list[-1][0] + 1
    for i in range(index_start, num+index_start):
        location_key = i
        location_type = "Licensee"
        contact_key = i
        co_ordinates = [random_float(0, 700, 4), random_float(0, 700, 4)]
        info_key = -1
        notes_key = i
        location_layout = [location_key, location_type, contact_key, co_ordinates, info_key, notes_key]
        location_list.append(location_layout)   
        contact = generate_name()
        address = generate_address()
        phone_number = generate_phone_number()
        email = generate_email(contact)
        licensee_id = generate_ID(ID_list)
        contact_list.append([contact_key, contact, address, phone_number, email, location_key, licensee_id])
        dates = generate_dates()
        license_end_date = dates[1]
        random_val = random.random()
        if random_val < 0.475:
            gender = "Man"
            random_val = random.random()
            if random_val < 0.95:
                sex = "Man"
            else:
                sex = "Woman"
        elif random_val < 0.95:
            gender = "Woman"
            random_val = random.random()
            if random_val < 0.95:
                sex = "Woman"
            else:
                sex = "Man"
        else:
            gender = "Non-binary"
            random_val = random.random()
            if random_val < 0.5:
                sex = "Man"
            else:
                sex = "Woman"
        random_val = random.randint(0, 2)
        category = categories[random_val]
        licensee_list.append([licensee_id, license_end_date, gender, sex, category, dates[0]])


def write_data():
    header = ["Info Key", "Cost Per Bed", "Capacity", "Emergency Capacity", "Short term beds", "Location", "Notes Key"]
    with open("data/rhu.csv", "w") as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerow(header)
        writecsv.writerows(rhu_list)
    header = ["Info Key", "Place significance", "Notes Key"]
    with open("data/poi.csv", "w") as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerow(header)
        writecsv.writerows(poi_list)
    header = ["Location", "Location Type", "Contact Info", "Co-ordinates", "Info Key", "Notes Key"]
    with open("data/locations.csv", "w") as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerow(header)
        writecsv.writerows(location_list)   
    header = ["Contact Entry", "Contact", "Address", "Phone number", "Email address", "Location Entry", "Licensee ID"]
    with open("data/contact.csv", "w") as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerow(header)
        writecsv.writerows(contact_list)
    header = ["Licensee ID", "License End", "Gender", "Sex", "Category", "Prison Release"]   
    with open("data/licensee.csv", "w") as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerow(header)
        writecsv.writerows(licensee_list)

generate_RHU(300)
generate_POI(45)
generate_locations()
generate_contact_info()
populate_with_licensees(4000)

write_data()