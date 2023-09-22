n1= input("digete numero 1 ")
n1= float(n1)

n2= input("digite numero 2 ")
n2= float(n2)

n3= input("digite numero 3 ")
n3= float(n3)

if n1 > n2 and n1 > n3:
    print(str(n1) + "é o maior numero")

elif n2 > n1 and n2 > n3:
    print(str(n2) + "é o maior numero") 

else:
     print(str(n3) + "é o maior numero") 
