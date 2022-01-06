dictionary = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четире",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten":"десять"
}

def num_translate(value: str) -> str:
    #`"""переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    for number_key in dictionary:
        if(value == number_key):
            str_out = dictionary.get(number_key)
            break
    return str_out
print(num_translate("one"))
print(num_translate("eight"))

