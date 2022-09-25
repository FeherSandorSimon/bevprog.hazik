if __name__ == '__main__':
    sentence = input("Adjon meg egy mondatot: ")
    letters = {};
    for i in range(0, len(sentence)):
        letter = sentence[i:(i + 1)];

        if (letters.get(letter) == None):
            letters[letter] = 0

        letters[letter] += 1;

    print(f"Betűk gyakorisága: {letters}");

    print(f"Fordítva: {sentence[::-1]}");

    words = sentence.split(" ");
    print(f"Listába rendezve szavanként: {words}")

