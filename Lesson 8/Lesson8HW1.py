def is_palindrome(word):
    stack = []

    
    for char in word:
        stack.append(char)

    
    for char in word:
        if char != stack.pop():
            return False

    return True


print(is_palindrome("racecar"))
print(is_palindrome("level"))
print(is_palindrome("hello"))