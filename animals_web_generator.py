import json


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_animal_lines(animal):
    lines = []


    name = animal.get("name")
    if name:
        lines.append(f"Name: {name}")


    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    if diet:
        lines.append(f"Diet: {diet}")


    locations = animal.get("locations", [])
    if locations:
        lines.append(f"Location: {locations[0]}")


    animal_type = characteristics.get("type")
    if animal_type:
        lines.append(f"Type: {animal_type}")

    return lines


def generate_animals_string(data):
    output = ""
    for animal in data:
        for line in get_animal_lines(animal):
            output += line + "\n"
        output += "\n"
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