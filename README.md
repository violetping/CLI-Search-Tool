# CLI‑Search‑Tool

A Python command‑line application offering:

- **googlesearch**: fetch top Google links
- **location**: geocode a place to latitude/longitude
- **weather**: fetch weather data from OpenWeatherMap

---

## ⚙️ Installation

Clone and install:

```bash
git clone https://github.com/yourusername/CLI-Search-Tool.git

cd CLI-Search-Tool
pip install .

## Use Commands 
cli-search googlesearch -n 5 ai tools   : -n = number of results [maximum20] , "ai tool" : your search keywordrs. 
cli-search location tokyo
cli-search weather -k YOUR_API_KEY -c mumbai
