def biggest_substring(string):
    streak = 0
    record = 0
    charset = set()
    for char in string:
        if char not in charset:
            charset.add(char)
            streak += 1
            record = max(streak, record)
        else:
            charset.clear()
            charset.add(char)
            streak = 1
    return record


def longer_no_repeating_substring_len(string):
    biggest = 0
    for index, _ in enumerate(string):
        substr = set()
        for letter in string[index:]:
            if letter in substr:
                break
            substr.add(letter)
        if len(substr) > biggest:
            biggest = len(substr)
    return biggest


string = "serdevemuitolegalmasehprecisoestudarbastante"
print(biggest_substring(string))
print(longer_no_repeating_substring_len(string))
