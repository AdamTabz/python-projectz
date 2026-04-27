import random
list1=["guess it", "good day"]
word=random.choice(list1)
wlist=list(word)
random.shuffle(wlist)
jmbl="".join(wlist)
while True:
    print("try to solve the puzzle")
    print(jmbl)
    guess=input()
    if guess==word:
        print("you solved it")
        break
    else:
        print("try again")


