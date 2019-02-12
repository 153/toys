# NSA "Diana" cipher
# using "autokey" algorithm
import random
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():    
    dec, plain, keyword = get_terms()
    cipher = handle_terms(dec, plain, keyword)
    cipher = wordblocks(cipher) if not dec else cipher
    print("-"*40)
    print("input:", plain, "\nkey  :", keyword)
    print("----->", cipher)

def formatstr(text):
    """Extract all letters from a string and make them uppercase"""
    return "".join([t.upper() for t in text if t.isalpha()])

def getpos(inp):
    """Find out what position a letter is in the alphabet"""
    return alphabet.index(inp)

def encode(pt='', ct=''):
    """Vastly simplified DIANA algorithm"""
    return alphabet[(25 - getpos(pt) - getpos(ct)) % 26]

def get_terms():
    """Users input a message and key, then encrypt/decrypt."""
    dec = 0 if input("Decode?\n[0/1] ") is "0" else 1
    plain = input("Please enter your message...\n> ")
    keyword = input("Please enter your key...\n> ")
    return dec, formatstr(plain), formatstr(keyword)

def handle_terms(dec, plain, keyword):
    """Encrypt or decrypt a message using autokey style"""
    cipher = []
    if not dec: # aka Enciphering
        keyword += plain
        cipher = [encode(letter, keyword[n]) \
                  for n, letter in enumerate(plain)]
    else: # Deciphering -> appending cleartext to key as it is deciphered
        for n, letter in enumerate(plain):
            letter = encode(letter, keyword[n])
            cipher.append(letter)
            keyword += letter
    return "".join(cipher)

def pad(num):
    """pad a message with num random characters""" 
    output = ""
    while len(output) < (5-num):
        output += random.choice(alphabet)
    return output

def wordblocks(text):
    """Format encoded output as blocks of 5 characters"""
    i, text2 = 0, ""
    if len(text) % 5:
        text += pad(len(text) % 5)
    while i < len(text):
        i += 5
        text2 += text[i-5:i] + " "
    return text2

if __name__ == "__main__":
    while True:
        main()
