"""
    - Program to generate Kenyan phone numbers 
"""
__author__ = "Chris Wachira"
__maintainer__ = "chriskane816@gmail.com"
__version__ = 0.1
__status__ = "Prototype"

import random

class PhoneNumber():
    """Create a phone number object"""
    def __init__(self):
        print("Number initiated...")
        self.area_code = ['+254', '07'] # common area code digits for any Kenya phone number
        self.carrier_digits = { # the range of digits used by the common service providers in Kenya
            "safaricom": (0,29),
            "airtel": (30,39),
            "orange": (70,79)
        }

        

      
    def construct(self, area_code, carrier, spacer='-'):
        print("Starting GEN for {0} lines...".format(carrier.upper()))
        
        while carrier in self.carrier_digits.keys(): # check if carrier specified is in the carrier dictionary above

            self.suffix = random.randint(0,999999) # generate a random number for the last 6 digits of a phone number
            suffix_length = len(str(self.suffix))
            required_length = 6

            if suffix_length < required_length: # check if length of generated number
                difference = required_length - suffix_length
                self.suffix = "0"*difference + str(self.suffix # append zeros before the generated number if its characters dont count to 6

            start = self.carrier_digits[carrier][0]
            end = self.carrier_digits[carrier][1]
            
            carrier_digit = str(random.randint(start, end))
            if len(carrier_digit) < 2:
                carrier_digit = "0" + carrier_digit
             
            first = area_code
            suffix = str(self.suffix)
            number = first + spacer + carrier_digit + spacer + suffix

            print(number)
        
#if __name__ == "__main__":
#    number = PhoneNumber()
#    number.construct("07","orange")
