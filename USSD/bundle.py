#Part of the USSD program
from airtime import Airtime as airtime

class Bundle:
    
    def __init__(self):
        print("Bundle.py started...")
        user_data_bundle = None
        self.current_cred = airtime.self.airtime
        
        
    def return_cred(self):
        cred = Bundle.__init__(self).current_cred
        return cred
    
    def award_bundle(self):
        global user_data_bundle
        u_input = input("Enter amount of desired data bundle: ")
        if cred < 10:
            print("You do not have sufficient funds to purchase any product here.\nRecharge and try again")
        elif u_input == 10:
            user_data_bundle = 10
            print("You have successfully purchased 10 MB data!")