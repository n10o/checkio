# Our robots are always working to improve their linguistic skills.
# For this mission, they research the latin alphabet and its applications.
# The alphabet contains both vowel and consonant letters (yes, we divide the letters).
# Vowels -- A E I O U Y
# Consonants -- B C D F G H J K L M N P Q R S T V W X Z
# You are given a block of text with different words.
# These words are separated by white-spaces and punctuation marks.
# Numbers are not considered words in this mission
# (a mix of letters and digits is not a word either).
# You should count the number of words (striped words) where the vowels
# with consonants are alternating,
# that is; words that you count cannot have two consecutive vowels or consonants.
# The words consisting of a single letter are not striped -- do not count those.
# Casing is not significant for this mission.
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
NUMBERS = "1234567890"
PUNCTUATION = " ,."

def checkio(text):
    count = 0
    wordcount = 0
    isvowel = None
    striped = True
    for c in text:
        c = c.upper()
        wordcount += 1
        if striped == True:
            if c in VOWELS:
                if isvowel == True:
                    striped = False
                isvowel = True
                continue
            elif c in CONSONANTS:
                if isvowel == False:
                    striped = False
                isvowel = False
                continue
            elif c in NUMBERS:
                striped = False
                continue

        if c in PUNCTUATION:
            if striped == True and wordcount > 2:
                count += 1
            isvowel = None
            striped = True
            wordcount = 0

    if striped == True and wordcount > 2:
        count += 1

    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio(u"1 2 3 12 13") == 0, "Number"
