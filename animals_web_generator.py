import json


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_animals_string(data):
    output = ""

    for animal in data:
        output += '<li class="cards__item">\n'

        name = animal.get("name")
        if name:
            output += f"Name: {name}<br/>\n"

        characteristics = animal.get("characteristics", {})

        diet = characteristics.get("diet")
        if diet:
            output += f"Diet: {diet}<br/>\n"

        locations = animal.get("locations", [])
        if locations:
            output += f"Location: {locations[0]}<br/>\n"

        animal_type = characteristics.get("type")
        if animal_type:
            output += f"Type: {animal_type}<br/>\n"

        output += "</li>\n"

    return output


def main():
    data = load_data("animals_data.json")

    with open("animals_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    animals_info = generate_animals_string(data)
    new_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(new_html)


if __name__ == "__main__":
    main()