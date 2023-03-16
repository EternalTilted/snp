def is_palindrome(string):
    string = str(string).lower()

    buf = ''
    for i in str(string):
        if(i.isalnum()):
            buf+=i

    if buf == ''.join(reversed(buf)):
        return True
    else:
        return False


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))

