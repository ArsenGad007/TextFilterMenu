def camel_filter(text):
    result = ""
    is_next_upper = False
    for i in range(len(text)):
        if text[i] == " ":
            is_next_upper = True
        elif is_next_upper:
            result += text[i].upper()
            is_next_upper = False
        else:
            result += text[i]
    return result


def snake_filter(text):
    return text.replace(" ", "_")


def shouting_filter(text):
    return text.upper()


def whispering_filter(text):
    return text.lower()
