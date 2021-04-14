import hashlib

with open("needhash.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\r\n")
        result = hashlib.md5(line.encode())
        print(result.hexdigest())
		