scores = [
    [100,90,98,88,65],
    [50,45,99,85,77],
    [47,88,95,80,67],
    [61,57,100,80,65],
    [24,90,94,75,65]]

# 평가하는 함수
def evaluation(mean_value):
    if mean_value >= 90:
        return 'A'
    elif 80<=mean_value<90:
        return 'B'
    elif 70<=mean_value<80:
        return 'C'
    elif 50<=mean_value<70:
        return 'D'
    else:
        return 'F'
    
# 중복 검사하는 함수
def  Duplicatetest(lists):
    count = {}
    for i in lists:
        try: count[i] += 1
        except: count[i] = 1
    return count


def solution(scores):
    rength_scores = len(scores)
    answer = ''

    # j는 열
    for j in range(rength_scores):
        sum = 0
        score = []
        # i는 행
        for i in range(rength_scores):
            # score라는 배열에 scores[i][j]를 열 별로 대입.
            score.append(scores[i][j])

        # score 리스트를 중복 검사. 중복 검사 후에 count dictionary로 만듦.
        count = Duplicatetest(score)

        # 만약 score의 j번째(자기 자신을 평가한 것)가 score의 최소거나 최대 값이면 pop,
        # 단, 유일한 최저점 or 최고점 이어야 하므로 count[score[j]]의 값이 1이어야 유일한 최저점, 최고점이므로 이때, pop을 진행
        if (score[j] == min(score) or score[j] == max(score)) and count[score[j]] == 1:
            score.pop(j)

        rength_score = len(score)
        for i in range(rength_score):
            sum += score[i]
        # 평균
        mean_value = sum/rength_score

        # 평가하는 함수 evaluation함수로 평가하기.
        answer += evaluation(mean_value)
    return answer

print(solution(scores))