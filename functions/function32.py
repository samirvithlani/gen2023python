data = ["ram","amit","manan","madam","malayalam","a","jar","rr","rrr",100,20,False,True,12.34]
#str,palindrome,4

def isPalindrome(x):
    
    if type(x) == str:
        if x == x[::-1] and len(x)>3:
            return True
        else:
            return False
    
    return False


newList = list(filter(lambda x: isPalindrome(x),data))
print(newList)
    
            