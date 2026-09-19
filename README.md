
# 🌱 EcoCivic AI

## AI-Powered Community Sustainability Grievance Analyzer

EcoCivic AI is a web-based sustainability grievance management system that allows community users to submit environmental and sustainability-related complaints.

The system uses AI to analyze submitted complaints, automatically classify them, assign a priority, generate a summary, and organize the information for monitoring and management.

An administrative dashboard allows authorized administrators to monitor complaints, analyze complaint statistics, search and filter complaints, and update complaint statuses.

---

# 📌 Project Overview

Community sustainability issues such as waste management, water and sanitation problems, pollution, environmental concerns, and infrastructure issues are often reported through unstructured channels.

EcoCivic AI provides a centralized platform where users can submit these grievances and administrators can monitor and manage them efficiently.

The system combines:

- Web-based complaint submission
- AI-powered complaint analysis
- MongoDB data storage
- User authentication
- Administrator authentication
- Complaint status tracking
- Search and filtering
- Dashboard statistics
- Data visualization
- Complaint details and timestamps

---

# 🎯 Problem Statement

Community sustainability grievances are often difficult to organize, classify, prioritize, and monitor when they are submitted through unstructured channels.

There is a need for a centralized system that can collect community complaints and use AI to analyze the information so that administrators can understand and manage sustainability-related issues more efficiently.

---

# 💡 Proposed Solution

EcoCivic AI provides a centralized grievance management platform.

The general workflow is:

```text
User
  ↓
Login / Registration
  ↓
Submit Sustainability Complaint
  ↓
AI Analysis
  ↓
Complaint Classification
  ↓
Priority Assignment
  ↓
Summary Generation
  ↓
MongoDB Storage
  ↓
Administrator Dashboard
  ↓
Status Management
  ↓
User Tracks Complaint
````

---

# ✨ Key Features

## 👤 User Features

* User registration
* User login
* User profile
* User logout
* Complaint submission
* Location submission
* Optional image upload
* View submitted complaints
* Complaint count
* Complaint status tracking
* View complaint details
* View submitted date and time
* View last updated date and time

---

## 🤖 AI-Powered Complaint Analysis

When a complaint is submitted, the AI analysis module processes the complaint and generates structured information.

The system currently extracts:

* Category
* Subcategory
* Priority
* Sustainability Area
* AI-generated Summary

The analyzed information is stored together with the original complaint in MongoDB.

---

## 🔐 Authentication

The application provides separate authentication flows for:

### Normal Users

Users can:

* Register
* Login
* Submit complaints
* View their own complaints
* Track complaint status
* Logout

### Administrators

Administrators have a separate login page and can access the authority dashboard.

The administrator dashboard is protected so that a normal user cannot directly access it.

---

# 🛡️ Admin Dashboard

The administrator dashboard provides an overview of community sustainability complaints.

It includes:

* Total complaints
* High-priority complaints
* Pending complaints
* Resolved complaints
* Complaints by category
* Priority overview
* Complaints by location
* Complaints by sustainability area
* Recent complaints
* Search functionality
* Category filtering
* Priority filtering
* Status filtering
* Complaint details
* Complaint status updates

---

# 📊 Complaint Status Tracking

Each complaint has a status.

The implemented statuses are:

```text
Pending
   ↓
In Progress
   ↓
Resolved
```

Administrators can update the status of a complaint.

The system also maintains:

* `created_at` — when the complaint was submitted
* `updated_at` — when the complaint was last updated

This allows users and administrators to distinguish between the original submission time and the most recent update time.

---

# 🗃️ Database

The application uses MongoDB for storing application data.

## Database

```text
EcoCivicAI
```

## Collections

### Users

The users collection stores registered user information.

Example structure:

```text
{
    name,
    email,
    password,
    role
}
```

The password is stored as a hashed password rather than plain text.

---

### Complaints

The complaints collection stores submitted complaints and their AI analysis.

Example structure:

```text
{
    user_id,
    user_email,
    complaint,
    location,
    image,
    category,
    subcategory,
    priority,
    sustainability_area,
    summary,
    status,
    created_at,
    updated_at
}
```

---

# 🧠 AI Analysis Module

The AI functionality is separated into an analyzer module.

The backend imports the analyzer using:

```python
from ai.analyzer import analyze_complaint
```

The complaint text is passed to the analyzer:

```python
ai_result = analyze_complaint(complaint)
```

The returned analysis is then stored with the complaint.

---

# 🏗️ Technology Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

## Backend

* Python
* Flask
* Flask-CORS

## Database

* MongoDB
* PyMongo

## Authentication & Security

* Werkzeug password hashing
* Role-based frontend access control

## AI

* Python-based complaint analysis module

## Development Environment

* Visual Studio Code
* Python virtual environment
* MongoDB

---

# 🏛️ System Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Frontend       │
                    │ HTML / CSS / JS     │
                    └──────────┬──────────┘
                               │
                               │ HTTP Requests
                               ▼
                    ┌─────────────────────┐
                    │    Flask Backend    │
                    │      app.py         │
                    └──────┬─────────┬────┘
                           │         │
                 ┌─────────┘         └─────────┐
                 ▼                             ▼
       ┌──────────────────┐          ┌──────────────────┐
       │   AI Analyzer    │          │     MongoDB      │
       │                  │          │                  │
       │ Classification   │          │ Users            │
       │ Priority         │          │ Complaints       │
       │ Summary          │          │                  │
       └──────────────────┘          └────────┬─────────┘
                                              │
                                              ▼
                                    ┌──────────────────┐
                                    │ Admin Dashboard  │
                                    │                  │
                                    │ Statistics       │
                                    │ Charts           │
                                    │ Search           │
                                    │ Filters          │
                                    │ Status Updates   │
                                    └──────────────────┘
```

