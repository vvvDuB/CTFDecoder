import base64 

def from_base64(string: str) -> str:
    res = base64.b64decode(string)
    return res

def from_hex(string: str) -> str:
    res = bytes.fromhex(string)
    return res

def from_utf(string: str) -> str:
    res = string.decode("utf-8")
    return res

flag = "666c6167 | e20xeA== | 5f346e64 | X200dA== | 63685f33 | bmMwZA== | 316e6735 | fQ=="

pieces = flag.split(" | ")
for p in pieces:
    if "=" in p:
        res = from_base64(p)
    else:
        res = from_hex(p)
    print(from_utf(res), end="")

print()
