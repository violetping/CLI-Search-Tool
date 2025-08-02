# CLI‑Search‑Tool

A Python command‑line application offering:

- **googlesearch**: fetch top Google links
- **location**: geocode a place to latitude/longitude
- **weather**: fetch weather data from OpenWeatherMap

---

## ⚙️ Installation

Clone and install:

```bash
git clone https://github.com/violetping/CLI-Search-Tool.git

cd CLI-Search-Tool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Use Commands 
```bash
cli-search googlesearch -n 5 "search words"   # -n = number of results [maximum 20] , "ai tool" = your search keywordrs. 
cli-search location "cityname"                # for location parameters 
cli-search weather "city" "API key"           # for weather parameters
