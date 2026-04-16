import base64
from rot_bruteforce import brute_force

encode_table = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    " ": "SPACE",
}

morse = open("./challende_final_boss.txt", "r")

flag = []

def from_bin(s: str) -> str:
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

pieces = morse.read().split()
for p in pieces:
    for k, v in encode_table.items():
        if p == v:
            flag.append(k)

flag = "".join(flag)
flag = flag.replace("0X", "")
flag = flag.replace(",", "")
flag = bytes.fromhex(flag)
flag = from_bin(flag)
flag = base64.b64decode(flag).decode("utf-8")
flag = brute_force(flag, "flag")
print(flag[:len(flag) - 1])
