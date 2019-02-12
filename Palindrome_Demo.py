Palindrome=input('Please enter a palindrome:')
Palindrome=Palindrome.lower()


if(Palindrome==Palindrome[::-1]):
    print('Yes that string is palindrome')
else:
    print('That string is not a palindrome')