products={"shoes":120,"shirt":20,"pants":60,"sweater":50,"hat":15}
cart={}

while True:

    print(products)
    print("what do you want?")
    thing=input()
    if thing=="stop":
        break
    print("how many?")
    num=int(input())
    cart[thing]=num
    
    print(cart)
total=0

for key, value in cart.items():
    print(key, value, products[key])
    amount=value*products[key]
    total=total+amount

    print(amount)
print(total)