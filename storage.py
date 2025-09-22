import json
import os

def load_deck(deck_name):
    decks_dir = os.path.join("data", "decks")
    os.makedirs(decks_dir, exist_ok=True)
    deck_path = os.path.join(decks_dir, f"{deck_name}.json")
    
    if os.path.exists(deck_path):
        with open(deck_path, 'r') as f:
            return json.load(f)
    return {}

def save_deck(deck_name, progress_data):
    decks_dir = os.path.join("data", "decks")
    os.makedirs(decks_dir, exist_ok=True)
    deck_path = os.path.join(decks_dir, f"{deck_name}.json")
    with open(deck_path, 'w') as f:
        json.dump(progress_data, f, indent=4)
        
def get_all_decks():
    decks_dir = os.path.join("data", "decks")
    if not os.path.exists(decks_dir):
        return []
    return [f.replace('.json', '') for f in os.listdir(decks_dir) if f.endswith('.json')]
    
def load_progress():

    return {}

def save_progress(progress_data):

    pass

def export_progress():

    return json.dumps({}, indent=4)