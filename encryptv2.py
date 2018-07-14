PlainKey =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890.,'"
EnigmaKey = "T'60US7,ORW 89HC3YJMKEIB1QVDXFP52ZN4ALG."
Message = input("Enter message: ")
Message = Message.upper()
val = 0
Cypher = ""
keys = {}

for char in PlainKey:
    keys[char] = EnigmaKey[val]
    val = val + 1

for char in Message:
    Cypher = Cypher + keys[char]

print(Cypher)
