from encrypt import encryptor
from decrypt import decryptor

def unreadable_response():
    return 'I\'m sorry, I did not understand your selection. Please enter the corresponding word for your response.'

def make_encryption():
    passage = input("Text to encrypt:\n")
    print(encryptor(passage))       
      
def make_decryption():    
    passage = input("Text to decrypt:\n")
    print(decryptor(passage)) 
        
def choose():
    choice = input("Would you like to encrypt or decrypt a message:\n")
    if choice == "encrypt":
        make_encryption()
    elif choice == "decrypt":
        make_decryption()
    else:
        print(unreadable_response())
        choose()
        
    

choose()