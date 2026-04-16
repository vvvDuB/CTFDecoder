import base64
from rot_bruteforce import brute_force

flag = "bXNobntqNDN6NHlfdDMzYXpfaTR6MzY0fQ=="

flag = base64.b64decode(flag).decode("utf-8")

print(brute_force(flag))
