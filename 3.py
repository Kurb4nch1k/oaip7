def count_vowels_recursive(s):
    if len(s) == 0:
        return 0
    elif s[0].lower() in 'aeiou':
        return 1 + count_vowels_recursive(s[1:])
    else:
        return count_vowels_recursive(s[1:])

string = input("Введите строку: ")
vowel_count = count_vowels_recursive(string)
print(f"Количество гласных в строке '{string}' is {vowel_count}.")

