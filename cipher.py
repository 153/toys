# NSA "Diana" cipher
# using "autokey" algorithm

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

def formatstr(text):
    """Extract all letters from a string and make them uppercase"""
    return "".join([t.upper() for t in text if t.isalpha()])

def getpos(inp):
    """Find out what position a letter is in the alphabet"""
    return alphabet.index(inp)

def encode(pt='', ct=''):
    """Vastly simplified DIANA algorithm"""
    if (25 - getpos(pt) - getpos(ct)) < 0:
        return alphabet[51 - getpos(pt) - getpos(ct)]
    else:
        return alphabet[25 - getpos(pt) - getpos(ct)]

def get_terms():
    """Users input a message and key, then encrypt/decrypt."""
    dec = input("Decode?\n[0/1] ")
    plain = input("Please enter your message...\n> ")
    keyword = input("Please enter your key...\n> ")
    if dec is "0":
        dec = 0
    return dec, formatstr(plain), formatstr(keyword)

def handle_terms(dec, plain, keyword):
    """Encrypt or decrypt a message using autokey style"""
    cipher = []
    if not dec:
        keyword = keyword + plain
        cipher = [encode(letter, keyword[n]) \
                  for n, letter in enumerate(plain)]
    else:
        for n, letter in enumerate(plain):
            letter = encode(letter, keyword[n])
            cipher.append(letter)
            keyword += letter            
    return "".join(cipher)    

def main():    
    dec, plain, keyword = get_terms()
    cipher = handle_terms(dec, plain, keyword)
    
    print("-"*40)
    print("input:", plain, "\nkey  :", keyword)
    print("----->", cipher)

if __name__ == "__main__":
    while True:
        main()
