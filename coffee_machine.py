money = 550
water = 400
milk = 540
beans = 120
cups = 9


class Coffee:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def fill(self):
        self.water += int(input("how much water do you want to add?"))
        self.milk += int(input("how much milk do you want to add?"))
        self.beans += int(input("how much coffee do you want to add?"))
        self.cups += int(input("how much cups do you want to add?"))

    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(f"${self.money} of money")


    def take(self):
        print(f"i gave you ${self.money}")
        self.money = 0


    def prepare(self, a, b, c, m):
        self.water -= a
        self.milk -= b
        self.beans -= c
        self.money += m
        self.cups -= 1

    def espresso(self):
        if self.water > 250 and self.beans > 16:
            self.prepare(250, 0, 16, 4)
            print("I have enough resources, making you a coffee!")
        else:
            print("Sorry, not enough water!")

    def latte(self):
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20:
            print("I have enough resources, making you a coffee!")
            self.prepare(350, 75, 20, 7)
        elif water < 350:
            print("Sorry, not enough water!")
        elif milk < 75:
            print("Sorry, not enough milk!")
        elif beans < 20:
            print("Sorry, not enough beans!")

    def cappucino(self):
        if self.water > 200 and self.milk > 100 and self.beans > 12:
            self.prepare(200, 100, 12, 6)
            print("I have enough resources, making you a coffee!")
        else:
            print("Sorry, not enough water!")

    def action(self):
        while True:
            request = input("would you like to buy, fill, or take, remaining, exit ?")
            if request == "buy":
                coffee_type = (input("would you like espresso, latte, or cappuccino?, or go back to main menu"))
                if coffee_type == "1":
                    self.espresso()
                elif coffee_type == "2":
                    self.latte()
                elif coffee_type == "3":
                    self.cappucino()
                elif coffee_type == "back":
                    pass
            if request == "fill":
                self.fill()
            if request == "take":
                self.take()
            if request == "remaining":
                self.remaining()
            if request == "exit":
                exit()

machine = Coffee()
machine.action()