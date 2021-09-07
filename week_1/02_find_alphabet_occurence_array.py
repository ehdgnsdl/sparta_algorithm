def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    alpha_index = 0
    for char in string:
        if not char.isalpha():
            continue
        alpha_index = ord(char)-ord('a')
        alphabet_occurrence_array[alpha_index] += 1


    return alphabet_occurrence_array



print(find_alphabet_occurrence_array("hello my name is sparta"))