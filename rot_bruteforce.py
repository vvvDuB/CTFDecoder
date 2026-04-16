
def brute_force(text: str, euristic: str = "") -> str | None:
    results = []
    for key in range(26):
        flag = []
        for c in text:
            if 'A' <= c <= 'Z':
                char = ((ord(c) - 65) + key) % 26
                flag.append(chr(char + 65))
            elif 'a' <= c <= 'z':
                char = ((ord(c) - 97) + key) % 26
                flag.append(chr(char + 97))
            else:
                flag.append(c)
        
        string = "".join(flag)
        
        if euristic == "":
            results.append(string)
            continue

        if euristic in string:
            return string

    return results
    
def main():
    flag = brute_force("mshn{j43z4y_t33az_i4z364}", "flag")
    print(flag)

if __name__ == "__main__":
    main()
