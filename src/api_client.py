import requests


API_URL = "https://www.floristone.com/api/flowers"


def get_flowers():
    """Get flower data from API."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as error:
        print(f"API Error: {error}")
        return []


def create_flower(name, price, category):
    """Create a new flower using POST request."""
    data = {
        "name": name,
        "price": price,
        "category": category
    }

    try:
        response = requests.post(
            API_URL,
            json=data,
            timeout=10
        )
        response.raise_for_status()
        return response.json()

    except requests.RequestException as error:
        print(f"API Error: {error}")
        return None