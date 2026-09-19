from pymongo import MongoClient
from werkzeug.security import generate_password_hash

client = MongoClient("mongodb://127.0.0.1:27017/")

db = client["EcoCivicAI"]
users_collection = db["users"]

name = "Admin"
email = "admin@ecocivic.ai"
password = "Admin@12345"

existing_user = users_collection.find_one({"email": email})

if existing_user:
    print("Admin account already exists.")
else:
    admin = {
        "name": name,
        "email": email,
        "password": generate_password_hash(password),
        "role": "admin"
    }

    result = users_collection.insert_one(admin)

    print("Admin account created successfully!")
    print("Email:", email)
    print("Password:", password)
    print("Role: admin")
    print("ID:", result.inserted_id)

client.close()