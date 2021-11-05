# Imports
from bs4 import BeautifulSoup
import requests

# Instruction
print(
    "This script will get the definition or synonym of a word.\nInputs are case-insensitive."
)

# User inputs
while True:
    def_or_syn = input("(D) for Definitons or (S) for Synonym: ").lower()
    if def_or_syn == "q":
        quit()
    elif def_or_syn not in ["d", "s"]:
        continue
    elif def_or_syn == "d":
        website, content_type = "dictionary", "definitions"
        el_tag, el_class = "div", "e1fc5zsj0"
        break
    else:
        website, content_type = "thesaurus", "synonyms"
        el_tag, el_class = "div", "css-ixatld"
        break

user_word = input("Word: ")
# User word input format for url
word = "%20".join(user_word.split(" "))

# URL to go to
url = f"https://{website}.com/browse/{word}"

# Parse website
get_website = requests.get(url).text
content = BeautifulSoup(get_website, "html.parser")

# Content to display
def_syn_content = content.find(el_tag, class_=el_class).text

if content_type == "synonyms":
    output = "\n".join(def_syn_content.split(" "))
else:
    output = "\n".join(def_syn_content.split(": "))

write_content = (
    f"{output}\n\nFor more {content_type}, go to the following url.\nURL: {url}"
)


# Ask user to place it in a file or not
while True:
    user_file_or_not = input(
        f"Would you like the {content_type} to be placed in a new file? (Y/N)\n"
    ).upper()
    if user_file_or_not not in ["Y", "N"]:
        continue
    elif user_file_or_not == "Y":
        user_filename = input(f"What would you like the filename to be? ").lower()
        user_extname = input(f"(T) for the text file or (M) for markdown? ").lower()
        if user_extname not in ["t", "m"]:
            continue
        elif user_extname == "t":
            user_extname = "txt"
        else:
            user_extname = "md"
        with open(f"./{user_filename}.{user_extname}", "w") as file:
            file.write(write_content)
            break
    else:
        print(write_content)
        break
