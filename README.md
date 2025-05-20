# Blood-Bank-Management-
This is a menu-driven, command-line Blood Bank Management System designed . It allows both Admin and User interactions, offering key functionalities for managing donors, processing blood requests, and maintaining inventory. 

NOTE: """"THIS IS ONLY BACKEND PART OF THE PROGRAMMING DONE IN PYTHON AND SQL ONLY. IT CAN BE CONSIDERED AS A MINI- PROJECT. THE WEBSITE WILL NOT BE DONE"""""

👤 Roles & Access
Admin (Login Required)
View and approve blood requests
View all or pending requests
Update blood inventory\

User (No Login)
Add donor details
Request blood units
View current blood inventory
See donor and request lists
Process their own blood requests

✅ Features
Role-based login (Admin/User)
Clean, text-based interface
Secure admin access with hardcoded credentials

Modular structure using:
BloodBank (donors & requests)
Inventory (blood stock)
Admin (admin panel)

🗂️ Modules
Main.py: Entry point. Prompts user to choose role and navigates to respective menu.
Admin.py: Handles admin functions like approval and inventory management.
BloodBank.py: Manages donor registration, requests, and listings.
Inventory.py: Displays and updates blood availability.
database.py: Provides db_query() and DB connection (mydb) for SQL operations.

💾 Database Structure (Overview)
request table: Stores blood request info (patient name, blood type, status, etc.)
inventory table: Tracks available units per blood type

🔓 Admin Credentials (for testing)
Username: Deepak / Deepa
Password: 12345678 / 09876543
