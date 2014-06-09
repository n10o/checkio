def checkio(expression):
    blackets = {"(":")", "{":"}", "[":"]"}
    stack = []
    for char in expression:
        for blacket in blackets.keys():
            if not stack and blackets[blacket] == char:
                return False
            if blacket == char:
                stack.append(blacket)
                break
            if stack and blackets[blacket] == char:
                if char != blackets[stack[-1]]:
                    return False
                else:
                    stack.pop()
                    break
    if stack:
        return False
    return True

assert checkio("((5+3)*2+1)") == True, "Simple"
assert checkio("{[(3+1)+2]+}") == True, "Different types"
assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
assert checkio("2+3") == True, "No brackets, no problem"
