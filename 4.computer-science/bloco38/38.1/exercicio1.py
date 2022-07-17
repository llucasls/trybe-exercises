def can_write(word, chars):
    charset = {character for character in chars}
    chardict = dict([(character, 0) for character in charset])
    for char in chars:
        chardict[char] += 1
    for letter in word:
        try:
            chardict[letter] -= 1
        except KeyError:
            return False
    return min(chardict.values()) >= 0


def total_length(words, chars):
    valid_words = []
    for word in words:
        if can_write(word, chars):
            valid_words.append(word)
    return len("".join(valid_words))
