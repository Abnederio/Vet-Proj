from flask import Flask, render_template, request, flash, redirect, url_for
from models.pet_owners import Pet_owners
from models.address import Address
from models.clinic import Clinic
from db import get_db_connection

app = Flask(__name__)
app.secret_key = 'a_very_secret_key_that_is_hard_to_guess_12345'

mydb = get_db_connection()
mycursor = mydb.cursor()
mycursor_dict = mydb.cursor(dictionary=True)

@app.route("/")
def petOwnerRegisterLink():
    
    return render_template("user_login.html")

#User Registration
@app.route("/userRegistration", methods=["POST","GET"])
def petOwnerRegisterReceived():
    if request.method == "POST":
        form_data = request.form
        Pet_owners.form_register(form_data)
        Address.form_register(form_data)
        
    return render_template("user_registration.html")

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

    return render_template("login.html")

@app.route("/userLogin", methods=["POST", "GET"])
def userLogin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        mycursor_dict.execute("SELECT * FROM pet_owners WHERE username = %s", (username,))
        user_confirmation = mycursor_dict.fetchone()

        if user_confirmation:
            if user_confirmation['password'] == password:
                return "login successful"  # For now, placeholder message
            else:
                flash("Invalid Password", "error")  # Flash error message
                return redirect(url_for("userLogin"))  # Redirect to avoid form resubmission
        else:
            flash("Username not Found", "error")  # Flash error message
            return redirect(url_for("userLogin"))  # Redirect to avoid form resubmission

    return render_template("user_login.html")
        



        
    

    
    
    
