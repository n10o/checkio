FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    speech = ""
    if number >= 100:
         speech += FIRST_TEN[int(str(number)[0])-1] + " " +  HUNDRED + " "
         number = int(str(number)[1:]) # cut first

    if number >= 20:
        speech += OTHER_TENS[int(str(number)[0])-2]
        if str(number)[1] != "0":
            speech += " " + FIRST_TEN[int(str(number)[1])-1]
    elif number >= 10:
        speech += SECOND_TEN[int(str(number)[1])]
    elif number == 0:
        pass
    else:
        speech += FIRST_TEN[number-1]

    return speech.rstrip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
