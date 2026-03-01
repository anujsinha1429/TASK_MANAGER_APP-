🔐 Flask User Authentication System

A simple user authentication system built using Flask.
This project demonstrates how real web applications handle user registration, login, session management, and password security.

---

🚀 Features

- User Registration
- User Login
- Secure Password Hashing (Werkzeug)
- Database Storage (SQLite)
- Login Validation
- Session Handling
- Logout Functionality

---

🧠 What I Learned

- How authentication works in real websites
- Why passwords should never be stored in plain text
- Using hashing to secure user credentials
- Connecting Flask with a database
- Verifying users using hashed passwords
- Testing API routes using Thunder Client

---

🛠️ Tech Stack

- Python
- Flask
- SQLite
- HTML
- CSS
- Werkzeug Security

---

⚙️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/anujsinha1429/TASK_MANAGER_APP-.git
cd USER_AUTH_APP

2️⃣ Create virtual environment

python -m venv venv

3️⃣ Activate virtual environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

4️⃣ Install dependencies

pip install -r requirements.txt

5️⃣ Run the application

python app.py

Open in browser:

http://127.0.0.1:5000

---

📁 Project Structure

USER_AUTH_APP
│── app.py
│── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│── static/
│   └── style.css
│── database.db
│── requirements.txt

---

🔒 Security Note

Passwords are hashed using "werkzeug.security" ("generate_password_hash" and "check_password_hash").
Plain text passwords are never stored in the database.

---

📌 Future Improvements

- Protected routes (login required pages)
- Flash messages
- Better UI/UX
- Email verification
- Password reset

---

👨‍💻 Author

Anuj Sinha

If you like this project, feel free to star ⭐ the repository!