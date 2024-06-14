def pallindrome(n):
    for i in range(0 , int(len(n) / 2)):
        if n[i] != n[len(n) - i - 1]:
            return False
        
    return True

print(pallindrome("ABC"))