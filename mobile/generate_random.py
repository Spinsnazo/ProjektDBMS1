import sqlite3
import random


def randomize():
    conn = sqlite3.connect("baza_danych.db")
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    
    cur.executescript("""CREATE TABLE IF NOT EXISTS klienci (
                                ID_klienta INTEGER PRIMARY KEY,
                                Imie VARCHAR(20) NOT NULL,
                                Nazwisko VARCHAR(20) NOT NULL
                            );

                            CREATE TABLE IF NOT EXISTS odczyty (
                                ID_odczytu INTEGER PRIMARY KEY AUTOINCREMENT,
                                Wartosc INTEGER NOT NULL,
                                Data_odczytu DATE DEFAULT (date('now')) NOT NULL,
                                Miejscowosc VARCHAR(20) NOT NULL,
                                Ulica VARCHAR(20) NOT NULL,
                                Nr_domu INTEGER NOT NULL,
                                Nr_mieszkania INTEGER NOT NULL,
                                ID_klienta INTEGER NOT NULL,
                                FOREIGN KEY (ID_klienta) REFERENCES klienci (ID_klienta) ON DELETE CASCADE
                            );""")
    
    names = [
    "Adam",
    "Adrian",
    "Aleksander",
    "Andrzej",
    "Antoni",
    "Arkadiusz",
    "Artur",
    "Bartek",
    "Bartłomiej",
    "Dawid",
    "Dominik",
    "Filip",
    "Grzegorz",
    "Hubert",
    "Jacek",
    "Jakub",
    "Jan",
    "Jarosław",
    "Jędrzej",
    "Kamil",
    "Karol",
    "Krzysztof",
    "Lukasz",
    "Maciej",
    "Marcin",
    "Marek",
    "Mariusz",
    "Mateusz",
    "Michał",
    "Mikołaj",
    "Norbert",
    "Patryk",
    "Paweł",
    "Piotr",
    "Rafał",
    "Robert",
    "Sebastian",
    "Szymon",
    "Tomasz",
    "Waldemar",
    "Witold",
    "Wojciech",
    "Zbigniew",
    "Zdzisław",
    "Łukasz",
    "Łukasz",
    "Łukasz",
    "Łukasz",
    "Łukasz"
    ]
    surnames = [
    "Kowalski",
    "Nowak",
    "Wiśniewski",
    "Wójcik",
    "Kowalczyk",
    "Kamiński",
    "Lewandowski",
    "Zieliński",
    "Szymański",
    "Woźniak",
    "Dąbrowski",
    "Kozłowski",
    "Jankowski",
    "Mazur",
    "Wojciechowski",
    "Kwiatkowski",
    "Krawczyk",
    "Kaczmarek",
    "Piotrowski",
    "Grabowski",
    "Zając",
    "Pawlak",
    "Michalski",
    "Król",
    "Nowicki",
    "Adamczyk",
    "Dudek",
    "Zalewski",
    "Wieczorek",
    "Jabłoński",
    "Krzyżewski",
    "Majewski",
    "Olszewski",
    "Jaworski",
    "Wróbel",
    "Malinowski",
    "Pawlowski",
    "Witkowski",
    "Walczak",
    "Stępień",
    "Górski",
    "Rutkowski",
    "Michalak",
    "Sikora",
    "Ostrowski",
    "Baran",
    "Tomaszewski",
    "Pietrzak",
    "Marciniak",
    "Wróblewski",
    "Zawadzki"
    ]
    
    cities = [
    "Wrocław",
    "Opole",
    "Wałbrzych",
    "Legnica",
    "Głogów",
    "Jaworzno",
    "Jastrzębie-Zdrój",
    "Racibórz",
    "Zielona Góra",
    "Gorzów Wielkopolski"
    ]
    
    streets = [
    "Krótka",
    "Słoneczna",
    "Polna",
    "Kościuszki",
    "Mickiewicza",
    "Kwiatowa",
    "Ogrodowa",
    "Łąkowa",
    "Cicha",
    "Szkolna",
    "Sportowa",
    "Leśna",
    "Klonowa",
    "Wąska",
    "Lipowa",
    "Kościelna",
    "Miodowa",
    "Sienkiewicza",
    "Sikorskiego",
    "Różana",
    "Długa",
    "Paderewskiego",
    "Wolności",
    "Piastowska",
    "Dworcowa",
    "Młyńska",
    "Kopernika",
    "Zamkowa",
    "Rynek",
    "Plac Wolności",
    "Mazowiecka",
    "Słowackiego",
    "Kasztanowa",
    "Akacjowa",
    "Kościuszki",
    "Władysława IV",
    "Krakowska",
    "Wojska Polskiego",
    "Wyszyńskiego",
    "Sobieskiego",
    "Jana Pawła II",
    "Olszynowa",
    "Nowa",
    "Boczna",
    "Wesoła",
    "Nadrzeczna",
    "Spokojna",
    "Kasprzaka",
    "Królowej Jadwigi",
    "Wiejska"
    ]

    
    for i in range(1000):
        cur.execute(f"INSERT INTO klienci VALUES ({i+1}, '{names[random.randint(0, len(names)-1)]}', '{surnames[random.randint(0, len(surnames)-1)]}')")
        cur.execute(f"""INSERT INTO odczyty (Wartosc, Miejscowosc, Ulica, Nr_domu, Nr_mieszkania, ID_klienta) VALUES
                    ({random.randint(500, 2000)}, '{cities[random.randint(0, len(cities)-1)]}', '{streets[random.randint(0, len(streets)-1)]}',
                    {random.randint(1, 20)}, {random.randint(0, 20)}, {i+1})""")
    conn.commit()
    

if __name__ == '__main__':
    randomize()
    