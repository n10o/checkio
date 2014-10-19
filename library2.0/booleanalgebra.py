OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
  if operation in OPERATION_NAMES:
    if operation == "conjunction":
      return x and y
    elif operation == "disjunction":
      return x or y
    elif operation == "implication":
      return 0 if x == 1 and y == 0 else 1
    elif operation == "exclusive":
      return 0 if x == y else 1
    else:
      return 1 if x == y else 0

  return False

if __name__ == '__main__':
  #These "asserts" using only for self-checking and not necessary for auto-testing
  assert boolean(1, 0, "conjunction") == 0, "and"
  assert boolean(1, 0, "disjunction") == 1, "or"
  assert boolean(1, 1, "implication") == 1, "material"
  assert boolean(0, 1, "exclusive") == 1, "xor"
  assert boolean(0, 1, "equivalence") == 0, "same?"
