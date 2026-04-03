# 🌤 Smart Weather City Manager

## 📌 About the Project

This is a Flask-based web application developed to manage cities and display their real-time weather information.
The application uses an external API to fetch weather data and stores city names in a local database.

---

## ✨ Features

* Add new cities
* View weather of multiple cities
* Delete cities from the list
* Shows:

  * Temperature 🌡
  * Weather description ☁️
  * Temperature category (Hot / Cold / Moderate) 🔥❄️

---

## 🛠️ Technologies Used

* Python (Flask)
* SQLite Database
* OpenWeather API
* HTML / CSS

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install flask flask_sqlalchemy requests
```

### 2. Run the application

```bash
python app.py
```

### 3. Open in browser

```
http://127.0.0.1:5000/
```

---

## 🗄️ Database

This project uses SQLite to store city names.
The database file (`weather.db`) is created automatically.

---

## 🚀 Future Improvements

* Search functionality
* Better UI design
* Weather forecast feature

---

## 👩‍💻 Author

Developed by Mukta Lackrany 

---