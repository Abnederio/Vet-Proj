import mysql.connector

def get_db_connection():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc123",
    database="telemed"
  )
  return mydb

mydb = get_db_connection()
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE telemed") #DATABASE CREATION

#mycursor.execute("SHOW DATABASES")
#for db in mycursor:
 # print(db)
 
 
mycursor.execute("""
CREATE TABLE IF NOT EXISTS address (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    number VARCHAR(255),
    street VARCHAR(255),
    barangay VARCHAR(255),
    city VARCHAR(255),
    province VARCHAR(255),
    postal_code VARCHAR(10)
);
""")
 
mycursor.execute("""
CREATE TABLE IF NOT EXISTS pet_owners (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL, 
  last_name VARCHAR(255) NOT NULL, 
  email VARCHAR(255) NOT NULL,
  username VARCHAR(255) NOT NULL, 
  password VARCHAR(255) NOT NULL,
  address_id INT NOT NULL,
  FOREIGN KEY (address_id) REFERENCES address(address_id) 
  );
  """)

mycursor.execute("""
CREATE TABLE IF NOT EXISTS pets (
  pet_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  gender VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  breed VARCHAR(255) NOT NULL,
  species VARCHAR(255) NOT NULL,
  weight FLOAT NOT NULL,
  size VARCHAR(255) NOT NULL,
  spayed_neutered TINYINT(1) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES pet_owners(user_id) 
);
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS clinic (
  clinic_id INT AUTO_INCREMENT PRIMARY KEY,
  veterinarian_count INT,
  name VARCHAR(255) NOT NULL, 
  address VARCHAR(255) NOT NULL, 
  phone_number VARCHAR(20) NOT NULL, 
  operating_hours TIME NOT NULL
);
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS veterinarian (
  veterinarian_id INT AUTO_INCREMENT PRIMARY KEY,
  clinic_id INT NOT NULL,
  first_name VARCHAR(255) NOT NULL, 
  last_name VARCHAR(255) NOT NULL, 
  email VARCHAR(255) NOT NULL, 
  username VARCHAR(255) NOT NULL, 
  password VARCHAR(255) NOT NULL,
  specialization VARCHAR(255) NOT NULL,
  verification_status INT NOT NULL,
  license_number INT NOT NULL,
  FOREIGN KEY (clinic_id) REFERENCES clinic(clinic_id)
);
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
  appointment_id INT AUTO_INCREMENT PRIMARY KEY,
  veterinarian_id INT NOT NULL,
  clinic_id INT NOT NULL,
  pet_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_status VARCHAR(255) NOT NULL,
  pet_concern VARCHAR(255) NOT NULL,
  FOREIGN KEY (pet_id) REFERENCES pets(pet_id),
  FOREIGN KEY (veterinarian_id) REFERENCES veterinarian(veterinarian_id),
  FOREIGN KEY (clinic_id) REFERENCES clinic(clinic_id)
);
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS consultation (
  consultation_id INT AUTO_INCREMENT PRIMARY KEY,
  pet_id INT NOT NULL,
  type VARCHAR(255) NOT NULL,
  appointment_id INT NOT NULL,
  record_date DATE NOT NULL,
  start_time TIME,
  end_time TIME,
  FOREIGN KEY (pet_id) REFERENCES pets(pet_id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
);
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS pet_records (
  record_id INT AUTO_INCREMENT PRIMARY KEY,
  pet_id INT NOT NULL,
  consultation_id INT,
  appointment_id INT NOT NULL,
  record_date DATE NOT NULL,
  FOREIGN KEY (pet_id) REFERENCES pets(pet_id),
  FOREIGN KEY (consultation_id) REFERENCES consultation(consultation_id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
);
""")

mydb.commit()

mycursor.close()
mydb.close()
 


