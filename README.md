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
