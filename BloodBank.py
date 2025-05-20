from database import *
from inventory import Inventory

class BloodBank:
    @staticmethod
    def add_blood(blood_type, quantity):
        try:
            # check if the blood type exists
            query = f"SELECT quantity FROM inventory WHERE blood_type='{blood_type}'"
            result = db_query(query)
            
            if not result:
                # If blood type doesn't exist, insert new record
                query = f"INSERT INTO inventory (blood_type, quantity) VALUES ('{blood_type}', {quantity})"
                db_query(query)
            else:
                # Update existing blood type quantity
                current_quantity = result[0][0]
                new_quantity = current_quantity + quantity
                query = f"UPDATE inventory SET quantity={new_quantity} WHERE blood_type='{blood_type}'"
                db_query(query)
            
            mydb.commit()
            print("Blood added successfully")
        except Exception as e:
            print(f"Error adding blood: {str(e)}")
            mydb.rollback()

    @staticmethod
    def deduct_blood(blood_type, quantity):
        try:
            query = f"SELECT quantity FROM inventory WHERE blood_type='{blood_type}'"
            result = db_query(query)
            
            if not result:
                print(f"Blood type {blood_type} not found in inventory")
                return
                
            current_quantity = result[0][0]
            if current_quantity < quantity:
                print(f"Not enough {blood_type} blood in inventory")
            else:
                new_quantity = current_quantity - quantity
                query = f"UPDATE inventory SET quantity={new_quantity} WHERE blood_type='{blood_type}'"
                db_query(query)
                mydb.commit()
                print("Blood deducted successfully")
        except Exception as e:
            print(f"Error deducting blood: {str(e)}")
            mydb.rollback()
          
            
    @staticmethod
    def donor_details():
        try:
            donor_name = input("Enter the Donor Name: ")
            age = int(input("Enter the Donor Age: "))
            gender = input("Enter the Donor Gender: ")
            blood_group = input("Enter the Donor Blood Group: ")
            phone_number = input("Enter the Donor Phone Number: ")
            email = input("Enter the Donor Email: ")
            
            query = f"""
                INSERT INTO donors (donor_name, age, gender, blood_group, phone_number, email)
                VALUES ('{donor_name}', {age}, '{gender}', '{blood_group}', '{phone_number}', '{email}')
            """
            db_query(query)
            mydb.commit()
            print("Donor details added successfully")
        except Exception as e:
            print(f"Error adding donor: {str(e)}")
            mydb.rollback()

    @staticmethod
    def request_blood():
        try:
            patient_name = input("Enter the Patient Name: ")
            blood_type = input("Enter the Blood Type: ")
            quantity = int(input("Enter the Quantity: "))
            hospital_name = input("Enter the Hospital Name: ")
            request_date = input("Enter the Request Date (DD-MM-YYYY): ")
            
            # Convert date from DD-MM-YYYY to YYYY-MM-DD
            try:
                day, month, year = request_date.split('-')
                request_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            except ValueError:
                print("Invalid date format. Please use DD-MM-YYYY format.")
                return
            
            # Start transaction
            mydb.start_transaction()
            
            try:
                # Check if enough blood is available and deduct
                query = f"SELECT quantity FROM inventory WHERE blood_type='{blood_type}'"
                result = db_query(query)
                
                if not result:
                    print(f"Blood type {blood_type} not found in inventory")
                    mydb.rollback()
                    return
                    
                current_quantity = result[0][0]
                if current_quantity < quantity:
                    print(f"Not enough {blood_type} blood in inventory")
                    mydb.rollback()
                    return
                
                # Deduct blood
                new_quantity = current_quantity - quantity
                query = f"UPDATE inventory SET quantity={new_quantity} WHERE blood_type='{blood_type}'"
                db_query(query)
                
                # Create request
                query = f"""
                    INSERT INTO request (patient_name, blood_type, quantity, hospital_name, request_date)
                    VALUES ('{patient_name}', '{blood_type}', {quantity}, '{hospital_name}', '{request_date}')
                """
                db_query(query)
                
                # Commit transaction
                mydb.commit()
                print("Blood request added successfully")
                
            except Exception as e:
                print(f"Error processing request: {str(e)}")
                mydb.rollback()
                
        except Exception as e:
            print(f"Error adding request: {str(e)}")
            mydb.rollback()

    @staticmethod
    def donor_list():
        try:
            query = "SELECT * FROM donors"
            result = db_query(query)
            
            if not result:
                print("No donors found")
                return
                
            print("\nDonor List:")
            print("ID | Name | Age | Gender | Blood Group | Phone | Email")
            print("-" * 80)
            for donor in result:
                print(f"{donor[0]:^2} | {donor[1]:^10} | {donor[2]:^3} | {donor[3]:^6} | {donor[4]:^11} | {donor[5]:^10} | {donor[6]}")
        except Exception as e:
            print(f"Error fetching donor list: {str(e)}")

    @staticmethod
    def blood_request_list():
        try:
            query = "SELECT * FROM request"
            result = db_query(query)
            
            if not result:
                print("No blood requests found")
                return
                
            print("\nBlood Request List:")
            print("ID | Patient Name | Blood Type | Quantity | Hospital | Request Date | Status")
            print("-" * 100)
            for request in result:
                print(f"{request[0]:^2} | {request[1]:^12} | {request[2]:^10} | {request[3]:^8} | {request[4]:^8} | {request[5]} | {request[6]}")
        except Exception as e:
            print(f"Error fetching request list: {str(e)}")

    @staticmethod
    def process_request():
        try:
            # Show pending requests
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
            
            # Get request ID to process
            request_id = int(input("\nEnter the Request ID to process: "))
            
            # Start transaction
            mydb.start_transaction()
            
            try:
                # Get request details
                query = f"SELECT * FROM request WHERE request_id={request_id} AND status='Pending'"
                result = db_query(query)
                
                if not result:
                    print("Invalid request ID or request already processed")
                    mydb.rollback()
                    return
                
                request = result[0]
                blood_type = request[2]
                quantity = request[3]
                
                # Check if enough blood is available
                query = f"SELECT quantity FROM inventory WHERE blood_type='{blood_type}'"
                result = db_query(query)
                
                if not result:
                    print(f"Blood type {blood_type} not found in inventory")
                    mydb.rollback()
                    return
                
                current_quantity = result[0][0]
                if current_quantity < quantity:
                    print(f"Not enough {blood_type} blood in inventory")
                    mydb.rollback()
                    return
                
                # Deduct blood from inventory
                new_quantity = current_quantity - quantity
                query = f"UPDATE inventory SET quantity={new_quantity} WHERE blood_type='{blood_type}'"
                db_query(query)
                
                # Update request status
                query = f"UPDATE request SET status='Completed' WHERE request_id={request_id}"
                db_query(query)
                
                # Commit transaction
                mydb.commit()
                print("Request processed successfully")
                
            except Exception as e:
                print(f"Error processing request: {str(e)}")
                mydb.rollback()
                
        except Exception as e:
            print(f"Error: {str(e)}")
            mydb.rollback()


if __name__ == "__main__":
    # Test the functionality
    BloodBank.donor_details()
    BloodBank.request_blood()
    BloodBank.donor_list()
    BloodBank.blood_request_list()

