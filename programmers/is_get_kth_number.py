from collections import deque

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    answers = []

    if 1 <= len(array) <= 100:
        for command in commands:  # 처음엔, 2, 5, 3
            i, j, k = command # command를 i, j, k로 꺼냄.
            answer = array[i - 1:j] # [i-1:j]으로 슬라이싱해서 자른 것을 answer에 저장
            answer.sort() # 저장된 값들을 sort
            answers.append(answer[k - 1]) # index k-1번째를 answers에 append
        return answers


print(solution(array, commands))
