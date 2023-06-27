3. Instrukcja obsługi skryptów do pracy z bazą danych PostgreSQL
==================================================================

:Authors:
    Eryk Mika

:Version: 1.0 of 22.06.2023
:Course: Databases I


Skrypty do obłsugi głównej bazy danych
------------------------------------------------

Zostały sporządzone skrypty do obsługi bazy danych PostgreSQL. Są one umieszczone w katalogu **main_db**. Należą do nich:

#. **buduj.py** - uruchomienie tego skryptu spowoduje utworzenie (jeżeli jeszcze nie istnieje) struktury bazy danych zgodnej z modelem użytym w aplikacji klienckiej (tabele klienci oraz odczyty)

#. **czysc.py** - skrypt ten powoduje wyczysczenie bazy danych (ale nie usunięcie jej struktury)

#. **importuj.py** - umożliwia zaimportowanie danych z plików csv o nazwach podanych przez użytkownika

#. **wprowadz.py** - umożliwia wprowadzenie kilku wierszy danych do bazy danych (klientów/odczytów)

#. **wynik.py** - odczytanie wyników

W wyżej wspominanym katalogu należy umieścić plik JSON **database_creds.json**, który zawiera dane logowania do bazy danych PostgreSQL, tj. w formacie:

.. code-block:: JSON

    {
     "user_name": "nazwa uzytkownika",
     "password": "haslo",
     "host_name": "adres IP/nazwa hosta",
     "port_number": "port, 5432",
     "db_name": "nazwa bazy danych"
    }
