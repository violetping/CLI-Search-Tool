# CLI‑Search‑Tool

A Python command‑line application offering:

- **googlesearch**: fetch top Google links
- **location**: geocode a place to latitude/longitude
- **weather**: fetch weather data from OpenWeatherMap

---

## ⚙️ Installation

*python3.13 or above must be installed already

Clone and install:
```bash
git clone https://github.com/violetping/CLI-Search-Tool.git
cd /CLI-Search-Tool                       #open terminal in the folder /CLI-Search-Tool or cd

pip install .
```
## Use Commands
```bash
cli-tool googlesearch "search term"       #fetch top google results
or
cli-tool googlesearch -n 7 "search term"  #-n:number of results [between 1-20]

cli-tool location "city"                  #fetch location parameters
cli-tool weather "city" "API key"         #fetch weather parameters
```
## If above installation failed then use the following steps:
Install in a venv sandbox >
```bash
git clone https://github.com/violetping/CLI-Search-Tool.git

cd CLI-Search-Tool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Use Commands 
```bash
python cli.py googlesearch -n 5 ai tool     # -n = number of results [maximum 20] , "ai tool" = your search keywordrs. 
python cli.py location "cityname"           # for location parameters 
python cli.py weather "city" "API key"      # for weather parameters
