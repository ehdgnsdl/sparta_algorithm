input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    alpha_index = 0
    for char in string:
        if not char.isalpha():
            continue
        alpha_index = ord(char) - ord('a')
        alphabet_occurrence_array[alpha_index] += 1



    not_repeating_alphabet = []
    for index in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[index] == 1:
            not_repeating_alphabet.append(chr(index+ord('a')))

    for char in string:
        if char in not_repeating_alphabet:
            return char
    return "_"


result = find_not_repeating_character(input)
print(result)