def checking_for_the_length(word):
    count = 0
    for letter in word:
        count = count + 1
    return count

def reverse_word(word):
    reverse_word = ""
    for letter in word:
        reverse_word = letter + reverse_word
    return reverse_word

def time_check(minutes):
    seconds = minutes * 60
    hours = minutes / 60
    return f"{minutes} mins in second is {seconds} and in hours is {hours} hours"

def vowel_checker(word):
    count = 0
    for letter in word:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            count = count + 1
    return count


word = "Pineapple"
minutes = 30
#print(checking_for_the_length(word))
#print(reverse_word(word))
print(time_check(minutes))
#print(vowel_checker(word))
