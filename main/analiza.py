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
        wybor = input("Czy chcesz filtrować rekordy wg ID klienta (k) czy miejscowości odczytu (m)? ")
        with conn.cursor() as cur:
            if wybor.casefold() == 'k':
                id = int(input("Prosze podac ID klienta: "))
                cur.execute(f"""SELECT ID_odczytu, Wartosc, Data_odczytu, Miejscowosc, Ulica, Nr_domu, Nr_mieszkania
                            FROM odczyty WHERE ID_klienta = {id}""")
                print("Wybrane rekordy (ID odczytu/Wartosc/Data odczytu/Miejscowosc/Ulica/Nr domu/Nr mieszkania): ")
                for item in cur.fetchall():
                    for attribute in item:
                        print(f"{str(attribute):20}", end="")
                    print()
            else:
                city = input("Prosze podac nazwe miejscowosci: ")
                cur.execute(f"""SELECT klienci.ID_klienta, klienci.Imie, klienci.Nazwisko, odczyty.ID_odczytu, odczyty.Wartosc,
                            odczyty.Data_odczytu, odczyty.Ulica, odczyty.Nr_domu, odczyty.Nr_mieszkania FROM klienci, odczyty WHERE
                            odczyty.Miejscowosc = '{city}' and odczyty.ID_klienta = klienci.ID_klienta""")
                print("Wybrane rekordy (ID odczytu/Wartosc/Data odczytu/Miejscowosc/Ulica/Nr domu/Nr mieszkania): ")
                for item in cur.fetchall():
                    for attribute in item:
                        print(f"{str(attribute):20}", end="")
                    print()
    except Exception as ex:
        print("Wystapil blad poczas analizy danych! " + str(ex))
    

if __name__ == '__main__':
    analiza()