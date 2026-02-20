import json

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def animals_organize(animals):
    for animal in animals:
        if "name" in animal:
            print(f"Name: {animal['name']}")

        if "diet" in animal:
            print(f"Diet: {animal['diet']}")

        if "locations" in animal and animal["locations"]:
            print(f"Location: {animal['locations'][0]}")

        if "type" in animal:
            print(f"Type: {animal['type']}")

        print()


def main():
    animals = load_data("animals_data.json")
    animals_organize(animals)


if __name__ == "__main__":
    main()