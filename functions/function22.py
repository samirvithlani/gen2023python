#hi this is india

def findMaxWord(name):
    x = name.split()
    return max(x,key=len)


ans = findMaxWord("hi this is xms india")
print(ans)