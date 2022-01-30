import random
def digitcheck(n):
    s = str(n)
    if(len(s)==4):
        return True
    else :
        return False
def repCheck(n):
    a = list(str(n))
    b = True
    for i in a:
        if(a.count(i)>1):
            b = False
    return b
def cowbull(choice,ans):
    cow=0
    bull = 0
    ans = list(str(ans))
    choice = list(str(choice))
    for i in range(0,len(ans)):
        if(ans[i]==choice[i]):
            bull += 1
            choice[i]=''
    for i in choice:
        cow += ans.count(i)
    
    a = (cow,bull)
    return a

    
    

answer = random.randint(1000,9999)
while(not repCheck(answer)):
    answer = random.randint(1000,9999)

chance = 6
while(chance >0):

    cho = int(input("Enter your choice          "))
    if(not digitcheck(cho)):
        print("Enter a four digit number only")
        continue
    if(not repCheck(cho)):
        print("invalid Choice; no repetetion of digits allowed")
        continue
    b = cowbull(cho,answer,)
    print("Cows ",b[0],"    Bulls   ",b[1] , "\n", "Chances left", chance)
    if(b[1]==4):
        print("Correct guess" )
        break
    chance = chance - 1
print("corect answer is ",answer)
