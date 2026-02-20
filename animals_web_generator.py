import json


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_animals_string(data):
    output = ""

    for animal in data:
        name = animal.get("name", "")

        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        animal_type = characteristics.get("type")

        locations = animal.get("locations", [])
        location = locations[0] if locations else None

        output += '<li class="cards__item">\n'
        output += f'  <div class="card__title">{name}</div>\n'
        output += '  <p class="card__text">\n'

        if diet:
            output += f'    <strong>Diet:</strong> {diet}<br/>\n'
        if location:
            output += f'    <strong>Location:</strong> {location}<br/>\n'
        if animal_type:
            output += f'    <strong>Type:</strong> {animal_type}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

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