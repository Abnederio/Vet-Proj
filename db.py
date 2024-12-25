import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abc123",
  
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE telemed") #DATABASE CREATION

#mycursor.execute("SHOW DATABASES")

