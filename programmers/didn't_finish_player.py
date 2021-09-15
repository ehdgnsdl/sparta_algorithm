from itertools import combinations

participants = ["mislav", "stanko", "mislav", "ana"]
completions = ["stanko", "ana", "mislav"]


def solution(participants, completions):
    participants.sort() # 먼저 각 리스트 정렬
    completions.sort()  # 먼저 각 리스트 정렬

    for par, com in zip(participants, completions): 
        if par != com:
            return par # 예시 1번
    return participants[-1]




print(solution(participants, completions))
