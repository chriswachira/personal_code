from ip_checker import Ipv4Address

#ipv4 = Ipv4Address()

class Subnet(Ipv4Address):
    pass


if __name__ == "__main__":
    subnet = Subnet()
    subnet.ipv4format()
    user_subnet = input("\nEnter your Subnet IP: ")
    subnet.check_ip_format(user_subnet)
