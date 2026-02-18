Pesos = float(input("What do you have left  in pesos? "))
Soels = float(input("What do you have left in soles?"))
Reais = float(input("What do you have left in Reasis?"))

Pesos_Dollars = Pesos * 0.00024
Soels_Dollars = Soels * 0.27
Reais_Dollars = Reais * 0.17

Total = Pesos_Dollars + Soels_Dollars + Reais_Dollars

print ("The total cash left in dolalrs is: ", Total)