---

# 📁 Project Structure

The project is organized as follows:

```text
EcoCivic-AI/
│
├── ai/
│   └── analyzer.py
│
├── backend/
│   └── app.py
│
├── database/
│
├── docs/
│   ├── bob-usage.png
│   ├── bob-usage1.png
│   └── SystemArchitecture.png
│
├── frontend/
│   ├── admin-login.html
│   ├── dashboard.css
│   ├── dashboard.html
│   ├── dashboard.js
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── script.js
│   └── style.css
│
├── uploads/
│
├── venv/
│
├── create_admin.py
├── README.md
└── AGENTS.md
```

---

# ⚙️ Requirements

Before running the project, install the following:

* Python 3.x
* MongoDB
* pip
* Web browser
* Visual Studio Code (recommended)

---

# 📦 Python Dependencies

The backend uses packages including:

```text
Flask
Flask-CORS
PyMongo
Werkzeug
```

If a `requirements.txt` file is added later, dependencies can be installed using:

```bash
pip install -r requirements.txt
```

Otherwise, install the required packages individually:

```bash
pip install flask flask-cors pymongo werkzeug
```

---

# 🗄️ MongoDB Setup

Make sure MongoDB is running locally.

The application connects to MongoDB using:

```text
mongodb://127.0.0.1:27017/
```

The application uses the database:

```text
EcoCivicAI
```

The required collections are:

```text
users
complaints
```

---

# 👨‍💼 Creating an Admin Account

The project contains:

```text
create_admin.py
```

This script can be used to create the administrator account in MongoDB.

The administrator account uses the role:

```text
admin
```

Normal registered users use:

```text
user
```

---

# 🚀 How to Run the Project

## Step 1 — Open the project

Open the `EcoCivic-AI` folder in Visual Studio Code.

---

## Step 2 — Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

---

## Step 3 — Start MongoDB

Make sure the MongoDB server is running locally.

---

## Step 4 — Start Flask

From the project root:

```bash
python backend/app.py
```

The Flask application should start on:

```text
http://127.0.0.1:5000/
```

---

## Step 5 — Open the application

Open the following URL in a browser:

```text
http://127.0.0.1:5000/
```

---

# 👤 User Workflow

```text
1. Open EcoCivic AI
        ↓
2. Register an account
        ↓
3. Login
        ↓
4. Submit complaint
        ↓
5. AI analyzes complaint
        ↓
6. Complaint stored in MongoDB
        ↓
7. View complaint in My Complaints
        ↓
8. View complaint details
        ↓
9. Track status
        ↓
10. Logout
```

---

# 👨‍💼 Administrator Workflow

```text
1. Open Admin Login
        ↓
2. Login as administrator
        ↓
3. Open Authority Dashboard
        ↓
4. View complaint statistics
        ↓
5. Search / filter complaints
        ↓
6. Open complaint details
        ↓
7. Update complaint status
        ↓
8. Monitor updated information
        ↓
9. Logout
```

---

# 🔎 Search and Filtering

The administrator dashboard provides complaint filtering based on:

### Category

```text
All Categories
Waste Management
Water & Sanitation
Air & Noise Pollution
Green Environment
Energy & Infrastructure
```

### Priority

```text
All Priorities
High
Medium
Low
```

### Status

```text
All Statuses
Pending
In Progress
Resolved
```

The dashboard also provides a search field for finding complaints using information such as:

* Complaint text
* Complaint ID
* Location
* Category

---

# 📈 Dashboard Visualization

The administrator dashboard uses charts to provide visual summaries of complaint data.

The dashboard includes visualizations for:

