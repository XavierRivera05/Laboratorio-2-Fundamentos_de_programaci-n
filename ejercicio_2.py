print("numeros enteros")

num1=int(input('Ingrese cualquier numero\n'))

num2= int(input('ingrese un segundo numero\n'))

num3= int(input('Ingrese un tercer numero\n'))

if num1<num3 and num2< num3:

    print(num3, ' es el numero mayor' )

    if num1<num2:

        print(num2, 'es el segundo numero mas alto')

        print("el numero mas pequeño es ", num1)

    else: print()

elif num1>num2 and num1 > num3:

    print(num1, ' es el numero mayor')

    if num3<num2:

        print(num2, 'es el segundo numero mas alto')

        print("el numero mas pequeño es ", num3)

    else: print()

elif num2>num1 and num2 > num3:

    print(num2,"es el numero mayor")

    if num1<num3:

        print(num2, 'es el segundo numero mas alto')

        print("el numero mas pequeño es ", num2)

    else:print()

print("FINAL") 
print("Xavier Rivera, Eduardo Arteaga")
