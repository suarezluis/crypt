PlainKey =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890.,'"
EnigmaKey = "T'60US7,ORW 89HC3YJMKEIB1QVDXFP52ZN4ALG."
Cypher = "UYOWTV" 


val = 0
message = ""
keys = {}

for char in EnigmaKey:
    keys[char] = PlainKey[val]
    val = val + 1

for char in Cypher:
    message = message + keys[char]    

print("UYOWTV")
