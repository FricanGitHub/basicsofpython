def main():

    print("\t\t\tWitaj w kalkulatorze! Zacznijmy z wpisaniem naszych x i y, menu zajmiemy się później!")
    x = float(input("\nWpisz x: "))
    y = float(input("Wpisz y: "))
    print("Twoje x wynosi: ",(x),"a y wynosi:", (y),)
    print(" 1. Dodawanie\n 2. Odejmowanie\n 3. Mnożenie\n 4.Dzielenie\n 5.Reszta z dzielenia modulo\n")
    mathmenu= float(input("Wybierz cyfrę od 1 do 5, w zależności jakie działanie chcesz wykonać!"))

    if mathmenu > 5:
        print("Nie wybrałeś cyfry z menu, koniec programu")
    if mathmenu == 0:
        print("Nie wybrałeś cyfry z menu, koniec programu")

    if mathmenu == 1:
        suma = x + y
        print("Suma wynosi", suma)
    if mathmenu == 2:
        roznica = x - y
        print("Różnica wynosi",roznica)
    if mathmenu == 3:
        iloczyn = x * y
        print("Iloczyn wynosi", iloczyn)
    if mathmenu ==4:
        iloraz = x / y
        print("Iloraz wynosi", iloraz)
    if mathmenu ==5:
        modulo = x % y
        print("Modulo wynosi", modulo)


while True:
    main()
    powtorzenieprogramu = str(input("Czy chcesz coś jeszcze obliczyć? (tak/nie)"))
    if powtorzenieprogramu != "tak" :
        break