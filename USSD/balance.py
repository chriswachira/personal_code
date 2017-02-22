from airtime import Airtime as airtime

class Balance:
    airtime_bal = airtime.award_airtime().self.airtime
    bundle_bal = bundle
    bonga_bal = bonga
    
    def balance(self):
        return airtime_bal
        return bundle_bal
        return bonga_bal
    
    def displayBal(self):
        
        choice = [1,2,3]
        
        if choice == 1:
            print("Your airtime balance is", airtime_bal)
        elif choice == 2:
            print("Your bundle balance is", bundle_bal)
        