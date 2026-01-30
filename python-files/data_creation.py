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

def licensee_location_mapper(num_of_rhu):
    for location in location_list:
        if location[1] == "Licensee":
            location[4] = random.randint(1, num_of_rhu-1)

def generate_bool_seed(length):
    string = ""
    for i in range(0, length):
        if random.random() <0.5:
            string += "0"
        else:
            string += "1"
    return string

suitability_template = ["", 0, False, False, 0, 0, 0, False, False, 0, False, 0, False, False, False, False, False, False, False, False, False, 0, False, False, False] #licensee_id, RHU_ID, Night Cir, Weekend cur, victim exc, school exc, prisoner exc, Disability, Accesibility, 
suitability_row = []
def generate_licensee_factors():
    for licensee in licensee_list:
        id = licensee[0]
        seed = generate_bool_seed(17)
        print(seed[0])
        if seed[0] == "0":
            bool_1 = True
        else:
            bool_1 = False
        if seed[1] == "0":
            bool_2 = True
        else:
            bool_2 = False
        exclusion = "Victim"
        if random.random() < 0.25:
            generate_exclusion_table(exclusion, generate_exclusionary_data(exclusion, 5))
            for entry in index_entry:
                if entry[0] == exclusion:
                    victim_index = entry[1]
        else:
            victim_index = -1
        exclusion = "School"
        if random.random() < 0.1:
            generate_exclusion_table(exclusion, generate_exclusionary_data(exclusion, 5))
            for entry in index_entry:
                if entry[0] == exclusion:
                    school_index = entry[1]
        else:
            school_index = -1
        exclusion = "Prisoner"
        if random.random() < 0.25:
            generate_exclusion_table(exclusion, generate_exclusionary_data(exclusion, 5))#
            for entry in index_entry:
                if entry[0] == exclusion:
                    prisoner_index = entry[1]
        else:
            prisoner_index = -1
        if seed[2] == "0":
            bool_3 = True
        else:
            bool_3 = False
        if seed[3] == "0":
            bool_4 = True
        else:
            bool_4 = False
        exclusion = "General"
        if random.random() < 0.25:
            generate_exclusion_table(exclusion, generate_exclusionary_data(exclusion, 5))
            for entry in index_entry:
                if entry[0] == exclusion:
                    general_index = entry[1]
        else:
            general_index = -1
        if seed[4] == "0":
            bool_5 = True
        else:
            bool_5 = False
        exclusion = "Associate"
        if random.random() < 0.25:
            generate_exclusion_table(exclusion, generate_exclusionary_data(exclusion, 5))
            for entry in index_entry:
                if entry[0] == exclusion:
                    associate_index = entry[1]
        else:
            associate_index = -1
        if seed[5] == "0":
            bool_6 = True
        else:
            bool_6 = False
        if seed[6] == "0":
            bool_7 = True
        else:
            bool_7 = False
        if seed[7] == "0":
            bool_8 = True
        else:
            bool_8 = False
        if seed[8] == "0":
            bool_9 = True
        else:
            bool_9 = False
        if seed[9] == "0":
            bool_10 = True
        else:
            bool_10 = False
        if seed[10] == "0":
            bool_11 = True
        else:
            bool_11 = False
        if seed[11] == "0":
            bool_12 = True
        else:
            bool_12 = False
        if seed[12] == "0":
            bool_13 = True
        else:
            bool_13 = False
        if seed[13] == "0":
            bool_14 = True
        else:
            bool_14 = False
        exclusion = "Other"
        if random.random() < 0.25:
            generate_exclusion_table(exclusion, generate_exclusionary_data(exclusion, 5))
            for entry in index_entry:
                if entry[0] == exclusion:
                    other_index = entry[1]
        else:
            other_index = -1
        if seed[14] == "0":
            bool_15 = True
        else:
            bool_15 = False
        if seed[15] == "0":
            bool_16 = True
        else:
            bool_16 = False
        if seed[16] == "0":
            bool_17 = True
        else:
            bool_17 = False
        print(bool_1)
        suitability_row.append([id, -1, bool_1, bool_2, victim_index, school_index, prisoner_index, bool_3, bool_4, general_index, bool_5, associate_index, bool_6, bool_7, bool_8, bool_9, bool_10, bool_11, bool_12, bool_13, bool_14, other_index, bool_15, bool_16, bool_17])

