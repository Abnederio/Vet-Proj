from models.person import Person
from db import get_db_connection

mydb = get_db_connection()
mycursor = mydb.cursor()

class Pet_owners(Person):
    def __init__(self, first_name, last_name, email, username, password, user_id, address_id):
        super().__init__(first_name, last_name, email, username, password)
        self.user_id = user_id
        self.address_id = address_id

    @classmethod
    def form_register(cls, form_data):  # Form retrieval
        
        first_name = form_data.get("first_name")
        last_name = form_data.get("last_name")
        email = form_data.get("email")
        username = form_data.get("username")
        password = form_data.get("password")

        # Insert the address into the address table
        mycursor.execute("""
            INSERT INTO address (number, street, barangay, city, province, postal_code) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, ('123', 'Default Street', 'City', 'State', '12345', '123'))

        # Get the last inserted address_id (auto-incremented)
        mycursor.execute("SELECT LAST_INSERT_ID()")
        address_id = mycursor.fetchone()[0]  # Fetch the generated address_id

        # Insert the pet owner into the pet_owners table
        mycursor.execute("""
            INSERT INTO pet_owners (first_name, last_name, email, username, password, address_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, email, username, password, address_id))

        # Commit the transaction and close the connection
        mydb.commit()
        mydb.close()
        
        
        
        
        
        