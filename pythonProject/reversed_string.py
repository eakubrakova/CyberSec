text = input("Введите строку: ")
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
print("Перевернутая строка:", reversed_text)

