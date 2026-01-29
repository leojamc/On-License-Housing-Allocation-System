#CODE BY LEO MCCAFFERTY W24046037
#datacreation.py

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

def random_float(lower_boundary, upper_boundary):
    integer_element = random.randint(lower_boundary, upper_boundary)
    decimal_element = random.random()
    return float(integer_element) + decimal_element

rhu_layout = list(0 , 0.00 , 0 , 0 , 0 , 0 , 0 ) #Info key, Cost per bed, Capacity, Emergency capacity, Short term beds, Location, Notes Key
rhu_list = [] #List containing all RHU's being made

def generate_RHU(num):
    for incremental in range(1, num):
        info_index = incremental
        cost_per_bed = random_float(10, 76) #Generates random float between 10 and 75 inclusive
        seed = random.random() # Generates random float between 0 and 1 non inclusive
        if seed > 0.75:
            if seed >0.95:
                capacity = random.randint(16, 21)
            else:
                capacity = random.randint(11, 16)
        else:
            capacity = random.randint(3, 11)
        emergency_capacity = random.randint(1, 3)
        short_term_beds = random.randint(1, 3)
        location_index = incremental
        notes_key = incremental
        rhu_layout = [info_index, cost_per_bed, capacity, emergency_capacity, short_term_beds, location_index, notes_key]



def write_data(processed_data):
    file = ""
    header = "# Processed data \n"
    data = []
    for row in processed_data:
        datarow = []
        datarow.append(row[0].get_ID()) #Adds first ID
        closest_tracks = row[1]
        for track in closest_tracks:
            datarow.append(f" {track.get_ID()}") #Adds closest ID's
        datarow.append(f" {str(float(f"{row[2][0]:.4f}"))}") #Adds distance
        data.append(datarow)
    with open("FAST.csv", "w") as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerow(["track_id", "track_id", "mindistance"]) #Writes headers
        writecsv.writerows(data) #Writes data