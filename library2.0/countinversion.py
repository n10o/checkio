def count_inversion(sequence):
  basepointer = 0
  pointer = 1
  count = 0
  while True:
    opponent = basepointer + pointer
    if len(sequence) <= opponent:
      break
    base = sequence[basepointer]
    if base > sequence[opponent]:
      count += 1
      pointer += 1
    else:
      basepointer += pointer
      pointer = 1
  print count

  return count

if __name__ == '__main__':
  #These "asserts" using only for self-checking and not necessary for auto-testing
  assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
  assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
  assert count_inversion((99, -99)) == 1, "Two numbers"
  assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
