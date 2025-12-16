using System;
using System.Collections.Generic;

class Topping
{
    public string name;
    public double price;

    public Topping(string name, double price)
    {
        this.name = name;
        this.price = price;
    }
}

class Pizza
{
    public string size;
    public string crust;
    public double basePrice;
    public List<Topping> toppings;

    public Pizza(string size, string crust)
    {
        this.size = size;
        this.crust = crust;
        this.toppings = new List<Topping>();

        // cena bazowa zależnie od rozmiaru
        if (size == "S") basePrice = 20;
        else if (size == "M") basePrice = 28;
        else if (size == "L") basePrice = 36;
        else basePrice = 28; // domyślnie M
    }

    public void AddTopping(Topping t)
    {
        toppings.Add(t);
    }

    public double TotalPrice()
    {
        double sum = basePrice;
        for (int i = 0; i < toppings.Count; i++)
        {
            sum += toppings[i].price;
        }
        return sum;
    }

    public void PrintPizza()
    {
        Console.WriteLine($"Pizza {size}, ciasto: {crust}");
        if (toppings.Count == 0)
        {
            Console.WriteLine("Dodatki: brak");
        }
        else
        {
            Console.WriteLine("Dodatki:");
            for (int i = 0; i < toppings.Count; i++)
            {
                Console.WriteLine("- " + toppings[i].name + " (+" + toppings[i].price.ToString("0.00") + " zł)");
            }
        }
        Console.WriteLine("Cena pizzy: " + TotalPrice().ToString("0.00") + " zł");
    }
}

class Order
{
    public List<Pizza> pizzas;

    public Order()
    {
        pizzas = new List<Pizza>();
    }

    public void AddPizza(Pizza p)
    {
        pizzas.Add(p);
    }

    public double TotalOrderPrice()
    {
        double sum = 0;
        for (int i = 0; i < pizzas.Count; i++)
        {
            sum += pizzas[i].TotalPrice();
        }
        return sum;
    }

    public void PrintSummary()
    {
        Console.WriteLine("\n=== PODSUMOWANIE ZAMÓWIENIA ===");
        for (int i = 0; i < pizzas.Count; i++)
        {
            Console.WriteLine("\n--- Pizza #" + (i + 1) + " ---");
            pizzas[i].PrintPizza();
        }
        Console.WriteLine("\nRAZEM DO ZAPŁATY: " + TotalOrderPrice().ToString("0.00") + " zł");
    }
}

class Program
{
    static void Main()
    {
        List<Topping> menu = new List<Topping>();
        menu.Add(new Topping("Ser extra", 4));
        menu.Add(new Topping("Szynka", 5));
        menu.Add(new Topping("Pieczarki", 4));
        menu.Add(new Topping("Papryka", 4));
        menu.Add(new Topping("Oliwki", 4));
        menu.Add(new Topping("Salami", 6));

        Order order = new Order();

        Console.WriteLine("=== APLIKACJA DO ZAMAWIANIA PIZZY ===");
        Console.Write("Ile pizz chcesz zamówić? ");
        int ile = Convert.ToInt32(Console.ReadLine());

        for (int i = 0; i < ile; i++)
        {
            Console.WriteLine("\n--- Tworzenie pizzy #" + (i + 1) + " ---");

            Console.Write("Wybierz rozmiar (S/M/L): ");
            string size = Console.ReadLine().ToUpper();

            Console.Write("Wybierz ciasto (cienkie/grube): ");
            string crust = Console.ReadLine().ToLower();

            Pizza pizza = new Pizza(size, crust);

            Console.WriteLine("\nDostępne dodatki:");
            for (int t = 0; t < menu.Count; t++)
            {
                Console.WriteLine((t + 1) + ". " + menu[t].name + " (+" + menu[t].price.ToString("0.00") + " zł)");
            }

            Console.Write("Ile dodatków chcesz dodać? ");
            int n = Convert.ToInt32(Console.ReadLine());

            for (int k = 0; k < n; k++)
            {
                Console.Write("Podaj numer dodatku: ");
                int nr = Convert.ToInt32(Console.ReadLine());

                if (nr >= 1 && nr <= menu.Count)
                {
                    pizza.AddTopping(menu[nr - 1]);
                }
                else
                {
                    Console.WriteLine("Błędny numer dodatku - pomijam.");
                }
            }

            order.AddPizza(pizza);
        }

        order.PrintSummary();
    }
}
