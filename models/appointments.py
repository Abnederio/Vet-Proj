class Appointment:
    def __init__(self, appointment_id, veterinarian_id, clinic_id, pet_id, appointment_date, appointment_status, pet_concern):
        self.appointment_id = appointment_id
        self.veterinarian_id = veterinarian_id
        self.clinic_id = clinic_id
        self.pet_id = pet_id
        self.appointment_date = appointment_date
        self.appointment_status = appointment_status
        self.pet_concern = pet_concern