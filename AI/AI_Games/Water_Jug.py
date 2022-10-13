from collections import defaultdict

j1,j2=4,3
check =defaultdict(lambda: False)
queue = []
count = 0

def btoaa(a,b):
    if a+b>4:
        x=b-(4-a)
        return 4
    else:
        return a+b

def btoab(a,b):
    if a+b>4:
        x=b-(4-a)
        return x
    else:
        return 0


def atoba(a,b):
    if a+b>3:
        x=a-(3-b)
        return x
    else:
        return 0


def atobb(a,b):
    if a+b>3:
        x=a-(3-b)
        return 3
    else:
        return a+b


def solve(a,b):
    if a==2:
        print(a,b)
        return True

    if check[(a,b)]==False:
         print(a,b)
         check[(a,b)]=True
         return (solve(0,b) or solve(a,0) or solve(4,b) or solve(a,3) or solve(btoaa(a,b),btoab(a,b)) or solve(atoba(a,b),atobb(a,b)))
    else:
        return False


print("Water Jug Problem :")
print("Enter Initial value of Jugs : ")
print("Jug 1 :")
a=int(input())
print("Jug 2 :")
b=int(input())
print("The solution is :")
solve(a,b)