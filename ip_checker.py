import sys

class Ipv4Address():
    def __init__(self):
        self.octets = 4
        self.max_of_octets = 3 #maximum number of digits of a single octet
        self.min_of_octets = 1 #minimum number of digits of a single octet
        self.notation = "." #dot notation is always used in IP address
        self.max_notations = 3 # IP address have only 3 dot notations
        self.max_bits = 255 # each octet in an IP address cannot have over 255 bits

    def ipv4format(self): #just display attributes of a good Ipv4 address
        print("A good IPv4 address ALWAYS has:")
        print("\n- ONLY 4 octets.")
        print("- ONLY 3 dot notations.")
        print("- No more than 255 bits in each octet.")
      
    def check_ip_format(self, ip_address):
        if ip_address.count(self.notation) < self.max_notations: #checking minimum number of notations
            print("\n--------------ERROR------------!")
            print("Your Ipv4 Address is too short!")
            sys.exit()
        elif ip_address.count(self.notation) > self.max_notations: # checking maximum number of notations
            print("\n-------------ERROR-----------!")
            print("Your Ipv4 Address is too long!")
            sys.exit()
        else:
            first_octet, second_octet, third_octet, fourth_octet = ip_address.split(".")
            # splitting the Ip address into four octets using the dot notations to split.
            
            octets = [first_octet, second_octet, third_octet, fourth_octet] # appending the four octets into a single list of octets.....
            #for purposes of looping thus less code
            
            for octet in octets: # looping through the list of octets
                    if len(octet) > self.max_of_octets: #checking number of digits in a single octet
                        print("\n----------------ERROR--------------!")
                        print("Invalid number of digits in ",octet)
                        sys.exit()
                    elif int(octet) > self.max_bits: #checking maximum number of bits in a single octet
                        print("\n----------------ERROR--------------!")
                        print("The octet",octet,"has over 255 bits!")
                        sys.exit()
                    elif octet not in range(0,255):
                        print("ERROR IN OCTET DIGIT",octet)
                    else:
                        pass
        print("\n-----------------------------PASS--------------------------!") #if the IP address has no errors so far....
        print("Your IPv4 Address is validated and is in the correct format!")#....this two messages get printed

    

if __name__ == "__main__":
    ipv4 = Ipv4Address() #no.....
    ipv4.ipv4format() #need....
    user_ip = input("\n\nEnter your Ipv4 Address: ")#....to explain
    ipv4.check_ip_format(user_ip)#....my code
    
            
