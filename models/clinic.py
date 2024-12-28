from db import get_db_connection

mydb = get_db_connection()
mycursor = mydb.cursor()
class Clinic:
    def __init__(self, clinic_id, address_id, name, veterinarian_count, address, phone_number, opening_hours, closing_hours, available_days):
        self.clinic_id = clinic_id
        self.address_id = address_id
        self.name = name
        self.veterinarian_count = veterinarian_count
        self.address_id = address
        self.phone_number = phone_number
        self.opening_hours = opening_hours
        self.closing_hours = closing_hours
        self.available_days = available_days

    @classmethod
    def form_register(cls, form_data): 
        
        from models.address import Address 
        
        name = form_data.get("name")
        phone_number = form_data.get("phone_number")
        opening_hours = form_data.get("opening_hours")
        closing_hours = form_data.get("closing_hours")
        available_days = form_data.getlist("days")
        address_data = Address.form_register(form_data)
      
        mycursor.execute("""
            INSERT INTO address (number, street, barangay, city, province, postal_code) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (address_data["number"], address_data["street"], address_data["barangay"], address_data["city"], address_data["province"], address_data["postal_code"]))
        
        mycursor.execute("SELECT LAST_INSERT_ID()")
        address_id = mycursor.fetchone()[0]  
        
        mycursor.execute("""
            INSERT INTO clinic (name, veterinarian_count, phone_number, opening_hours, closing_hours, available_days, address_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (name, None, phone_number, opening_hours, closing_hours, ', '.join(available_days), address_id))

        mydb.commit()
        mycursor.close()
        mydb.close()
        


