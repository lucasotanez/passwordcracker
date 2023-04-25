import time
from hashlib import md5

possibleChars = [
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B",
                "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4",
                "5", "6", "7", "8", "9", "0"
                ]

ifile = open("hashes.txt", "r")
hashes = ifile.readlines()
ifile.close()

def crack(realhash):
    realhash = str(realhash.strip())
    calchash = ""
    x = []
    stack = []
    start = time.time()
    while True:
        temp = ''.join(x)
        for char in possibleChars:
            calchash = md5((temp + char).encode()).hexdigest()
            if (calchash == realhash):
                print(f'{(temp+char):10} cracked in {str(round(time.time() - start, 4)):4} seconds')
                return
        if (x == []):
            x.append("a")
            stack.append(0)
            continue
        estack = len(stack) - 1
        while (x[estack] == "0") and (estack >= 0):
            x[estack] = "a"
            stack[estack] = 0
            estack -= 1
        if (estack == -1):
            x.append("a")
            stack.append(0)
            continue
        else:
            stack[estack] += 1
            x[estack] = possibleChars[stack[estack]]
        
for p in hashes:
    crack(p)