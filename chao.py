# Python3 implementation of Chaocipher
# L: PYTHONFLAVREDZXWUSQMKJIGCB (cipherwheel)
# R: CHAOIPERZYXWVUTSQNMLKJGFDB (plain wheel)
# 
# -> PYXMHGALDVNVHSYBNJETMXDZPFL
# <- CONGRATULATIONSONCRACKINGME

def main():
    # letters only! 
    lalpha = makealpha("pythonflavored")
    ralpha = makealpha("chaocipher") 
    
    mymsg  = "congratulations on cracking me"
    cipher = "PYXMHGALDVNVHSYBNJETMXDZPFL"
    
    print("L:", lalpha)
    print("R:", ralpha)
    print()
    print("->", do_chao(mymsg, lalpha, ralpha))
    print("<-", do_chao(cipher, lalpha, ralpha, 0))

def correct_case(string):
    return "".join([s.upper() for s in string if s.isalpha()])

def do_chao(msg, lalpha, ralpha, en=1):
    msg = correct_case(msg)
    out = ""
    for L in msg:
        pos = ralpha.index(L)
        if en:
            lalpha, ralpha = rotate_wheels(lalpha, ralpha, L)
            out += lalpha[0]
        else:
            ralpha, lalpha = rotate_wheels(ralpha, lalpha, L)
            out += ralpha[0]
        lalpha, ralpha = scramble_wheels(lalpha, ralpha)
    return out
    
def makealpha(key=""):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    z = set()
    key = [x.upper() for x in (key + alpha[::-1])
           if not (x.upper() in z or z.add(x.upper()))]
    return "".join(key)

def permu(alp, num):
    alp = alp[:num], alp[num:]
    return "".join(alp[::-1])

def rotate_wheels(lalph, ralph, key):
    newin = ralph.index(key)
    return permu(lalph, newin), permu(ralph, newin)    

def scramble_wheels(lalph, ralph):
    # LEFT = cipher wheel 
    # Cycle second[1] through nadir[14] forward
    lalph = list(lalph)
    lalph = "".join([*lalph[0],
                    *lalph[2:14],
                    lalph[1],
                    *lalph[14:]])
    
    # RIGHT = plain wheel                    
    # Send the zenith[0] character to the end[25],
    # cycle third[2] through nadir[14] characters forward
    ralph = list(ralph)
    ralph = "".join([*ralph[1:3],
                     *ralph[4:15],
                     ralph[3],
                     *ralph[15:],
                     ralph[0]])
    return lalph, ralph

main()