def populate_rhus():
    for rhu in rhu_list:
        id = rhu[0]
        seed = generate_bool_seed(17)
        print(seed[0])
        if seed[0] == "0":
            bool_1 = True
        else:
            bool_1 = False
        if seed[1] == "0":
            bool_2 = True
        else:
            bool_2 = False
        if seed[2] == "0":
            bool_3 = True
        else:
            bool_3 = False
        if seed[3] == "0":
            bool_4 = True
        else:
            bool_4 = False
        if seed[4] == "0":
            bool_5 = True
        else:
            bool_5 = False
        if seed[5] == "0":
            bool_6 = True
        else:
            bool_6 = False
        if seed[6] == "0":
            bool_7 = True
        else:
            bool_7 = False
        if seed[7] == "0":
            bool_8 = True
        else:
            bool_8 = False
        if seed[8] == "0":
            bool_9 = True
        else:
            bool_9 = False
        if seed[9] == "0":
            bool_10 = True
        else:
            bool_10 = False
        if seed[10] == "0":
            bool_11 = True
        else:
            bool_11 = False
        if seed[11] == "0":
            bool_12 = True
        else:
            bool_12 = False
        if seed[12] == "0":
            bool_13 = True
        else:
            bool_13 = False
        if seed[13] == "0":
            bool_14 = True
        else:
            bool_14 = False
        if seed[14] == "0":
            bool_15 = True
        else:
            bool_15 = False
        if seed[15] == "0":
            bool_16 = True
        else:
            bool_16 = False
        if seed[16] == "0":
            bool_17 = True
        else:
            bool_17 = False
        print(bool_1)
        suitability_row.append([-1, id, bool_1, bool_2, -1, -1, -1, bool_3, bool_4, -1, bool_5, -1, bool_6, bool_7, bool_8, bool_9, bool_10, bool_11, bool_12, bool_13, bool_14, -1, bool_15, bool_16, bool_17])


exclusions_list = []
def generate_exclusion_table(exclusion, exclusions):
    header = [exclusion, "POI's included..."]
    exclusions_list.append([header, exclusions])

index_entry = []
def generate_exclusionary_data(exclusion, max_amount):
    index = 1
    appended = False
    for entry in index_entry:
        if entry[0] == exclusion:
            index = entry[1]+1
            entry[1] = index
            appended = True
    if appended != True:
            index_entry.append([exclusion, 1])        
    if len(index_entry) == 0:
            index_entry.append([exclusion, 1])     
    exclusion_list = []
    exclusion_list.append(exclusion)
    for poi in poi_list:
        if poi[1] == exclusion:
            exclusion_list.append(poi[0])
    amount = random.randint(1, max_amount)
    chosen_list = []
    chosen_list.append(index)
    for i in range(0, amount):
        valid = False
        while not valid:
            random_val = random.randint(1, len(exclusion_list)-1)
            if exclusion_list[random_val] not in chosen_list:
                chosen_list.append(exclusion_list[random_val])
                valid = True
    return chosen_list
        

def generate_exclusionary_poi(exclusion, max):
    index = poi_list[-1][0] + 1
    index_2 = location_list[-1][0] + 1
    for i in range(0, random.randint(1, max)):
        exc_poi = [index, exclusion]
        poi_list.append(exc_poi)
        location_list.append([index_2, "POI", [random_float(0, 700, 4), random_float(0, 700, 4)], index, index_2])
        index += 1
        index_2 += 1

def generate_exclusions():
    exclusion = "Victim"
    generate_exclusionary_poi(exclusion, 750)
    exclusion = "School"
    generate_exclusionary_poi(exclusion, 25)
    exclusion = "Prisoner"
    generate_exclusionary_poi(exclusion, 250)
    exclusion = "General"
    generate_exclusionary_poi(exclusion, 25)
    exclusion = "Associate"
    generate_exclusionary_poi(exclusion, 500)
    exclusion = "Other"
    generate_exclusionary_poi(exclusion, 50)

def write_exclusion_tables(exclusions_list):
    for i in range(0, 6):
        with open("data/exclusions/"+exclusions_list[i][0][0]+".csv", "w") as csvfile:
            writecsv = csv.writer(csvfile)
            final_rows = [exclusions_list[i][0]]
            for row in exclusions_list:
                if row[0][0] == exclusions_list[i][0][0]:
                    final_rows.append(row[1])
            writecsv.writerows(final_rows)        



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
    write_exclusion_tables(exclusions_list)
    header = ["Licensee ID", "RHU ID", "Night Curfew", "Weekend Curfew", "Victim Exclusion Zone", "School Exclusion Zone", "Prisoner Exclusion Zone", "Disability", "Accsessibility", "General Exclusion Zone", "Drug Searches", "Associate Exclusion", "Young Offender Suitable", "Medical Service Access", "Transport Links", "Cultural/Religious Needs", "Mental Health Exclusions", "Gender Exclusion", "Access to family", "Prior RHU Experience", "Job Opportunities", "Other POI", "Set License Period", "Gender Support Services Nearby", "Education Servies"]
    with open("data/exclusions.csv", "w") as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerow(header)
        writecsv.writerows(suitability_row)

generate_RHU(300)
generate_POI(45)
generate_locations()
generate_contact_info()
populate_with_licensees(4000)
licensee_location_mapper(300)
generate_exclusions()
generate_licensee_factors()
populate_rhus()

write_data()