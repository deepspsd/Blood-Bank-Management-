use blood_donation;
Database changed
mysql> show tables in blood_donation;
Empty set (0.07 sec)

mysql> show tables in blood_donation;
+--------------------------+
| Tables_in_blood_donation |
+--------------------------+
| donors                   |
| inventory                |
| request                  |
+--------------------------+
3 rows in set (0.04 sec)

mysql> select * from donors;
Empty set (0.00 sec)

mysql> select * from donors;
+----------+------------+-----+--------+-------------+--------------+------------------+
| donor_id | donor_name | age | gender | blood_group | phone_number | email            |
+----------+------------+-----+--------+-------------+--------------+------------------+
|        1 | Bhavya     |  20 | Female | A+          | 9876543210   | bhavya@gmail.com |
+----------+------------+-----+--------+-------------+--------------+------------------+
1 row in set (0.01 sec)

mysql> select * from donors;
+----------+------------+-----+--------+-------------+--------------+------------------+
| donor_id | donor_name | age | gender | blood_group | phone_number | email            |
+----------+------------+-----+--------+-------------+--------------+------------------+
|        1 | Bhavya     |  20 | Female | A+          | 9876543210   | bhavya@gmail.com |
|        2 | Kavya      |  19 | Female | A-          | 9089097345   | kavya@gmail.com  |
+----------+------------+-----+--------+-------------+--------------+------------------+
2 rows in set (0.00 sec)

mysql> select * from donors;
+----------+------------+-----+--------+-------------+--------------+------------------+
| donor_id | donor_name | age | gender | blood_group | phone_number | email            |
+----------+------------+-----+--------+-------------+--------------+------------------+
|        1 | Bhavya     |  20 | Female | A+          | 9876543210   | bhavya@gmail.com |
|        2 | Kavya      |  19 | Female | A-          | 9089097345   | kavya@gmail.com  |
|        3 | Deepak     |  20 | male   | O+          | 6748428330   | deepak@gmail.com |
+----------+------------+-----+--------+-------------+--------------+------------------+
3 rows in set (0.01 sec)

mysql> select * from inventory;
Empty set (0.07 sec)

mysql> INSERT INTO inventory (blood_type,quantity) VALUES
    -> ( "A+",10),
    -> ( "A-",10),
    -> ( "B+",10),
    -> ( "B-",10),
    -> ( "O+",10),
    -> ( "O-",10),
    -> ( "AB+",10),
    -> ( "AB-",10);
Query OK, 8 rows affected (0.05 sec)
Records: 8  Duplicates: 0  Warnings: 0

mysql> select * from inventory;
+----------+------------+----------+
| blood_id | blood_type | quantity |
+----------+------------+----------+
|        1 | A+         |       10 |
|        2 | A-         |       10 |
|        3 | B+         |       10 |
|        4 | B-         |       10 |
|        5 | O+         |       10 |
|        6 | O-         |       10 |
|        7 | AB+        |       10 |
|        8 | AB-        |       10 |
+----------+------------+----------+
8 rows in set (0.00 sec)
