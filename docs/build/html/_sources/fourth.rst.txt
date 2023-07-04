4. Część analityczna
==================================================================

:Authors:
    Eryk Mika

:Version: 1.0 of 1.07.2023
:Course: Databases I

W tej części projektu zostały napisane moduły znajdujące się w katalogu **main** - **analiza.py** oraz **raport.py**. Pierwszy z wymienionych może zostać uruchomiony z poziomu notatnika Jupyter za pomocą linii kodu:

.. code-block:: Python

    from main.analiza import analiza
    analiza()

Moduł umożliwia filtrowanie rekordów w bazie danych PostgreSQL za pomocą ID klienta lub miejscowości odczytu.

Drugi moduł wykorzystuje numpy/matplotlib i może być wykorzystany do graficznego raportowania sumy odczytów wg miejscowości. Odbywa się to poprzez wykonanie następującego kodu w Jupyter Notebook z poziomu katalogu głównego projektu:

.. code-block:: Python

    from main.raport import raport
    raport()