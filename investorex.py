porcentage = float(input("What is the anual interest percentage of your investment?"))
investquant = float(input("How much money do you want to invest?"))
years = int(input("Tell me how much years do you want to be investing."))
interest = porcentage//100
anualinvest = investquant + (investquant*interest)
totalinvest = anualinvest*years
print(f"If you invest {investquant}$, your anual earnings will be {anualinvest}, and your total earnings will be {totalinvest}.")