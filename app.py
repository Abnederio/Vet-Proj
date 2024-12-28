from flask import Flask, render_template, request
from models.pet_owners import Pet_owners

app = Flask(__name__)

@app.route("/")
def petOwnerRegisterLink():
    
    name = request.args.get("name", "world")
    
    return render_template("user_registration.html", name = name)

#User Registration
@app.route("/userRegistration", methods=["GET", "POST"])
def petOwnerRegisterReceived():
    form_data = request.form
    Pet_owners.form_register(form_data)
    
    
    
    
