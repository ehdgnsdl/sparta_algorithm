input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # a~z까지 총 26개이므로 빈도수를 저장할 list를 각 자리에 0으로 초기화
    alphabet_occurrence_array = [0] * 26

    alpha_index = 0
    for char in string:  # string에 들어가있는 문자를 char에 차례로 저장
        # isalpha()함수는 알파벳인지 아닌지 확인해주는 함수
        if not char.isalpha():  # 띄어쓰기 부분을 걸러주는 부분.
            continue
        alpha_index = ord(char) - ord('a')  # ord함수는 char를 ascii code로 변환시킴.
        alphabet_occurrence_array[alpha_index] += 1  # alpha_index번째에 들어가있는 빈도수를 1 추가


    max_occ = 0
    max_index = 0
    for index in range(len(alphabet_occurrence_array)):
        if max_occ < alphabet_occurrence_array[index]:
            max_occ = alphabet_occurrence_array[index]
            max_index = index

    return chr(max_index + ord('a'))


result = find_max_occurred_alphabet(input)
print(result)
