def encryptor(passage):
    alphabet = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z", 27: "A", 28: "B", 29: "C", 30: "D", 31: "E", 32: "F", 33: "G", 34: "H", 35: "I", 36: "J", 37: "K", 38: "L", 39: "M", 40: "N", 41: "O", 42: "P", 43: "Q", 44: "R", 45: "S", 46: "T", 47: "U", 48: "V", 49: "W", 50: "X", 51: "Y", 52: "Z", 53: " "}
    alphabet_new = {}
    
    for number in alphabet.keys():
        if number == 53:
            key = 1
        else:
            key = number + 1
        alphabet_new[key] = alphabet[number]
    
    alphabet = "abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    characters_value = 0
    final = ""
    for character in passage:
        if character == ' ':
            characters_value = 1
        else: 
            characters_value = alphabet.find(character) + 3
        if alphabet.find(character) == 53:
            final += alphabet_new[1]
        else:
            final += alphabet_new[characters_value]
    return final
          
  