* Complaints by category
* Priority distribution
* Complaints by location
* Complaints by sustainability area

Chart.js is used for frontend data visualization.

---

# 🖼️ Image Upload

Users can optionally attach an image while submitting a complaint.

Uploaded images are stored in the project's:

```text
uploads/
```

directory.

The Flask backend provides access to uploaded files through the upload route.

---

# 🔒 Access Control

The administrator dashboard is protected from normal users.

If a user without administrator privileges attempts to access:

```text
dashboard.html
```

the application redirects the user to:

```text
admin-login.html
```

The administrator dashboard also redirects to the administrator login page when no valid administrator login information is available.

---

# 🛡️ Responsible AI Considerations

EcoCivic AI is designed as a decision-support and grievance-management system.

AI-generated results should be treated as analysis support rather than as a replacement for human administrative decisions.

Important considerations include:

* Avoiding misleading AI outputs
* Maintaining transparency about AI-generated analysis
* Protecting user information
* Avoiding unnecessary collection of sensitive information
* Allowing administrators to review complaint information
* Using AI results as supporting information for grievance management

---

# 🌱 Sustainability Alignment

EcoCivic AI focuses on community sustainability grievances and supports the broader goal of creating more sustainable and better-managed communities.

The project can be associated particularly with:

### SDG 11 — Sustainable Cities and Communities

The system supports community-level reporting and monitoring of sustainability-related issues.

It can also contribute to areas related to:

### SDG 12 — Responsible Consumption and Production

Through the monitoring of issues such as waste management and resource-related grievances.

The project demonstrates how AI and digital systems can support sustainability-focused community services.

---

# 🎯 Project Objectives

The main objectives of EcoCivic AI are:

1. Provide a centralized platform for sustainability grievance submission.
2. Automatically analyze complaint information using AI.
3. Categorize sustainability-related complaints.
4. Assign complaint priorities.
5. Generate concise complaint summaries.
6. Store complaint information in MongoDB.
7. Allow users to track their complaints.
8. Provide administrators with a centralized monitoring dashboard.
9. Provide search and filtering functionality.
10. Track complaint status and update times.

---

# 📌 Advantages

* Centralized complaint management
* AI-assisted complaint analysis
* Faster organization of complaints
* Structured complaint information
* User complaint tracking
* Administrator monitoring
* Search and filtering
* Visual dashboard
* Status tracking
* Timestamp tracking
* MongoDB-based storage

---

# 🔮 Future Enhancements

Possible future improvements include:

* Email or SMS notifications
* Advanced AI classification models
* Automatic duplicate complaint detection
* Geographic map-based visualization
* Advanced analytics
* Role-based permissions with stronger server-side authentication
* Automated report generation
* Threat-resistant file upload validation
* Cloud deployment
* Mobile application
* Integration with municipal grievance systems
* Historical trend analysis
* More advanced sustainability impact metrics

These are proposed future enhancements and are not part of the current implementation.

---

# 🧪 Testing

The following workflows were tested during development:

### User Testing

* User registration
* User login
* Complaint submission
* AI analysis
* Complaint retrieval
* Complaint details
* Complaint status display
* Submitted timestamp
* Last updated timestamp
* User logout

### Admin Testing

* Admin login
* Dashboard access
* Dashboard statistics
* Complaint search
* Complaint filters
* Complaint details
* Status update
* Updated timestamp
* Admin logout
* Unauthorized dashboard access

---

# 🧑‍💻 Project Development

This project was developed as an AI + Sustainability project to demonstrate how artificial intelligence can be integrated with a web-based grievance management system.

The project combines:

```text
Artificial Intelligence
        +
Web Development
        +
Database Management
        +
Data Visualization
        +
Sustainability
```

---

# 📚 Main Technologies

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| HTML       | Web page structure           |
| CSS        | User interface styling       |
| JavaScript | Frontend functionality       |
| Chart.js   | Dashboard charts             |
| Python     | Backend and AI integration   |
| Flask      | Web backend/API              |
| MongoDB    | Database                     |
| PyMongo    | MongoDB connection           |
| Werkzeug   | Password hashing             |
| Flask-CORS | Cross-origin request support |

---

# 📄 License

This project was developed as an educational and prototype project.

It is intended for learning, demonstration, and sustainability-focused application development.

---

# 🌱 Conclusion

EcoCivic AI demonstrates how AI can be combined with web technologies to support the management of community sustainability grievances.

The system provides a complete workflow from complaint submission and AI analysis to database storage, user tracking, administrator monitoring, status management, and dashboard visualization.

The project demonstrates the practical application of:

* Artificial Intelligence
* Web Development
* Database Management
* Data Visualization
* Authentication
* Sustainability-focused problem solving
