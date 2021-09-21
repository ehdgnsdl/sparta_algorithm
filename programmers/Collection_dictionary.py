word = "AAAAE"
# A, AA, AAA, AAAA,
# AAAAA, AAAAE, AAAAI, AAAAO, AAAAU
# AAAEA, AAAEE, AAAEI, AAAEO, AAAEU

# 모든 경우의 수를 리스트에 때려 넣고 정렬을 해서 사전을 만듦.
from itertools import product


# product 는 product([뽑아낼 데이터], repeat=뽑는 개수)로 함.
# append는 x 그 자체를 원소로 넣고, extend는 iterable의 각 항목들을 넣는다.
# ex) y = ['Ping', 'Pong']이고 x.append(y)하면. x = ['a', 'b', ['Ping', 'Pong']]
# ex) y = ['Ping', 'Pong']이고 x.extend(y)하면. x = ['a', 'b','Ping', 'Pong']
# dictionary.index(변수) 하면 index 값이 출력이 된다.

def solution(word):
    answer = 0
    dictionary = []
    # for i in range(1, 6):
    #     print(f'\n{i}개 뽑아내기')
    #     print(list(product(['A', 'E', 'I', 'O', 'U'], repeat=i)))

    for i in range(1, 6):
        dictionary.extend(list(map(''.join, product(['A', 'E', 'I', 'O', 'U'], repeat=i))))
    dictionary.sort()
    print(dictionary)

    return dictionary.index(word) + 1


print(solution(word))
