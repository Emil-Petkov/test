def palindrome(text):
    if text == text[::-1]:
        return f"({text}) => This is a palindrome."
    else:
        return f"({text}) => Not a palindrome."


print(palindrome(input("Еnter input and I'll tell you if it's a palindrome: ")))
