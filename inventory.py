from database import *

class Inventory: 

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
        finally:
            cursor.fetchall()  # Clear any remaining results


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
        finally:
            cursor.fetchall()

    @staticmethod
    def check_inventory():
        try:
            query = "SELECT blood_type, quantity FROM inventory"
            result = db_query(query)
            
            if not result:
                print("No blood in inventory")
                return
                
            print("\nCurrent Blood Inventory:")
            print("Blood Type | Quantity")
            for blood_type, quantity in result:
                print(f"{blood_type:^10} | {quantity:^8}")
        except Exception as e:
            print(f"Error checking inventory: {str(e)}")

# Test the functionality
if __name__ == "__main__":
    Inventory.add_blood("A+", 10)
