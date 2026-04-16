import base64
from rot_bruteforce import brute_force

def main() -> None:
    flag = "pHSjnRW0lF9iW2AgIjXuHjXynP8jmtBpnDL5o2nrlQI="

    results = brute_force(flag)
    
    for encoded in results:
        try:
            decoded = base64.b64decode(encoded).decode("utf-8")
            return decoded[::-1]
        except:
            pass

if __name__ == "__main__":
    main()
