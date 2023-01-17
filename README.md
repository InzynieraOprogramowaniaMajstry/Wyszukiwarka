# Wyszukiwarka

## Instalacja

Stworzenie wirtualnego środowiska
```
python -m venv venv
```

Aktywowanie środowiska
```
.\venv\Scripts\activate
```

Zainstalowanie wymaganych zależności
```
pip install -r requirements.txt
```

## Uruchamianie aplikacji w konsoli

Aktywowanie środowiska w nowej konsoli
```
.\venv\Scripts\activate
```
Uruchomienie strony internetowej.
```
flask run
```

## Sprawdzenie rekordów tabeli w schematach User oraz Book w VSCode
Zainstaluj rozszerzenie SQLite ze sklepu VSCode
Sprawdzenie User:
```
Użyj palety (ctrl + shift + p)
Wpisz  >sqlite new_query
select * from user
Uruchom plik (ctrl + shift + q)
```
Sprawdzenie Book:
```
Użyj palety (ctrl + shift + p)
Wpisz  >sqlite new_query
select * from book
Uruchom plik (ctrl + shift + q)
```

## Sprawdzenie rekordów tabeli w schematach User oraz Book w PyCharm
Dwa razy nacisnij na database.db

Zaakceptuj połączenie z SQLite

Z panelu bocznego `Database` można wejść w `database -> main -> tables -> book/user -> keys -> key #1` aby zobaczyć wszystkie rekordy w danym schemacie.

## Uruchomienie testów
```
coverage run -m unittest tests/test_*
```

## Otrzymanie informacji z testów
```
coverage report
```
## Wygenerowanie pliku HTML z informacji o testach
```
coverage html
```
## Dokumentacja użytkownika
Plik `dokumentacja_użytkownika.pdf`

## Dokumentacja techniczna
Plik `dokumantacja_techniczna.pdf`

## Pokrycie testami
```
Name                                          Stmts   Miss  Cover   Missing
---------------------------------------------------------------------------
config.py                                         5      0   100%
initialize_objects.py                            16      0   100%
models/database.py                               15      0   100%
models/database_operations.py                    63      0   100%
models/wolne_lektury_api.py                      59      0   100%
tests/test_database.py                           13      0   100%
tests/test_database_operations.py               104      0   100%
tests/test_wolne_lektury_api.py                  32      0   100%
tests/test_wolne_lektury_api_no_internet.py      37      0   100%
---------------------------------------------------------------------------
TOTAL                                           344      0   100%
```
## Przepuszczenie kodu przez SonarCloud
Dostęp do SonarCloud jest przyznawany po dołączeniu do organizacji.
![sonar](https://user-images.githubusercontent.com/47687092/212783089-7e4fe170-d26a-4cd6-98f5-a845e94a250d.png)
(Mimo wielu wysiłku nie udało się włączyć pokrycia testami z `coverage` do SonarCloudu)

