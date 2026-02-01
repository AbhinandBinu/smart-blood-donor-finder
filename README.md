# 🩸 Smart Blood Donor Finder System


The project focuses on creating a **socially relevant, privacy-aware blood donor management system** where donors are verified by an admin before being made visible to patients or hospitals.

---

## 📌 Project Overview

The **Smart Blood Donor Finder System** allows donors to register their details along with a medical certificate.  
An admin verifies donor authenticity, and **only approved donors** are shown during search, ensuring **data privacy and reliability**.

This project evolved based on **Stage-1 review feedback**, where mentors advised enhancing real-world usability, validation, and access control.

---

## 🚀 Features

- Donor registration with medical certificate upload
- Explicit donor consent before sharing contact details
- Admin login and authentication
- Admin approval workflow for donors
- Only verified donors visible for search
- Blood group–based donor search with controlled selection
- Secure JSON-based data persistence
- Responsive and user-friendly UI

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **HTML & CSS**
- **JSON** (for persistent storage)

---

## 📂 Project Structure
smart-blood-donor-finder/
│
├── app.py # Main Flask application
├── donor.py # Donor data model (OOP)
├── database.py # JSON-based database handler
├── finder.py # Donor search logic
├── donors.json # Stored donor data (auto-created)
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── add.html
│ ├── search.html
│ ├── admin.html
│ └── admin_login.html
│
├── static/
│ ├── style.css
│ └── uploads/ # Uploaded medical certificates
│
└── README.md


---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/smart-blood-donor-finder.git
cd smart-blood-donor-finder

Install Required Package
pip install flask

3️⃣ Run the Application
python app.py


The web application will open automatically in your browser.

🔐 Admin Login Details (For Demo)
Username: admin
Password: admin123


⚠️ These credentials are hardcoded for academic/demo purposes only.

