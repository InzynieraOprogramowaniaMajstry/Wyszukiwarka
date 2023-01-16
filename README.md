# Wyszukiwarka

## Installation

Create virtual environment
```
python -m venv venv
```

Active virtual environment
```
.\venv\Scripts\activate
```

Install application dependecies
```
pip install -r requirements.txt
```

## Run application in terminal

Active virtual environment in new terminal
```
.\venv\Scripts\activate
```

```
flask run
```

## see db inside
```
install sqlite extension in vsc
use command palette (ctrl + shift + p)
type  >sqlite new_query
select * from user
run file (ctrl + shift + q)
```

## run tests
```
python -m pytest -vv
```

## get test coverage information
```
coverage run -m pytest
coverage report
```
