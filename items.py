while True:
    items={"shoes":120,"shirt":20,"pants":60,"sweater":50,"hat":15}
    cart={}
    print(items)
    print("what do you want?")
    thing=input()
    if thing=="stop":
        break
    print("how many?")
    num=int(input())
    cart[thing]=num
    print(cart)
   