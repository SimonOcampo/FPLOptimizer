import requests
import json
import os
from datetime import datetime

# Create data folder if it doesn't exist
DATA_DIR = "../data"
os.makedirs(DATA_DIR, exist_ok=True)

# Function to get data from url
def fetch_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# Function to save data to your computer
def save_json(data, filename):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2) # Format nicely
    print(f"Saved: {filepath}")
    
# Function to fetch and save everything
def fetch_fpl_data():
    print(f"Fetching FPL data... [{datetime.now().strftime('%Y-%m-%d %H:%M')}]")
    
    # 1. Players, teams, prices, etc.
    bootstrap_data = fetch_url("https://fantasy.premierleague.com/api/bootstrap-static/")
    save_json(bootstrap_data, "bootstrap-static.json")
    
    # 2. Fixtures (upcoming games)
    fixtures = fetch_url("https://fantasy.premierleague.com/api/fixtures/")
    save_json(fixtures, "fixtures.json")

    # 3. Gameweek deadlines and info
    event_data = bootstrap_data.get("events", [])
    save_json(event_data, "events.json")
    
    print("All data downloaded successfully ✅")
    
# Run the function if you execute this file
if __name__ == "__main__":
    fetch_fpl_data()
    