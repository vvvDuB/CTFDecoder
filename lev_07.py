import base64

flag = "4e6a5932597a59784e6a6333596a63304e6a67334d6a4d7a4d7a4d315a6a5a6a4d7a51334f544d7a4e7a49334d7a566d4e6a517a4d7a4d7a4e7a41335a413d3d"

flag = bytes.fromhex(flag)
flag = base64.b64decode(flag).decode("utf-8")
flag = bytes.fromhex(flag).decode("utf-8")
print(flag)

