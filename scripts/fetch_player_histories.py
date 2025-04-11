import requests
import os
import json
from time import sleep

# Creates directory if it doesnt exist
DATA_DIR = "data/raw/player_histories"
os.makedirs(DATA_DIR, exist_ok=True)

# Gets the player history with the player id
def fetch_player_history(player_id):
    url = f"https://fantasy.premierleague.com/api/element-summary/{player_id}/"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()

# Saves the player's JSON data into a file
def save_player_history(player_id, data):
    with open(f"{DATA_DIR}/player_{player_id}.json", "w") as f:
        json.dump(data, f, indent=2)

# Iterates over a list of player IDs to fetch and save each player's history
def fetch_all_histories(player_ids, delay=0.4):
    for pid in player_ids:
        try:
            print(f"Fetching player {pid}...")
            data = fetch_player_history(pid)
            save_player_history(pid, data)
            sleep(delay)  # be nice to the server
        except Exception as e:
            print(f"Error fetching player {pid}: {e}")
    print("All data downloaded successfully ✅")

if __name__ == "__main__":
    # Load player data from bootstrap-static
    with open("data/raw/bootstrap-static.json") as f:
        bootstrap_data = json.load(f)
        
    all_players = bootstrap_data["elements"]
    
    # Filter players who have played at least 500 minutes
    filtered_players = [p for p in all_players if p["minutes"] >= 500]
    
    # Get their player IDs
    filtered_player_ids = [p["id"] for p in filtered_players]
    
    print(f"Fetching history for {len(filtered_player_ids)} high-minute players...")
    fetch_all_histories(filtered_player_ids)
