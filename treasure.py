import random 
for i in range(5):
    print("_ _ _ _ _")
t_c=random.randint(1,5)
t_r=random.randint(1,5)
while True:
    print("pick two numbers")
    c=int(input())
    r=int(input())
    if c< t_c:
        print("move to the right")
    elif r<t_r:
        print("move down")
    elif c>t_c:
        print("move to the left")
    elif r >t_r:
        print("move up")
   
    elif c==t_c and r==t_r:
        print("you found the treasure!!")
        break
    if c==t_c:
        print("the colum is correct")
    elif r==t_r:
         print("the row is correct")