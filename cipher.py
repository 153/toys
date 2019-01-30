# NSA "Diana" cipher
# using "autokey" algorithm

# To use a different Tabula rasa, modify alpha1, alpha2, alpha3 
alpha1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha2 = "ZYXWVUTSRQPONMLKJIHGFEDCBAZYXWVUTSRQPONMLKJIHGFEDCBA"
alpha3 = "AZYXWVUTSRQPONMLKJIHGFEDCBAZYXWVUTSRQPONMLKJIHGFEDCB"

def formatstr(text):
    """Extract all letters from a string and make them uppercase"""
    return "".join([t.upper() for t in text if t.isalpha()])

def multindex(text, query):
    """Returns all indices of a given character in a string"""
    return [i for i, e in enumerate(text) if e == query]

def encode(pt="A", ct="A"):
    """Given two letters, return the third in an NSA Diana trigram"""
    pair = []
    for i in multindex(alpha1, pt):
        for j in multindex(alpha2, ct):
            if i > j:
                pair.append(i-j)
    pair = min(pair)
    return(alpha3[pair])

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
