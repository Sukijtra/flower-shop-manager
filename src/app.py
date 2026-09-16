from src.api_client import get_flowers, create_flower
from src.storage import save_flowers, load_flowers, search_flowers


def show_flowers(flowers):
    """Display flower information."""
    if not flowers:
        print("No flowers found.")
        return

    for flower in flowers:
        print(
            f'{flower["id"]}. '
            f'{flower["name"]} - '
            f'{flower["price"]} THB - '
            f'{flower["category"]}'
        )


def main():
    print("================================")
    print("       FLOWER SHOP MANAGER")
    print("================================")

    print("\n1. Get flowers from API")

    flowers = get_flowers()

    if flowers:
        save_flowers(flowers)
        print("Flower data saved successfully.")
        show_flowers(flowers)

    print("\n2. Search flower")

    keyword = input("Enter flower name: ")

    results = search_flowers(keyword)

    print("\nSearch Results:")
    show_flowers(results)

    print("\n3. Add new flower")

    name = input("Flower name: ")
    price = input("Price: ")
    category = input("Category: ")

    if name and price and category:
        new_flower = create_flower(name, price, category)

        if new_flower:
            print("\nFlower created successfully!")
            print(new_flower)

    saved_flowers = load_flowers()

    print(
        f"\nTotal saved flowers: "
        f"{len(saved_flowers)}"
    )


if __name__ == "__main__":
    main()