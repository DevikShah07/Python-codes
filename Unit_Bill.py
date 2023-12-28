unit=float(input("how many total unit u have used: "))

if unit <=50:
    rs=0.50*unit
elif 50< unit <=150:
    rs=25+((50-unit)*0.75)
elif 150< unit <= 250:
    rs=100+((150-unit)*1.20)
elif unit> 250:
    rs=220+((250-unit)*1.50)
    
tax=rs+((rs*20)/100)
print(tax)
