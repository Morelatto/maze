def decode(message):
    # Method 1
    for i, char in enumerate(message):
        if not i % 3:
            print(char, end="")

    print()

    # Method 2
    char_list = [char for i, char in enumerate(message) if not i % 3]
    string = "".join(char_list)
    print(string)


def main():
    panthas_message = "Tkxhwbiscscu vfbmwlgzirlsnysqr"
    decode(panthas_message)


main()
