water = 400
milk = 420
coffe_beans = 120
cups = 9
money = 500
espresso = {water :  250, coffe_beans : 120, cups : 1, money : 4}

def buy():
    question = input("Write action (buy, fill, take): ")
    global water, milk, coffe_beans, cups, money
    if question =="buy":
        wtb = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        if wtb == "espresso":
            water = water - 250
            coffe_beans= coffe_beans - 16
            money = money + 4
            cups = cups - 1
            return("The coffee machine has: ")
            return(water)
            return(milk )
            return(coffe_beans)
            return(cups)
            return(money)
        elif wtb == "latte":
            water = water - 350
            milk = milk - 75
            coffe_beans= coffe_beans - 20
            money = money + 7
            cups = cups - 1
            return("The coffee machine has: ")
            return(water)
            return(milk )
            return(coffe_beans)
            return(cups)
            return(money)
        else: 
            water = water -  200 
            milk = milk - 100
            coffe_beans= coffe_beans - 12
            money = money + 6
            cups = cups - 1
            return("The coffee machine has: ")
            return(water)
            return(milk )
            return(coffe_beans)
            return(cups)
            return(money)
    else: pass
       
def fill():
    question = input("Write action (buy, fill, take): ")
    global water, milk, coffe_beans, cups, money
    if question == "fill": 
       watter_add = input(int("Write how many ml of water you want to add:"))
       milk_add = input(int("Write how many ml of milk you want to add:"))
       coffe_add = input(int("Write how many grams of coffee beans you want to add:"))
       cupps_add = input(int("Write how many disposable coffee cups you want to add:"))
       return("The coffee machine has: ")
       water = water + watter_add
       milk = milk + milk_add
       coffe_beans = coffe_beans + coffe_add
       cups = cups + cupps_add
       return(f"{water} + of water")
       return(f"{milk} + of mil")
       return(f"{coffe_beans} + of water")
       return(f"{cups} + of coffee beans")
       return(f"{money} + of money")
    else: pass
def take():
    question = input("Write action (buy, fill, take): ")
    global water, milk, coffe_beans, cups, money
    if question == "take":
        return(f" I gave you {money}")
        money = money - money
        return("The coffee machine has")
        return(f" I gave you {money}")
        return(f"{water} of water")
        return(f"{milk} of milk")
        return(f"{coffe_beans} of coffee beans")
        return(f"({cups} cups of disposable cups")
        return(f"({money} of money")
    else:
        pass
buy()
fill()
take()