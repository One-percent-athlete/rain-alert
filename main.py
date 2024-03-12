import requests
import smtplib
import dotenv
import os
dotenv.load_dotenv()


my_email = os.environ.get("my_email")
password = os.environ.get("password")
api = os.environ.get("api")
lat = os.environ.get("lat")
lon = os.environ.get("lon")

ow_url = "http://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": lat,
    "lon": lon,
    "appid": api,
    "cnt": 4
}

response = requests.get(url=ow_url, params=params)
response.raise_for_status()
data = response.json()

# print(data["list"][0])

for i in range(4):
    if data["list"][i]["weather"][0]["id"] <= 700:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=my_email, 
                msg=f"Subject:Umbrella reminder\n\nYou might need umbrella today!!")
    i += 1


