tables = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
          "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
          "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
          "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
          "GAME C++ C# JAVASCRIPT C JAVA"]

languages = ["JAVA", "JAVASCRIPT"]  # 개발자 언어 선호도 7 5 5

preference = [7, 5]


def solution(tables, languages, preference):
    score = [] # tables를 한줄씩 ' '를 기준으로 쪼갠 것을 score 리스트에 저장.
    sum_score = []  # 점수 총 합을 리스트에다가 저장
    job_category = [] # job category를 저장할 리스트


    for table in tables:
        score = table.split(' ')
        sum = 0 # 언어 선호도 X 직업군 언어 점수의 총 합
        job_category.append(score[0]) # job_category에 직업군을 넣음.

        for i in range(len(languages)):
            for j in range(1, len(score)):

                if languages[i] == score[j]:
                    sum += preference[i] * (5-j+1)
        sum_score.append(sum)

    max_job_category = [] # 최댓값이 같을 때 job_category에 직업군을 저장하는 리스트
    # tables의 for문이 끝나면 SI, CONTENTS, HARDWARE, PORTAL, GAME의 총 점수 합과 직업군이 리스트에 저장이 됨.
    for i in range(len(sum_score)):
        if sum_score[i] == max(sum_score):
            max_job_category.append(job_category[i])
    max_job_category.sort() # 사전 순으로 정렬.
    return max_job_category[0] # 맨 앞에 있는 것을 출력.

print(solution(tables, languages, preference))
