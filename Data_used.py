data=float(input("How many gb data you have used: "))

if data<= 12:
    cost=50
elif data<=30:
    cost=60
elif data<=50:
    cost=80
    
tax=cost+((cost*6.625)/100)
print(tax)
