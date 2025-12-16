def read_float(prompt):
    while True:
        try:
            s = input(prompt)
            return float(s)
        except (ValueError, TypeError):
            print("Błędna liczba, spróbuj ponownie.")


def read_int_positive(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            print("Podaj liczbę większą od 0.")
        except (ValueError, TypeError):
            print("Błędna wartość, spróbuj ponownie.")


def kalkulator():
    a = read_float("Podaj pierwszą liczbę: ")
    b = read_float("Podaj drugą liczbę: ")
    op = input("Wybierz operację (+, -, *, /): ").strip()

    if op == "+":
        print("Wynik:", a + b)
    elif op == "-":
        print("Wynik:", a - b)
    elif op == "*":
        print("Wynik:", a * b)
    elif op == "/":
        if b != 0:
            print("Wynik:", a / b)
        else:
            print("Błąd: nie można dzielić przez zero.")
    else:
        print("Błąd: nieznana operacja.")


def konwerter_temperatur():
    kier = input("Wybierz kierunek (C - Celsjusz->Fahrenheit, F - Fahrenheit->Celsjusz): ").strip().upper()
    temp = read_float("Podaj temperaturę: ")

    if kier == "C":
        f = temp * 1.8 + 32
        print(f"{temp}°C = {f}°F")
    elif kier == "F":
        c = (temp - 32) / 1.8
        print(f"{temp}°F = {c}°C")
    else:
        print("Błąd: nieznany kierunek konwersji.")


def srednia_ocen():
    n = read_int_positive("Ile ocen chcesz wprowadzić? ")
    suma = 0.0
    for i in range(n):
        oc = read_float(f"Podaj ocenę {i+1}: ")
        suma += oc
    sred = suma / n
    print(f"Średnia: {sred:.2f}")
    if sred >= 3.0:
        print("Uczeń zdał.")
    else:
        print("Uczeń nie zdał.")


def main():
    while True:
        print("=== MENU ===")
        print("1 - Kalkulator (+, -, *, /)")
        print("2 - Konwerter temperatur (C <-> F)")
        print("3 - Średnia ocen ucznia")
        print("q - Wyjście")
        wybor = input("Wybierz zadanie (1/2/3/q): ").strip()

        if wybor == "1":
            kalkulator()
        elif wybor == "2":
            konwerter_temperatur()
        elif wybor == "3":
            srednia_ocen()
        elif wybor.lower() == "q":
            print("Do widzenia!")
            break
        else:
            print("Błąd: nieprawidłowy wybór.")


if __name__ == "__main__":
    main()
    input("Naciśnij Enter, aby zamknąć...")
