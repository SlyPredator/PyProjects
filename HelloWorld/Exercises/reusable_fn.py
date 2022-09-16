def emoji_converter(msg):
    msg2 = msg.split(" ")
    emojis = {
        ":)" : "😁",
        ":(" : "😪",
    }

    output = ""
    for word in msg2:
        output += emojis.get(word, word) + " "
    return output
    

msg = input(">")
print(emoji_converter(msg))