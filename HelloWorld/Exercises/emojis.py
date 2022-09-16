msg = input(">")
msg2 = msg.split(" ")
emojis = {
    ":)" : "😁",
    ":(" : "😪",
}

output = ""
for word in msg2:
    output += emojis.get(word, word) + " "

print(output)