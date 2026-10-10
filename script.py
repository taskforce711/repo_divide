def factores(n)

if n % 3 == 0:
    print("Divisible entre 3")
else:
    print ("NO es divisible entre 3")

  if n % 5 == 0:
      print("Divisible entre 5")
  else: 
      print("NO es divisible entre 5")



num = int(input("Da un entero: "))
factores(num)
print("Goodbye")



