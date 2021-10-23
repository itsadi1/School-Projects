import random

def add(x,y): 
    return x+y
    

def sub(x,y):
    return x-y
    
    
def mul(x,y):
    return x*y
    
    
def div(x,y):
    return round((x/y),2)
    
    
def operator(z):
    if z == "+":
        R = add(x,y)
    elif z == "-":
        R = sub(x,y)
    elif z == "*":
        R = mul(x,y)
    else :
        R = div(x,y)
    return R



def CheckInput(strN):
    if len(strN)>3 and strN[-4]==",":
        N = eval(strN.replace(",",""))
    else:
        try:
           N = eval(strN)
        except TypeError:
            answer = False 
    return N


def LivesAndScore(live, score, R, N):
    if answer == True:
        print(f"+1\nYour score: {score}\n")
    elif answer == False:
        live -= 1
        score -= 1
        print(f"oops! The correct Answer  is {R}\nNo. of lives left: {live}\n")
    elif score == 100:
        print("You Win!\nYour score: 100")
    else:
        pass
    return live, score


print("Welcome...")
operators = ("+","-","*","/")
x = random.randint(1, 99)
y = random.randint(1, 99)
n, score, live = 0, 0, 3
while score <= 100:
    n+=1
    score+=1
    x = random.randint(1, 99)
    y = random.randint(1, 99)
    z = random.choice(operators)
    strN = input(f"{n}). {x} {z} {y} = ")
    N = CheckInput(strN)  
    R = operator(z)
    answer = N==R
    live, score = LivesAndScore(live, score, R, N)
    if live == 0:
        print(f"You Lose! Your score: {score}")
        break

 
