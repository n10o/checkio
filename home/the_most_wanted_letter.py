# You are given a text, which contains different english letters
# and punctuation symbols. You should find the most frequent letter
# in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter,
# so for the purpose of your search, "A" == "a".
# Make sure you do not count punctuation symbols,
# digits and whitespaces, only letters.
# If you have two or more letters with the same frequency,
# then return the letter which comes first in the latin alphabet.
# For example -- "one" contains "o", "n", "e" only once for each,
# thus we choose "e".

# TODO try one loop (instead of two loops
def checkio(text):
    count = {}
    for c in text:
        if c.isalpha():
            c = c.lower()
            if count.has_key(c):
                num = count[c]
                num += 1
                count[c] = num
            else:
                count[c] = 1
    maxkeys = []
    maxnum = ""
    for key in count.keys():
        num = count[key]
        if not maxkeys or maxnum < num:
            maxkeys = [key]
            maxnum = num
        elif maxnum == num:
            maxkeys.append(key)
    maxkeys.sort()
    return maxkeys[0]

if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
