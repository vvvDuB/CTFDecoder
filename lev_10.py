import base64

POSSIBLE = [
    "qITkoSX0mG9jX2BhJkYvIkYzoQ8knuCqoEM5p2osmRJ=",
    "rJUlpTY0nH9kY2CiKlZwJlZapR8lovDrpFN5q2ptnSK=",
    "sKVmqUZ0oI9lZ2DjLmAxKmAbqS8mpwEsqGO5r2quoTL=",
    "tLWnrVA0pJ9mA2EkMnByLnBcrT8nqxFtrHP5s2rvpUM=",
    "uMXosWB0qK9nB2FlNoCzMoCdsU8oryGusIQ5t2swqVN=",
    "vNYptXC0rL9oC2GmOpDaNpDetV8pszHvtJR5u2txrWO=",
    "wOZquYD0sM9pD2HnPqEbOqEfuW8qtaIwuKS5v2uysXP=",
    "xPArvZE0tN9qE2IoQrFcPrFgvX8rubJxvLT5w2vztYQ=",
    "yQBswAF0uO9rF2JpRsGdQsGhwY8svcKywMU5x2wauZR=",
    "zRCtxBG0vP9sG2KqStHeRtHixZ8twdLzxNV5y2xbvAS=",
    "aSDuyCH0wQ9tH2LrTuIfSuIjyA8uxeMayOW5z2ycwBT=",
    "bTEvzDI0xR9uI2MsUvJgTvJkzB8vyfNbzPX5a2zdxCU=",
    "cUFwaEJ0yS9vJ2NtVwKhUwKlaC8wzgOcaQY5b2aeyDV=",
    "dVGxbFK0zT9wK2OuWxLiVxLmbD8xahPdbRZ5c2bfzEW=",
    "eWHycGL0aU9xL2PvXyMjWyMncE8ybiQecSA5d2cgaFX=",
    "fXIzdHM0bV9yM2QwYzNkXzNodF8zcjRfdTB5e2dhbGY=",
    "gYJaeIN0cW9zN2RxZaOlYaOpeG8adkSgeUC5f2eicHZ=",
    "hZKbfJO0dX9aO2SyAbPmZbPqfH8belThfVD5g2fjdIA=",
    "iALcgKP0eY9bP2TzBcQnAcQrgI8cfmUigWE5h2gkeJB=",
    "jBMdhLQ0fZ9cQ2UaCdRoBdRshJ8dgnVjhXF5i2hlfKC=",
    "kCNeiMR0gA9dR2VbDeSpCeStiK8ehoWkiYG5j2imgLD=",
    "lDOfjNS0hB9eS2WcEfTqDfTujL8fipXljZH5k2jnhME=",
    "mEPgkOT0iC9fT2XdFgUrEgUvkM8gjqYmkAI5l2koiNF=",
    "nFQhlPU0jD9gU2YeGhVsFhVwlN8hkrZnlBJ5m2lpjOG=",
    "oGRimQV0kE9hV2ZfHiWtGiWxmO8ilsAomCK5n2mqkPH=",
]

def decode_candidate(encoded: str) -> str | None:
    try:
        decoded = base64.b64decode(encoded)[::-1]
        text = decoded.decode("utf-8")
    except:
        return None

    if "flag" in text:
        return text

    return None

def main() -> None:
    for encoded in POSSIBLE:
        flag = decode_candidate(encoded)
        if flag is not None:
            print(flag)
            return

if __name__ == "__main__":
    main()
