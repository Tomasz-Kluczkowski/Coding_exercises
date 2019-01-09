def anagram_check(s1: str, s2: str):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if len(s1) != len(s2):
        return False
    cache = {}
    for char in s1:
        cache[char] = cache.get(char, 0) + 1
    for char in s2:
        if not cache.get(char):
            return False
        cache[char] -= 1
    return sum(cache.values()) == 0


print(anagram_check('dog', 'god'))


