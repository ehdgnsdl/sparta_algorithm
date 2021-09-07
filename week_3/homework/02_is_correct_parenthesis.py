s = "(())()"


# 1. ( 괄호가 열림
# 2. ( ( 괄호 또 열림
# 3. ) 괄호가 닫혔다! 그러면 아까 열린 것 중에 현재 열린 괄호는 (
# 4. ) 괄호가 닫혔다! 그러면 아까 열린 것ㅈ우에 현재 열린 괄호는
# 5. ( 괄호가 열림
# 6. ) 괄호가 닫혔다! 그러면 아까 열린 것ㅈ우에 현재 열린 괄호는

# ((()
# 1. ( 괄호가 열림
# 2. (( 괄호가 열림
# 3. ((( 괄호가 열림
# 4. ) 괄호가 닫혔다! 그러면 아까 열린 것중에 현재 열린 괄호는 (())

# 바로 직전에 조회한 괄호를 저장해야 한다. -> 즉 Stack 자료구조
def is_correct_parenthesis(string):
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i) # 어떤 값이 들어가도 상관 X (여부 저장
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
    # 구현해보세요!



print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
