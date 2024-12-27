from person import Person

class Veterinarian(Person):
    def __init__(self, first_name, last_name, email, username, password, user_id, clinic_id, specialization, verification_status, license_number):
        super().__init__(first_name, last_name, email, username, password)
        self.user_id = user_id
        self.clinic_id = clinic_id
        self.specialization = specialization
        self.verification_status = verification_status
        self.license_number = license_number