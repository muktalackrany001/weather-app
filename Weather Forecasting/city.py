from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import requests

# ================= CONFIG =================
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///weather.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "myweatherproject123"

db = SQLAlchemy(app)

print("🌤 Smart Weather City Manager")

# ================= DATABASE MODEL =================
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# ================= FUNCTIONS =================
def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=c3a269da272cad852966bc587e58f9ec"
    response = requests.get(url).json()
    return response

def get_temp_category(temp):
    if temp < 15:
        return "Cold ❄️"
    elif temp < 30:
        return "Moderate 🌤"
    else:
        return "Hot 🔥"

# ================= ROUTES =================

# Home Page (GET)
@app.route("/")
def index_get():
    cities = City.query.all()
    weather_data = []

    for city in cities:
        r = fetch_weather(city.name)

        if r.get("cod") != 200:
            continue

        weather = {
            "city": city.name,
            "temperature": r["main"]["temp"],
            "description": r["weather"][0]["description"],
            "icon": r["weather"][0]["icon"],
            "category": get_temp_category(r["main"]["temp"])
        }

        weather_data.append(weather)

    return render_template("index.html", weather_data=weather_data)

# Add City (POST)
@app.route("/", methods=["POST"])
def index_post():
    err_msg = ""
    new_city = request.form.get("city")

    if new_city:
        existing_city = City.query.filter_by(name=new_city).first()

        if not existing_city:
            new_city_data = fetch_weather(new_city)

            if new_city_data.get("cod") == 200:
                new_city_obj = City(name=new_city)
                db.session.add(new_city_obj)
                db.session.commit()
            else:
                err_msg = "Invalid city name. Please try again."
        else:
            err_msg = "City already exists in database."

    if err_msg:
        flash(err_msg, "error")
    else:
        flash("City added successfully!", "success")

    return redirect(url_for("index_get"))

# Delete City
@app.route("/delete/<name>")
def delete_city(name):
    city = City.query.filter_by(name=name).first()

    if city:
        db.session.delete(city)
        db.session.commit()
        flash(f"Deleted {city.name}", "success")

    return redirect(url_for("index_get"))

# ================= RUN =================
if __name__ == "__main__":
    db.create_all()
    app.run()