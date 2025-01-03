from models.person import Person
from db import get_db_connection

mydb = get_db_connection()
mycursor = mydb.cursor()
mycursor_dict = mydb.cursor(dictionary=True)

class Pet_owners(Person):
    def __init__(self, first_name, last_name, email, username, password, user_id, address_id):
        super().__init__(first_name, last_name, email, username, password)
        self.user_id = user_id
        self.address_id = address_id

    @classmethod
    def form_register(cls, form_data): 
        
        from models.address import Address 
        
        first_name = form_data.get("first_name")
        last_name = form_data.get("last_name")
        email = form_data.get("email")
        username = form_data.get("username")
        password = form_data.get("password")
        
        if cls.checkUserduplication(username, email):
            raise ValueError("Username or Email already exists") #placeholder
        
        address_data = Address.form_register(form_data)
      
        mycursor.execute("""
            INSERT INTO address (number, street, barangay, city, province, postal_code) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (address_data["number"], address_data["street"], address_data["barangay"], address_data["city"], address_data["province"], address_data["postal_code"]))
        
        mycursor.execute("SELECT LAST_INSERT_ID()")
        address_id = mycursor.fetchone()[0]  
        
        mycursor.execute("""
            INSERT INTO pet_owners (first_name, last_name, email, username, password, address_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, email, username, password, address_id))

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
    
    @classmethod
    def checkUserduplication(cls, username, email):
        
        mycursor_dict.execute("SELECT * FROM pet_owners WHERE username = %s", (username,))
        user_duplicate = mycursor_dict.fetchone()
        
        mycursor_dict.execute("SELECT * FROM pet_owners WHERE email = %s", (email,))
        email_duplicate = mycursor_dict.fetchone()
        
        if user_duplicate or email_duplicate:
            return True  
        else:
            return False 
        
        
        
        
        
        
        