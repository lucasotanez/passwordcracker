import time
from hashlib import md5

# TO RUN THE SCRIPT
# ==========================
# cd into this directory
# in the console, enter:
# python passcracker.py
# ==========================
# by Lucas Otanez

possibleChars = [
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B",
                "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4",
                "5", "6", "7", "8", "9", "0"
                ]

# read in hashes from text file:
ifile = open("hashes.txt", "r")
hashes = ifile.readlines()
ifile.close()

# define a function to crack one hash:
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
            # exit condition: hash match:
            if (calchash == realhash):
                print(f'{(temp+char):10} cracked in {str(round(time.time() - start, 4)):4} seconds')
                return
        # handling initial case when x is empty:
        if (x == []):
            x.append("a")
            stack.append(0)
            continue
        estack = len(stack) - 1
        # walk down the stack to find which character to update:
        while (x[estack] == "0") and (estack >= 0):
            x[estack] = "a"
            stack[estack] = 0
            estack -= 1
        # triggered if the length of the string should be increased:
        if (estack == -1):
            x.append("a")
            stack.append(0)
            continue
        # else move to the next password string:
        else:
            stack[estack] += 1
            x[estack] = possibleChars[stack[estack]]

# call crack on each hash in the list   
for p in hashes:
    crack(p)