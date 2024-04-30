import os

def generate_markdown_menu(directory):
    markdown_menu = "# Index\n"  # Nagłówek dla menu

    for root, dirs, files in os.walk(directory):
        # Pomijamy katalogi ukryte (zaczynające się od kropki)
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        # Tworzymy strukturę listy punktowanej
        level = root.count(os.sep)  # Poziom zagnieżdżenia
        indent = "  " * level  # Wcięcie w zależności od poziomu

        # Dodajemy folder do menu
        markdown_menu += f"{indent}* {os.path.basename(root)}\n"

        # Dodajemy pliki Markdown w folderze
        for file in files:
            if file.lower().endswith(".md"):
                markdown_menu += f"{indent}  * [{os.path.splitext(file)[0]}]({os.path.join(root, file)})\n"

    return markdown_menu

# Przykład użycia
directory_path = "."
generated_menu = generate_markdown_menu(directory_path)

# Zapisujemy menu do pliku README.md
with open(os.path.join(directory_path, "MENU.md"), "w") as readme_file:
    readme_file.write(generated_menu)
