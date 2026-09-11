s = input()
self_chars = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
from_chars = ['E', 'J', 'S', 'Z']
to_chars   = ['3', 'L', '2', '5']
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
def is_mirrored(s):
    for i in range(len(s)):
        st = s[i]
        op = s[len(s) - 1 - i]

        if st in self_chars:
            if st != op:
                return False
            continue

        in_pairs = False
        for k in range(len(from_chars)):
            if st == from_chars[k]:
                in_pairs = True
                if op != to_chars[k]:
                    return False
                break
            elif st == to_chars[k]:
                in_pairs = True
                if op != from_chars[k]:
                    return False
                break

        if not in_pairs:
            return False

    return True

if is_palindrome(s) and is_mirrored(s):
    print(s + " is a mirrored palindrome.") 
elif is_palindrome(s):
    print(s + " is a regular palindrome.")
elif is_mirrored(s):
    print(s + " is a mirrored string.")
else:
    print(s + " is not a palindrome.")