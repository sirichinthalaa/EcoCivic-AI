from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime, timezone
import os
import sys
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash


# Allow Flask to access the AI module
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from ai.analyzer import analyze_complaint


app = Flask(
    __name__,
    static_folder="../frontend",
    static_url_path=""
)

CORS(app)


# -----------------------------
# MongoDB Connection
# -----------------------------

client = MongoClient(
    "mongodb://127.0.0.1:27017/"
)

db = client["EcoCivicAI"]

complaints_collection = db["complaints"]
users_collection = db["users"]


# -----------------------------
# Upload Folder
# -----------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "uploads"
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Make sure upload folder exists
os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


# -----------------------------
# Home Route
# -----------------------------

@app.route("/")
def home():

    return send_from_directory(
        os.path.join(
            BASE_DIR,
            "frontend"
        ),
        "index.html"
    )


# -----------------------------
# Submit Complaint
# -----------------------------

@app.route(
    "/api/complaints",
    methods=["POST"]
)
def submit_complaint():

    # Get complaint text
    complaint = request.form.get(
        "complaint"
    )

    # Get location
    location = request.form.get(
        "location"
    )

    # Get logged-in user information
    user_id = request.form.get(
        "user_id"
    )

    user_email = request.form.get(
        "user_email"
    )

    # Get uploaded image
    image = request.files.get(
        "image"
    )

    image_filename = None


    # -----------------------------
    # Validate Complaint
    # -----------------------------

    if not complaint:

        return jsonify({
            "error":
                "Complaint text is required"
        }), 400


    # -----------------------------
    # Save Image
    # -----------------------------

    if image and image.filename:

        image_filename = secure_filename(
            image.filename
        )

        image_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            image_filename
        )

        image.save(
            image_path
        )


    # -----------------------------
    # AI Analysis
    # -----------------------------

    ai_result = analyze_complaint(
        complaint
    )


    # -----------------------------
    # Create Submission Timestamp
    # -----------------------------

    submission_time = datetime.now(
        timezone.utc
    )


    # -----------------------------
    # Store Complaint + AI Analysis
    # -----------------------------

    complaint_data = {

        # User Information
        "user_id":
            user_id,

        "user_email":
            user_email,


        # Complaint Information
        "complaint":
            complaint,

        "location":
            location,

        "image":
            image_filename,


        # AI Analysis
        "category":
            ai_result["category"],

        "subcategory":
            ai_result["subcategory"],

        "priority":
            ai_result["priority"],

        "sustainability_area":
            ai_result["sustainability_area"],

        "summary":
            ai_result["summary"],


        # Complaint Tracking
        "status":
            "Pending",

        # IMPORTANT:
        # Both are the same when the complaint
        # is first submitted.
        "created_at":
            submission_time,

        "updated_at":
            submission_time
    }


    # -----------------------------
    # Save to MongoDB
    # -----------------------------

    result = complaints_collection.insert_one(
        complaint_data
    )


    # -----------------------------
    # Console Output
    # -----------------------------

    print("\n==============================")
    print("New Complaint Saved")
    print("==============================")

    print(
        "Complaint ID:",
        result.inserted_id
    )

    print(
        "Complaint:",
        complaint
    )

    print(
        "Location:",
        location
    )

    print(
        "Image:",
        image_filename
    )

    print(
        "Created At:",
        submission_time
    )

    print(
        "Updated At:",
        submission_time
    )

    print("\nAI Analysis")

    print(
        "Category:",
        ai_result["category"]
    )

    print(
        "Subcategory:",
        ai_result["subcategory"]
    )

    print(
        "Priority:",
        ai_result["priority"]
    )

    print(
        "Sustainability Area:",
        ai_result["sustainability_area"]
    )

    print(
        "Summary:",
        ai_result["summary"]
    )


    # -----------------------------
    # Send Response
    # -----------------------------

    return jsonify({

        "message":
            "Complaint submitted successfully!",

        "complaint_id":
            str(result.inserted_id)

    }), 201


# -----------------------------
# Get All Complaints
# -----------------------------

@app.route(
    "/api/complaints",
    methods=["GET"]
)
def get_complaints():

    complaints = list(
        complaints_collection
        .find()
        .sort(
            "created_at",
            -1
        )
    )

    for complaint in complaints:

        complaint["_id"] = str(
            complaint["_id"]
        )

    return jsonify(
        complaints
    )


# -----------------------------
# Update Complaint Status
# -----------------------------

