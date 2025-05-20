from BloodBank import BloodBank
from database import *
from inventory import Inventory

class Admin:
    @staticmethod
    def admin_menu():
        while True:
            print("\n=== Admin Menu ===")
            options = int(input("Choose an option:\n"
                  "1. View Pending Requests \n"
                  "2. Approve Request \n"
                  "3. View All Requests \n"
                  "4. Alter Blood Inventory \n"
                  "5. Exit \n"
                  "Enter your choice: "))
            
            try:
                if type(options) != int:
                    print("Please enter a number")
                    continue
            except Exception as e:
                print(e)
                continue

            if options == 1:
                Admin.view_pending_requests()
            elif options == 2:
                Admin.approve_request()
            elif options == 3:
                BloodBank.blood_request_list()
            elif options == 4:
                Admin.alter_inventory()
            elif options == 5:
                print("Thank you for using SVCE Blood Bank Admin Panel")
                break
            else:
                print("Invalid Option")

    @staticmethod
    def view_pending_requests():
        try:
            query = "SELECT * FROM request WHERE status='Pending'"
            result = db_query(query)
            
            if not result:
                print("No pending requests found")
                return
                
            print("\nPending Blood Requests:")
            print("ID | Patient Name | Blood Type | Quantity | Hospital | Request Date")
            print("-" * 90)
            for request in result:
                print(f"{request[0]:^2} | {request[1]:^12} | {request[2]:^10} | {request[3]:^8} | {request[4]:^8} | {request[5]}")
        except Exception as e:
            print(f"Error viewing requests: {str(e)}")

    @staticmethod
    def approve_request():
        try:
            # Show all requests
            query = "SELECT * FROM request"
            result = db_query(query)
            
            if not result:
                print("No requests found")
                return
                
            print("\nAll Blood Requests:")
            print("ID | Patient Name | Blood Type | Quantity | Hospital | Request Date | Status")
            print("-" * 100)
            for request in result:
                print(f"{request[0]:^2} | {request[1]:^12} | {request[2]:^10} | {request[3]:^8} | {request[4]:^8} | {request[5]} | {request[6]}")
            
            # Get request ID to approve
            request_id = int(input("\nEnter the Request ID to approve: "))
            
            try:
                # Update request status
                query = f"UPDATE request SET status='Approved' WHERE request_id={request_id}"
                db_query(query)
                mydb.commit()
                print("Request approved successfully")
                
            except Exception as e:
                print(f"Error approving request: {str(e)}")
                mydb.rollback()
                
        except Exception as e:
            print(f"Error: {str(e)}")
            mydb.rollback()

    @staticmethod
    def alter_inventory():
        try:
            # Show current inventory
            query = "SELECT * FROM inventory"
            result = db_query(query)
            
            if not result:
                print("No blood inventory found")
                return
                
            print("\nCurrent Blood Inventory:")
            print("Blood Type | Quantity")
            print("-" * 30)
            for blood in result:
                print(f"{blood[0]:^10} | {blood[1]:^8}")
            
            # Get blood type to alter
            blood_type = input("\nEnter blood type to alter (A+, A-, B+, B-, AB+, AB-, O+, O-): ").upper()
            
            # Validate blood type
            valid_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
            if blood_type not in valid_types:
                print("Invalid blood type")
                return
            
            # Get new quantity
            try:
                new_quantity = int(input("Enter new quantity: "))
                if new_quantity < 0:
                    print("Quantity cannot be negative")
                    return
            except ValueError:
                print("Please enter a valid number")
                return
            
            try:
                # Update inventory
                query = f"UPDATE inventory SET quantity={new_quantity} WHERE blood_type='{blood_type}'"
                db_query(query)
                mydb.commit()
                print(f"Inventory updated successfully for {blood_type}")
                
            except Exception as e:
                print(f"Error updating inventory: {str(e)}")
                mydb.rollback()
                
        except Exception as e:
            print(f"Error: {str(e)}")
            mydb.rollback()

if __name__ == "__main__":
    Admin.admin_menu()
