import os

from configparser import ConfigParser, SectionProxy

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_languages() -> dict:
    languages = {}
    config = ConfigParser()
    for f in os.listdir("./langs/"):
        if "ini" in f:
            config.read("./langs/" + f)
            languages[f.split(".")[0]] = config["translation"]["language_name"]
    return languages

def get_language(languages: dict) -> SectionProxy:
    config = ConfigParser()
    print("Available languages: ")
    for k, v in languages.items():
        print(f" [-] {k} -> {v}")
    while True:
        language = input('Choose a language: ').lower()
        if language in languages:
            config.read(f"./langs/{language}.ini")
            return config["translation"]
        else:
            print("Invalid language key! Try again...")

def get_message(message: str, language: SectionProxy) -> str:
    return language[message].replace("{n}", "\n")

def get_spoons(cup_qnt: float) -> float:
    return (14 * cup_qnt) / 7

def get_water(cup_qnt: float, cup_size: float) -> float:
    if cup_qnt > 1:
        return (float(14.285714285714) * cup_size / 100) * cup_qnt
    else:
        return cup_size / 7

def get_milk(cup_qnt: float, cup_size: float) -> float:
    if cup_qnt > 1:
        return (float(85.714285714286) * cup_size / 100) * cup_qnt
    else:
        return cup_size - get_water(cup_qnt, cup_size)

def show_recipe(cup_qnt: float, cup_size: float, language: SectionProxy) -> None:
    text = get_message("ingredients", language)\
        .replace("{cup_qnt}", str(cup_qnt))\
        .replace("{cup_size}", str(cup_size))\
        .replace("{soup_spoons}", f"{get_spoons(cup_qnt):.0f}")\
        .replace("{water}", f"{get_water(cup_qnt, cup_size):.2f}")\
        .replace("{milk}", f"{get_milk(cup_qnt, cup_size):.2f}")
    print(text)

def show_steps(cup_qnt, cup_size, language) -> None:
    text = get_message("how_to_prepare", language) \
        .replace("{soup_spoons}", f"{get_spoons(cup_qnt):.0f}") \
        .replace("{water}", f"{get_water(cup_qnt, cup_size):.2f}") \
        .replace("{milk}", f"{get_milk(cup_qnt, cup_size):.2f}")
    print(text)
    print(get_message("observation", language))

def main():
    clear_screen()

    languages = get_languages()
    language = get_language(languages)

    clear_screen()

    cup_size = float(input(get_message("enter_cup_size", language) + " "))
    cup_qnt = int(input(get_message("enter_cups", language) + " "))

    clear_screen()

    show_recipe(cup_qnt, cup_size, language)
    show_steps(cup_qnt, cup_size, language)

    input(get_message("exit", language))

if __name__ == '__main__':
    main()
