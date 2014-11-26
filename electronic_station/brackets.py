# You are given an expression with numbers,
# brackets and operators. For this task only the brackets matter.
# Brackets come in three flavors: "{}" "()" or "[]".
# Brackets are used to determine scope or to restrict some expression.
# If a bracket is open, then it must be closed with a closing bracket
# of the same type. The scope of a bracket must not intersected
# by another bracket. For this task, you should to make a decision
# to correct an expression or not based on the brackets.
# Do not worry about operators and operands.

def checkio(expression):
    blackets = {"(":")", "{":"}", "[":"]"}
    stack = []
    for c in expression:
        if c in blackets.keys():
            stack.append(blackets[c])
        if c in blackets.values():
            if stack == [] or c != stack[-1]:
                return False
            stack.pop()
    if stack:
        return False
    return True

assert checkio("((5+3)*2+1)") == True, "Simple"
assert checkio("{[(3+1)+2]+}") == True, "Different types"
assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
assert checkio("2+3") == True, "No brackets, no problem"
