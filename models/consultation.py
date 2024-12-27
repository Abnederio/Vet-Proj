class Consultation:
    def __init__(self, consultation_id, pet_id, consultation_type, appointment_id, record_date, start_time, end_time):
        self.consultation_id = consultation_id
        self.pet_id = pet_id
        self.consultation_type = consultation_type  # Changed 'type' to 'consultation_type' to avoid conflict with Python keyword
        self.appointment_id = appointment_id
        self.record_date = record_date
        self.start_time = start_time
        self.end_time = end_time