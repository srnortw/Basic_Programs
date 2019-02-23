def biggest_polindrome_number(amount_of_digit):
    quantity=10**amount_of_digit
    quantity1=10**(amount_of_digit-1)

    a=list(range(quantity1,quantity))
    b=list(range(quantity1,quantity))
    b=b[::-1]
    a=a[::-1]
    palindrome=0

    for x in range(0,quantity-quantity1):
        for p in range(0,quantity-quantity1):
            c=a[p]*b[x]
            mystr=str(c)
            if mystr[::-1] == mystr:
                if c>palindrome:
                    palindrome=c
                    print(f"Maybe our result is this:{palindrome}")
                else:
                    pass
            else:
                pass

    print("Precise result is:")
    return palindrome

print(biggest_polindrome_number(6))
#Enter number of digits.And learn max palindrome about that number of digits

