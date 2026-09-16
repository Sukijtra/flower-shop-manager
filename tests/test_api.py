from unittest.mock import patch

from src.api_client import get_flowers, create_flower


@patch("src.api_client.requests.get")
def test_get_flowers(mock_get):
    mock_get.return_value.json.return_value = [
        {
            "id": 1,
            "name": "Rose",
            "price": 150,
            "category": "Romantic"
        }
    ]

    mock_get.return_value.raise_for_status.return_value = None

    flowers = get_flowers()

    assert len(flowers) == 1
    assert flowers[0]["name"] == "Rose"


@patch("src.api_client.requests.post")
def test_create_flower(mock_post):
    mock_post.return_value.json.return_value = {
        "id": 2,
        "name": "Tulip",
        "price": 120,
        "category": "Birthday"
    }

    mock_post.return_value.raise_for_status.return_value = None

    flower = create_flower(
        "Tulip",
        120,
        "Birthday"
    )

    assert flower["name"] == "Tulip"