import random
times = 5
secret = random.randint(1,50) 
guess = 0
while  (guess != secret) and (times>0):
    temp = input("Please input a number(1-50).\n")
    guess = int(temp)
    times = times-1
    if  guess == secret:
        print("success!!!")
    elif guess<secret:
        print("biger!!!")
    else :
        print("less!!!")
if times<=0:
    print("have no times")
print("game end")
