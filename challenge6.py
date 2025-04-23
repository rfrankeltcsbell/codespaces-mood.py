def count_vowels(word):
    vowels= ["a","e","i","o"]
    count= 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count
print (count_vowels("raz"))