@app.route(
    "/api/complaints/<complaint_id>/status",
    methods=["PUT"]
)
def update_complaint_status(
    complaint_id
):

    print("\n==============================")
    print("STATUS UPDATE REQUEST")
    print("==============================")


    # -----------------------------
    # Get request data
    # -----------------------------

    data = request.get_json()

    print(
        "Received Data:",
        data
    )


    if not data or "status" not in data:

        return jsonify({
            "error":
                "Status is required"
        }), 400


    new_status = data["status"]

    print(
        "New Status:",
        new_status
    )


    # -----------------------------
    # Allowed Statuses
    # -----------------------------

    allowed_statuses = [

        "Pending",

        "In Progress",

        "Resolved"

    ]


    if new_status not in allowed_statuses:

        return jsonify({
            "error":
                "Invalid status"
        }), 400


    # -----------------------------
    # Validate ObjectId
    # -----------------------------

    try:

        object_id = ObjectId(
            complaint_id
        )

    except Exception:

        return jsonify({
            "error":
                "Invalid complaint ID"
        }), 400


    # -----------------------------
    # Create NEW Updated Timestamp
    # -----------------------------

    updated_time = datetime.now(
        timezone.utc
    )

    print(
        "NEW UPDATED TIME:",
        updated_time
    )


    # -----------------------------
    # Update MongoDB
    # -----------------------------

    try:

        result = complaints_collection.update_one(

            {
                "_id":
                    object_id
            },

            {
                "$set": {

                    "status":
                        new_status,

                    "updated_at":
                        updated_time
                }
            }
        )


        # -----------------------------
        # Check Complaint
        # -----------------------------

        if result.matched_count == 0:

            print(
                "Complaint not found"
            )

            return jsonify({
                "error":
                    "Complaint not found"
            }), 404


        # -----------------------------
        # Read Updated Complaint
        # -----------------------------

        updated_complaint = (
            complaints_collection.find_one(
                {
                    "_id":
                        object_id
                }
            )
        )


        print(
            "MongoDB Created At:",
            updated_complaint[
                "created_at"
            ]
        )

        print(
            "MongoDB Updated At:",
            updated_complaint[
                "updated_at"
            ]
        )

        print(
            "MongoDB Status:",
            updated_complaint[
                "status"
            ]
        )


        # -----------------------------
        # Return Updated Data
        # -----------------------------

        return jsonify({

            "message":
                "Complaint status updated successfully",

            "status":
                updated_complaint[
                    "status"
                ],

            "created_at":
                updated_complaint[
                    "created_at"
                ].isoformat(),

            "updated_at":
                updated_complaint[
                    "updated_at"
                ].isoformat()

        }), 200


    except Exception as e:

        print(
            "STATUS UPDATE ERROR:",
            str(e)
        )

        return jsonify({
            "error":
                str(e)
        }), 500


# -----------------------------
# Uploaded Images
# -----------------------------

@app.route(
    "/uploads/<filename>"
)
def uploaded_file(
    filename
):

    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )


# -----------------------------
# Register User
# -----------------------------

@app.route(
    "/api/register",
    methods=["POST"]
)
def register_user():

    data = request.get_json()

    name = data.get(
        "name"
    )

    email = data.get(
        "email"
    )

    password = data.get(
        "password"
    )


    # -----------------------------
    # Validate
    # -----------------------------

    if not name or not email or not password:

        return jsonify({
            "error":
                "Name, email and password are required"
        }), 400


    # -----------------------------
    # Check Existing User
    # -----------------------------

    existing_user = users_collection.find_one({
        "email":
            email
    })


    if existing_user:

        return jsonify({
            "error":
                "User with this email already exists"
        }), 409


    # -----------------------------
    # Hash Password
    # -----------------------------

    hashed_password = (
        generate_password_hash(
            password
        )
    )


    # -----------------------------
    # Create User
    # -----------------------------

    user = {

        "name":
            name,

        "email":
            email,

        "password":
            hashed_password,

        "role":
            "user"
    }


    result = users_collection.insert_one(
        user
    )


    return jsonify({

        "message":
            "User registered successfully",

        "user_id":
            str(result.inserted_id)

    }), 201


# -----------------------------
# Login User
# -----------------------------

@app.route(
    "/api/login",
    methods=["POST"]
)
def login_user():

    data = request.get_json()

    email = data.get(
        "email"
    )

    password = data.get(
        "password"
    )


    # -----------------------------
    # Validate
    # -----------------------------

    if not email or not password:

        return jsonify({
            "error":
                "Email and password are required"
        }), 400


    # -----------------------------
    # Find User
    # -----------------------------

    user = users_collection.find_one({
        "email":
            email
    })


    if not user:

        return jsonify({
            "error":
                "Invalid email or password"
        }), 401


    # -----------------------------
    # Check Password
    # -----------------------------

    if not check_password_hash(
        user["password"],
        password
    ):

        return jsonify({
            "error":
                "Invalid email or password"
        }), 401


    # -----------------------------
    # Login Successful
    # -----------------------------

    return jsonify({

        "message":
            "Login successful",

        "user": {

            "id":
                str(user["_id"]),

            "name":
                user["name"],

            "email":
                user["email"],

            "role":
                user["role"]

        }

    }), 200


# -----------------------------
# Get My Complaints
# -----------------------------

@app.route(
    "/api/my-complaints/<user_id>",
    methods=["GET"]
)
def get_my_complaints(
    user_id
):

    complaints = list(

        complaints_collection.find({

            "user_id":
                user_id

        }).sort(
            "created_at",
            -1
        )
    )


    for complaint in complaints:

        complaint["_id"] = str(
            complaint["_id"]
        )


    return jsonify(
        complaints
    )


# -----------------------------
# Run Server
# -----------------------------

if __name__ == "__main__":

    print("\n==============================")
    print("EcoCivic AI Backend")
    print("==============================")
    print(
        "Server running at:"
    )
    print(
        "http://127.0.0.1:5000"
    )
    print("==============================\n")

    app.run(
        debug=True
    )