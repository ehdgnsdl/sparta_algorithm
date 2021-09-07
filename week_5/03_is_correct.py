from collections import deque

balanced_parentheses_string = "()))((()"

# 이 문제는 문제에 푸는 방법을 다 적어서 줌. 1번부터 4번까지 차례대로 구현하면 됐음.


# 균형잡힌 괄호 문자열 -> 올바른 괄호 문자열
# 올바른 괄호 문자열? 어떻게 알았지?

# 올바른 괄호 문자열인지 확인
def is_correct_parenthsis(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0

def separate_to_u_v(string):
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    # 단, u는 "균형잡힌 괄호 문자열로" 더 이상 분리할 수 없어야 하며
    # v는 빈 문자열이 될 수 있습니다.
    # ( )개수가 같아야 한다.
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
    reversed_string = ""
    for char in string:
        if char == "(":
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string



# 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
def change_to_correct_parenthesis(string):
    if string =="":
        return ""
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    # 단, u는 "균형잡힌 괄호 문자열로" 더 이상 분리할 수 없어야 하며
    # v는 빈 문자열이 될 수 있습니다.
    # ( )개수가 같아야 한다.
    u, v = separate_to_u_v(string)

    # 3. 문자열 u가 "올바른 괄호 문자열"이라면 문자열 v에 대해
    # 1단계부터 다시 수행합니다.
    # 3-1. 수행한 결과 문자열을 u에 이어붙인뒤 반환합니다.
    # -> change_to_correct_parenthesis

    if is_correct_parenthsis(u):
        return u + change_to_correct_parenthesis(v)

    # 4. 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정을 수행합니다.
    # 4-1. 빈 문자열에 첫 번째 문자로 (를 붙입니다.
    # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한결과 문자열을 이어 붙입니다.
    # 4-3. )를 다시 붙입니다.
    # 4-4. u의 첫 번째 문자와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을
    # 뒤집어서 뒤에 붙입니다.
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])
        # 첫 번째와 마지막 문자를 제거한 범위가 [1:-1]이다.


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthsis(balanced_parentheses_string): # 올바른 괄호 문자열이면 그대로 반환
        return balanced_parentheses_string
    else: # 올바른 괄호 문자열이 아닌 경우
        return change_to_correct_parenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
