import json


def load_animals_data():
    """Load a json file"""
    with open("animals_data.json", "r") as file:
        data = json.load(file)
    return data


def main():
    animals = load_animals_data()
    print(animals)


if __name__ == "__main__":
    main()