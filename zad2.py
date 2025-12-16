class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Pizza:
    def __init__(self, size, crust):
        self.size = size
        self.crust = crust
        self.toppings = []

        # cena bazowa zależnie od rozmiaru
        if size == "S":
            self.basePrice = 20
        elif size == "M":
            self.basePrice = 28
        elif size == "L":
            self.basePrice = 36
        else:
            self.basePrice = 28  # domyślnie M

    def AddTopping(self, t):
        self.toppings.append(t)

    def TotalPrice(self):
        sum = self.basePrice
        for topping in self.toppings:
            sum += topping.price
        return sum

    def PrintPizza(self):
        print(f"Pizza {self.size}, ciasto: {self.crust}")
        if len(self.toppings) == 0:
            print("Dodatki: brak")
        else:
            print("Dodatki:")
            for topping in self.toppings:
                print(f"- {topping.name} (+{topping.price:.2f} zł)")
        print(f"Cena pizzy: {self.TotalPrice():.2f} zł")

class Order:
    def __init__(self):
        self.pizzas = []

    def AddPizza(self, p):
        self.pizzas.append(p)

    def TotalOrderPrice(self):
        sum = 0
        for pizza in self.pizzas:
            sum += pizza.TotalPrice()
        return sum

    def PrintSummary(self):
        print("\n=== PODSUMOWANIE ZAMÓWIENIA ===")
        for i, pizza in enumerate(self.pizzas, 1):
            print(f"\n--- Pizza #{i} ---")
            pizza.PrintPizza()
        print(f"\nRAZEM DO ZAPŁATY: {self.TotalOrderPrice():.2f} zł")

def main():
    menu = [
        Topping("Ser extra", 4),
        Topping("Szynka", 5),
        Topping("Pieczarki", 4),
        Topping("Papryka", 4),
        Topping("Oliwki", 4),
        Topping("Salami", 6)
    ]

    order = Order()

    print("=== APLIKACJA DO ZAMAWIANIA PIZZY ===")
    ile = int(input("Ile pizz chcesz zamówić? "))

    for i in range(ile):
        print(f"\n--- Tworzenie pizzy #{i + 1} ---")

        size = input("Wybierz rozmiar (S/M/L): ").upper()
        crust = input("Wybierz ciasto (cienkie/grube): ").lower()

        pizza = Pizza(size, crust)

        print("\nDostępne dodatki:")
        for t, topping in enumerate(menu, 1):
            print(f"{t}. {topping.name} (+{topping.price:.2f} zł)")

        n = int(input("Ile dodatków chcesz dodać? "))

        for k in range(n):
            nr = int(input("Podaj numer dodatku: "))

            if 1 <= nr <= len(menu):
                pizza.AddTopping(menu[nr - 1])
            else:
                print("Błędny numer dodatku - pomijam.")

        order.AddPizza(pizza)

    order.PrintSummary()

if __name__ == "__main__":
    main()