import hashlib

string = input("Digite uma palavra: ")
stringHash = hashlib.sha1()
stringHash.update(string.encode())
print("SHA-1 Hash (hexadecimal):", stringHash.hexdigest())