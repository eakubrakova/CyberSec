
cypher = "VG HFRQ GB OR RKCRAFVIR GB ZNXR GUVATF CHOYVP NAQ PURNC GB ZNXR GURZ CEVINGR ABJ VGF RKCRAFVIR GB ZNXR GUVATF CEVINGR NAQ PURNC GB ZNXR GURZ CHOYVP"

english_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'   #английский алфавит в порядке частотности символов
encrypted = np.zeros((26, 2))

for c in range(26):
    encrypted[c, 0] = c + 65

for i in cypher:
    for c in range(26):
        if i == chr(c + 65):
            encrypted[c, 1] = encrypted[c, 1] + 1

encrypted = np.flipud(encrypted[encrypted[:, 1].argsort()])

for c in range(26):
    encrypted[c, 1] = ord(english_freq[c])

for i in cypher:
    if i == ' ':
        print(' ', end='')
    else:
        for c in range(26):
            if ord(i) == encrypted[c, 0]:
                print(chr(int(encrypted[c, 1])), end='')


