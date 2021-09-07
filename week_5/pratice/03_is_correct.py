from collections import deque

balanced_parentheses_string = "()))((()"

# 이 문제는 문제에 푸는 방법을 다 적어서 줌. 1번부터 4번까지 차례대로 구현하면 됐음.


def is_correct_parenthesis(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif stack:
            stack.pop()
    return len(stack) == 0


def seperate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    v = ''.join(list(queue))

    return u, v

def reverse_parenthesis(string):
    char = ""
    for s in string:
        if s == '(':
            char += ')'
        else:
            char += '('
    return char


def change_to_correct_parenthesis(string):
    if string == "":
        return ""

    u, v = seperate_to_u_v(string)

    # 3번
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)

    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])





# 1. 올바른 괄호 문자열인지 판단하는 함수 생성
def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string # 균형잡힌 스트링이라면 그대로 출력
    else:# 균형 잡힌 스트링이 아니라면
        return change_to_correct_parenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
