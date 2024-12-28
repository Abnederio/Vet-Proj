from db import get_db_connection

mydb = get_db_connection()
mycursor = mydb.cursor()

class Address:
    def __init__(self, address_id, number, street, barangay, city, province, postal_code):
        self.address_id = address_id
        self.number = number
        self.street = street
        self.barangay = barangay
        self.city = city
        self.province = province
        self.postal_code = postal_code

    @classmethod
    def form_register(cls, form_data):  
        address_data = {
        "number": form_data.get("number"),
        "street": form_data.get("street"),
        "barangay": form_data.get("barangay"),
        "city": form_data.get("city"),
        "province": form_data.get("province"),
        "postal_code": form_data.get("postal_code")
        } 
        return address_data
      
        
        
    