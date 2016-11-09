Message=input("Message-->")
Message=Message.lower()
print(Message)
Tmessage=""
Cipher_Key=int(input("Cipher Key-->"))
print("Input 1 to encrypt or 2 to decrypt")
mode=int(input("mode-->"))
letters="abcdefghijklmnopqrstuvwxyz"
for symbol in Message:
    C=letters.find(symbol)
    if mode==1:
        C=C+Cipher_Key
        if C>=26:
            C=C-26
    if mode==2:
        C=C-Cipher_Key
        if C<=-1:
            C=C+26
    Tmessage=Tmessage+letters[C]
print(Tmessage)
