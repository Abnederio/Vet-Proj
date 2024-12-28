from person import Person

class Pet_owners(Person):
    def __init__(self, first_name, last_name, email, username, password, user_id, address_id):
        super().__init__(first_name, last_name, email, username, password)
        self.user_id = user_id
        self.address_id = address_id
    
    def form_register(cls, form_data): #Form retirieval
        
        first_name = form_data.get("first_name")
        last_name = form_data.get("last_name")
        email = form_data.get("email")
        username = form_data.get("username")
        password = form_data.get("password")
        
        
        