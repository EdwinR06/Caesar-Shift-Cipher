def decryptor(passage):
    alphabet = "abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    characters_value = 0
    final = ""
    for character in passage:
        if character == ' ':
            characters_value = 52
        else: 
            characters_value = alphabet.find(character) - 1
        if alphabet.find(character) == 53:
            final += alphabet[52]
        else:
            final += alphabet[characters_value]
    return final