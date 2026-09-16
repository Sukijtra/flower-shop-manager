from src import storage


def test_save_and_load_flowers(tmp_path, monkeypatch):
    test_file = tmp_path / "flowers.json"

    monkeypatch.setattr(
        storage,
        "DATA_FILE",
        test_file
    )

    flowers = [
        {
            "id": 1,
            "name": "Rose",
            "price": 150,
            "category": "Romantic"
        }
    ]

    storage.save_flowers(flowers)

    result = storage.load_flowers()

    assert result == flowers


def test_search_flowers(tmp_path, monkeypatch):
    test_file = tmp_path / "flowers.json"

    monkeypatch.setattr(
        storage,
        "DATA_FILE",
        test_file
    )

    flowers = [
        {
            "id": 1,
            "name": "Rose",
            "price": 150,
            "category": "Romantic"
        },
        {
            "id": 2,
            "name": "Tulip",
            "price": 120,
            "category": "Birthday"
        }
    ]

    storage.save_flowers(flowers)

    result = storage.search_flowers("rose")

    assert len(result) == 1
    assert result[0]["name"] == "Rose"