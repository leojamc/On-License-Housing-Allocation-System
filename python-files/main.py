#CODE BY LEO MCCAFFERTY W24046037
#main.py

correct_login = "DRHM45" #Password for logging in
def check_login(login_attempt):
    if login_attempt == correct_login:
        return True
    else:
        return False
    
from data_handling import register_offender