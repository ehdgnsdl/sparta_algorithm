def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1 = 0
    count2 = 0
    count3 = 0
    answer = []
    answer_temp = []

    for i in range(len(answers)):
        if answers[i] == person1[i % len(person1)]:
            count1 += 1
        if answers[i] == person2[i % len(person2)]:
            count2 += 1
        if answers[i] == person3[i % len(person3)]:
            count3 += 1

    answer_temp = [count1, count2, count3]

    for person, score in enumerate(answer_temp):
        if score == max(answer_temp):
            answer.append(person + 1)

    return answer


input = [1, 3, 2, 4, 2]

print(solution(input))