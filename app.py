from flask import Flask, render_template, request
from models.pet_owners import Pet_owners
from models.address import Address
from models.clinic import Clinic
app = Flask(__name__)

@app.route("/")
def petOwnerRegisterLink():
    
    return render_template("user_registration.html")

#User Registration
@app.route("/userRegistration", methods=["POST","GET"])
def petOwnerRegisterReceived():
    if request.method == "POST":
        form_data = request.form
        Pet_owners.form_register(form_data)
        Address.form_register(form_data)
        
    return render_template("layout.html")

@app.route("/userManager")
def manageUser():
    
    user_data = Pet_owners.retrieve_users()
    
    return render_template("user_manager.html", users = user_data)

@app.route("/clinicRegistration", methods=["POST", "GET"])
def clinicRegistrationReceived():
    if request.method == "POST":
        form_data = request.form
        Clinic.form_register(form_data)
        Address.form_register(form_data)

    return render_template("clinic_registration.html")



        
    

    
    
    
