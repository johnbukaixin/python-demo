import functools

def cmp_ignore_case(s1, s2):
    newS1 = s1.lower()
    newS2 = s2.lower()
    if newS1 < newS2:
        return -1
    if newS1 > newS2:
        return 1
    return 0


sorted_ignore_case = functools.partial(sorted, key=(functools.cmp_to_key(cmp_ignore_case)))

print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))