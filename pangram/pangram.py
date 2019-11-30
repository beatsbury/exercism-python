def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in sentence.lower():
        if letter in alphabet:
            alphabet = alphabet.replace(letter, '')
    if alphabet == '':
        return True
    else:
        return False
        
