import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    password="Bhav@123",
    database="blood_donation",
    auth_plugin='mysql_native_password'
)
cursor = mydb.cursor()

def db_query(query):
    try:
        cursor.execute(query)
        if query.strip().upper().startswith(('SELECT', 'SHOW')):
            result = cursor.fetchall()
            cursor.fetchall()  # Clear any remaining results
            return result
        return None
    except Exception as e:
        print(f"Database error: {str(e)}")
        return None

def create_tables():

    donor_table= """ CREATE TABLE IF NOT EXISTS donors (
        donor_id INT AUTO_INCREMENT PRIMARY KEY,
        donor_name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        gender VARCHAR(10) NOT NULL,
        blood_group VARCHAR(5) NOT NULL,
        phone_number VARCHAR(15) NOT NULL,
        email VARCHAR(100)
    )"""

    inventory_table = """ CREATE TABLE IF NOT EXISTS inventory (
        blood_id INT AUTO_INCREMENT PRIMARY KEY,
        blood_type VARCHAR(5),
        quantity INT
    )"""

    request_table = """ CREATE TABLE IF NOT EXISTS request (
        request_id INT AUTO_INCREMENT PRIMARY KEY,
        patient_name VARCHAR(100) NOT NULL,
        blood_type VARCHAR(5) NOT NULL,
        quantity INT NOT NULL,
        hospital_name VARCHAR(100) NOT NULL,
        request_date DATE NOT NULL,
        status VARCHAR(20) DEFAULT 'Pending'
    )"""

    cursor.execute(donor_table)
    cursor.execute(inventory_table)
    cursor.execute(request_table)
    mydb.commit()
    print("Tables created successfully")

if __name__ == "__main__":
    create_tables()

