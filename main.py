from BloodBank import BloodBank
from inventory import Inventory
from admin import Admin

class Main:
    def __init__(self):
        print("Welcome to the SVCE Blood Bank")
        option = input("Are you a admin (A) or a user (U)?: ")
        if option == "A":
            print("Admin Login")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username == "Deepak" and password == "12345678":
                Admin.admin_menu()
            elif username == "Deepa" and password == "09876543":
                Admin.admin_menu()
            else:
                print("Invalid username or password")
        elif option == "U":
            self.user_menu()
        else:
            print("Invalid Option")

    def user_menu(self):
        while True:
            try:
                options = int(input("Choose the Available Facilities:\n"
                    "1. Add Donor Details \n"
                    "2. Request Blood \n"
                    "3. Check Inventory \n"
                    "4. Donor List \n"
                    "5. Blood Request List \n"
                    "6. Process Blood Request \n"
                    "7. Exit \n"
                    "Enter your choice: "))
                
                if type(options) != int:
                    print("Please enter a number")
                    continue

                if options == 1:
                    BloodBank.donor_details()
                elif options == 2:
                    BloodBank.request_blood()
                elif options == 3:
                    Inventory.check_inventory()
                elif options == 4:
                    BloodBank.donor_list()
                elif options == 5:
                    BloodBank.blood_request_list()
                elif options == 6:
                    BloodBank.process_request()
                elif options == 7:
                    print("Thank you for using SVCE Blood Bank")
                    break
                else:
                    print("Invalid Option")
                    
            except Exception as e:
                print(e)
                continue

if __name__ == "__main__":
    Main()
