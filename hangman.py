word="python"
list=["_"]*len(word)
print('''
___________
|      |
|      O
|     \\|/
|     / \\
|
      ''')
stages=[

    '''

|      
|      
|     
|     
|
''',
'''
___________
|      
|      
|     
|     
|
''',
'''
___________
|      |
|      
|     
|     
|
''',
'''
___________
|      |
|      O
|     
|     
|
''',
'''
___________
|      |
|      O
|      |
|     
|
'''
,
'''
___________
|      |
|      O
|     \\|
|     
|
'''
,
'''
___________
|      |
|      O
|     \\|/
|     
|
'''
,
'''
___________
|      |
|      O
|     \\|/
|     / 
|
'''
,
'''
___________
|      |
|      O
|     \\|/
|     / \\
|
'''

]
count=0

while True:
    print("pick a letter")
    ans=input()
    if ans in word:
        for i in range(len(word)):
            if word[i]==ans:
                list [i]=ans
    else:
        print("your guess is incorrect")
        print (stages[count])
        count=count+1
        print(count)
        if count==9:
            print("you lost")
            break
    print(" ".join(list))
    
    if "".join(list)==word:
        print("you did it!")
        break
