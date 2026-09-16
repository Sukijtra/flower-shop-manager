import json
from pathlib import Path


DATA_FILE = Path("data/flowers.json")


def save_flowers(flowers):
    """Save flowers to JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(flowers, file, indent=4)


def load_flowers():
    """Load flowers from JSON file."""
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def search_flowers(keyword):
    """Search flowers by name."""
    flowers = load_flowers()

    return [
        flower for flower in flowers
        if keyword.lower() in flower["name"].lower()
    ]