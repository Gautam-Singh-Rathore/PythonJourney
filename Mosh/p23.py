# Emoji Converter

msg = input(">")
words = msg.split(' ')
emojis = {
    ":)" : "😊",
    ":(" : "😞"
}
ans = ''
for word in words:
    ans += emojis.get(word , word)+" "

print(ans)