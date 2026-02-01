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

2️⃣ Install Required Package
pip install flask

3️⃣ Run the Application
python app.py


The web application will open automatically in your browser.

🔐 Admin Login Details (For Demo)
Username: admin
Password: admin123


⚠️ These credentials are hardcoded for academic/demo purposes only.

🔁 Application Workflow

Donor registers with details and medical certificate

Donor data is stored with pending status

Admin logs in and verifies donor information

Admin approves donor

Approved donors become visible in search results