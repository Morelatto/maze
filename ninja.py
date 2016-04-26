def alphabet(msg):
    if msg == "ka":
        return "a"
    elif msg == "zu":
        return "b"
    elif msg == "mi":
        return "c"
    elif msg == "te":
        return "d"
    elif msg == "ku":
        return "e"
    elif msg == "lu":
        return "f"
    elif msg == "ji":
        return "g"
    elif msg == "ri":
        return "h"
    elif msg == "ki":
        return "i"
    elif msg == "zu":
        return "j"
    elif msg == "me":
        return "k"
    elif msg == "ta":
        return "l"
    elif msg == "rin":
        return "m"
    elif msg == "to":
        return "n"
    elif msg == "mo":
        return "o"
    elif msg == "no":
        return "p"
    elif msg == "ke":
        return "q"
    elif msg == "shi":
        return "r"
    elif msg == "ari":
        return "s"
    elif msg == "chi":
        return "t"
    elif msg == "do":
        return "u"
    elif msg == "ru":
        return "v"
    elif msg == "mei":
        return "w"
    elif msg == "na":
        return "x"
    elif msg == "fu":
        return "y"
    elif msg == "zi":
        return "z"


def sentence_translator(sentence):
    words = sentence.split("~")
    translated_words = [alphabet(word) for word in words]
    return translated_words


def translate(message):
    sentence_list = message.split("\n")
    translation = []
    for sentence in sentence_list:
        translation.append(sentence_translator(sentence))
    return translation


def main():
    message = "chi~ri~ku\n" \
              "ka~to~ari~mei~ku~shi\n" \
              "chi~mo\n" \
              "chi~ri~ki~ari\n" \
              "no~shi~mo~zu~ta~ku~rin\n" \
              "ki~ari\n" \
              "ari~ki~na\n" \
              "te~ki~ru~ki~te~ku~te\n" \
              "zu~fu\n" \
              "ri~ka~ta~lu"

    result = translate(message)
    for word in result:
        print("".join(word), end=" ")

main()

