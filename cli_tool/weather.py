import requests
import datetime

def run(city, apikey):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric"
    r = requests.get(url).json()
    if r.get("cod") != 200:
        print("❌", r.get("message"))
        return

    main, wind, sys = r["main"], r["wind"], r["sys"]
    weather = r["weather"][0]["description"]

    print(f"🌦️ Weather in {city}: {weather}")
    print(f"🌡️ Temp: {main['temp']}°C (min {main['temp_min']}°C, max {main['temp_max']}°C)")
    print(f"💧 Humidity: {main['humidity']}%, Pressure: {main['pressure']} hPa")
    print(f"💨 Wind Speed: {wind['speed']} m/s")
    print("🌅 Sunrise:", datetime.datetime.fromtimestamp(sys["sunrise"]))
    print("🌇 Sunset:", datetime.datetime.fromtimestamp(sys["sunset"]))
