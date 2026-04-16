import base64
from rot_bruteforce import brute_force

def solve_level_1() -> str:
    first = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
    return bytes.fromhex(first).decode("utf-8")

def solve_level_2() -> str:
    first = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
    second = int("664813035583918006462745898431981286737635929725")
    clean = hex(second)[2:]

    return base64.b64decode(first).decode("utf-8") + bytes.fromhex(clean).decode("utf-8")

def solve_level_3() -> str:
    flag = "NjY2YzYxNjc3YjZjMzQ3OTMzNzIzNTVmMzA2ZTVmNmMzNDc5MzM3MjM1N2Q="
    flag = base64.b64decode(flag).decode("utf-8")
    return bytes.fromhex(flag).decode("utf-8")


def solve_level_4() -> str:
    flag = "Wm14aFozdGlOSE16WDNNeGVIUjVYMll3ZFhKZk1XNWpNM0IwTVRCdWZRPT0="
    
    flag = base64.b64decode(flag).decode("utf-8")
    return base64.b64decode(flag).decode("utf-8")
    
def solve_level_5() -> str:
    flag = "7d72337474346d5f73337479625f35647234776b6334627b67616c66"
    return bytes.fromhex(flag)[::-1].decode("utf-8")

def solve_level_6() -> str:
    flag = "0066006c00610067007b007a003300720030005f00700034006400640031006e0067005f0033007600330072007900770068003300720033007d"
    flag = flag.replace("00", "")

    return bytes.fromhex(flag).decode("utf-8")
    
def solve_level_7() -> str:
    flag = "4e6a5932597a59784e6a6333596a63304e6a67334d6a4d7a4d7a4d315a6a5a6a4d7a51334f544d7a4e7a49334d7a566d4e6a517a4d7a4d7a4e7a41335a413d3d"

    flag = bytes.fromhex(flag)
    flag = base64.b64decode(flag).decode("utf-8")
    return bytes.fromhex(flag).decode("utf-8")

def solve_level_8() -> str:
    flag = "666c6167 | e20xeA== | 5f346e64 | X200dA== | 63685f33 | bmMwZA== | 316e6735 | fQ=="
    result = []
    pieces = flag.split(" | ")
    for p in pieces:
        res = ""
        if "=" in p:
            res = base64.b64decode(p)
        else:
            res = bytes.fromhex(p)

        result.append(res)
    
    res = list(map(lambda el: el.decode("utf-8"), result))
    return "".join(res)

def solve_level_9() -> str:
    flag = "bXNobntqNDN6NHlfdDMzYXpfaTR6MzY0fQ=="
    flag = base64.b64decode(flag).decode("utf-8")

    return brute_force(flag, "flag")

def solve_level_10() -> str:
    flag = "pHSjnRW0lF9iW2AgIjXuHjXynP8jmtBpnDL5o2nrlQI="

    results = brute_force(flag)
    
    for encoded in results:
        try:
            decoded = base64.b64decode(encoded).decode("utf-8")
            return decoded[::-1]
        except:
            pass

def solve_level_11() -> str:
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
    return flag[:len(flag) - 1]

def main():
    print(solve_level_1()) 
    print(solve_level_2()) 
    print(solve_level_3()) 
    print(solve_level_4()) 
    print(solve_level_5()) 
    print(solve_level_6()) 
    print(solve_level_7()) 
    print(solve_level_8()) 
    print(solve_level_9()) 
    print(solve_level_10()) 
    print(solve_level_11()) 

if __name__ == "__main__":
    main()

