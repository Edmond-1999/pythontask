

def digit_adder(texts):
    count = 0
        
    for text in texts:
        if text == "0" or text == "1" or text == "2" or text == "3" or text == "4" or text == "5" or text == "6" or text == "7" or text == "8" or text == "9":
            text = int(text)
            count = count + text
    return count

def case_toggle(word):
    new_word = ""
    for letter in word:
        number = ord(letter)
        if number >= 97 and number <= 122:
            new_word += chr(number - 32)
        elif number >= 65 and number <= 90:
            new_word += chr(number + 32)
    return new_word

def space_compressor(letter):
    new_word = ""
    for char in letter:
        if char == " ":
            char = "-"
    
        new_word += char
    return new_word

def triple_threat(wording):
    new_word = ""
    for word in wording:
        for number in range(3):
            new_word += word
    return new_word

texts = "a5b2c1"
word = "PyThOn"
letter = "Hello World !"
wording = "code"
#print(digit_adder(texts))
#print(case_toggle(word))
print(space_compressor(letter))
print(triple_threat(wording))

