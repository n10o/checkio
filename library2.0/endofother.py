def checkio(words_set):
  # TODO this implementation is slow
  for base in words_set:
    for op in words_set:
      if op == base:
        continue
      if base.endswith(op):
        return True
  return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
  assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
  assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
  assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
  assert checkio({u"one"}) == False, "Only One"
  assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"
