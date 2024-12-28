from models.person import Person

from db import get_db_connection

mydb = get_db_connection()
mycursor = mydb.cursor()

class Veterinarian(Person):
    def __init__(self, first_name, last_name, email, username, password, vet_id, clinic_id, specialization, verification_status, license_number):
        super().__init__(first_name, last_name, email, username, password)
        self.vet_id = vet_id
        self.clinic_id = clinic_id
        self.specialization = specialization
        self.verification_status = verification_status
        self.license_number = license_number
    
    @classmethod
    def form_register(cls, form_data): 
        
        first_name = form_data.get("first_name")
        last_name = form_data.get("last_name")
        email = form_data.get("email")
        username = form_data.get("username")
        password = form_data.get("password")
        specialization = form_data.get("specialization")
        license_number = form_data.get("license_number")

        mycursor.execute("SELECT LAST_INSERT_ID()")
        address_id = mycursor.fetchone()[0]  
        
        mycursor.execute("""
            INSERT INTO pet_owners (first_name, last_name, email, username, password, specialization, license_number)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, email, username, password, specialization, license_number))

        mydb.commit()
        mycursor.close()
        mydb.close()
        
    @classmethod
    def retrieve_users(cls):
        mycursor.execute("SELECT * FROM pet_owners")
        user_records = mycursor.fetchall()
        
        # Get column names (assuming the table schema is known)
        column_names = [desc[0] for desc in mycursor.description]
        
        # Convert tuples to dictionaries
        users = []
        for record in user_records:
            user = dict(zip(column_names, record))
            users.append(user)
        
        return users
        