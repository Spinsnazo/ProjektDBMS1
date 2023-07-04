import psycopg
import json


def analiza():
    try:
        # Odczytaj plik JSON
        with open("database_creds.json", "r") as json_file:
            dane = json.loads(json_file.read())
        # Polacz sie z baza danych
        conn = psycopg.connect(dbname=dane["db_name"],
                                user=dane["user_name"],
                                password=dane["password"],
                                host=dane["host_name"],
                                port=dane["port_number"]
                               )
        wybor = input("Czy chcesz filtrować rekordy wg ID klienta (k), miejscowości odczytu (m) czy filtrować wg zużycia (z)? ")
        with conn.cursor() as cur:
            if wybor.casefold() == 'k':
                id = int(input("Prosze podac ID klienta: "))
                cur.execute(f"""SELECT ID_odczytu, Wartosc, Data_odczytu, Miejscowosc, Ulica, Nr_domu, Nr_mieszkania
                            FROM odczyty WHERE ID_klienta = {id}""")
                print("Wybrane rekordy") 
                print(f"""{"ID odczytu":20}{"Wartość":20}{"Data odczytu":20}{"Miejscowość":20}"""
                      f"""{"Ulica":20}{"Nr domu":20}{"Nr mieszkania":20}""")

            elif wybor.casefold() == 'm':
                city = input("Prosze podac nazwe miejscowosci: ")
                cur.execute(f"""SELECT klienci.ID_klienta, klienci.Imie, klienci.Nazwisko, odczyty.ID_odczytu, odczyty.Wartosc,
                            odczyty.Data_odczytu, odczyty.Ulica, odczyty.Nr_domu, odczyty.Nr_mieszkania FROM klienci, odczyty WHERE
                            odczyty.Miejscowosc = '{city}' and odczyty.ID_klienta = klienci.ID_klienta""")
                print("Wybrane rekordy") 
                print(f"""{"ID klienta":20}{"Imię":20}{"Nazwisko":20}{"ID odczytu":20}"""
                      f"""{"Wartosc":20}{"Data odczytu":20}{"Ulica":20}{"Nr domu":20}{"Nr mieszkania":20}""")
            else:
                print("Opcje do wyboru: ")
                print("1.  >       większe niż")
                print("2.  <       mniejsze niż")
                print("3.  < x <   pomiędzy")
                wybor = input("Twój wybór: ")
                down, up = 0, 10000
                down = input("Wartosc 1: ")
                if wybor == "3":
                    up = input("Wartosc 2: ")
                select_str = None
                if wybor == "1":
                    select_str = f"odczyty.Wartosc > {down} ORDER BY odczyty.Wartosc ASC;"
                elif wybor == "2":
                    select_str = f"odczyty.Wartosc < {down} ORDER BY odczyty.Wartosc ASC;"
                else:
                    select_str = f"odczyty.Wartosc > {down} AND odczyty.Wartosc < {up} ORDER BY odczyty.Wartosc ASC;"
                cur.execute(f"""SELECT klienci.ID_klienta, klienci.Imie, klienci.Nazwisko, odczyty.ID_odczytu, odczyty.Wartosc,
                            odczyty.Data_odczytu, odczyty.Miejscowosc, odczyty.Ulica, odczyty.Nr_domu, odczyty.Nr_mieszkania FROM klienci, odczyty
                            WHERE klienci.ID_klienta = odczyty.ID_klienta AND """ + select_str)
                print("Wybrane rekordy") 
                print(f"""{"ID klienta":20}{"Imię":20}{"Nazwisko":20}{"ID odczytu":20}"""
                      f"""{"Wartosc":20}{"Data odczytu":20}{"Miejscowość":20}{"Ulica":20}{"Nr domu":20}{"Nr mieszkania":20}""")
                
            for item in cur.fetchall():
                for attribute in item:
                    print(f"{str(attribute):20}", end="")
                print()
                
    except Exception as ex:
        print("Wystapil blad poczas analizy danych! " + str(ex))
    

if __name__ == '__main__':
    analiza()