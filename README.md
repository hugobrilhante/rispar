# Rispar - Test software engineer

#### rispartest.py
```
usage: python rispatest.py [-h] --files account.csv transactions.csv

Script to calculate balances

optional arguments:
  -h, --help            show this help message and exit
  --files account.csv transactions.csv
                        Enter the .csv files
```

#### Run Tests

`python -m venv venv`

`python -m pip install coverage`

`coverage run -m unittest discover`

`coverage report`

`coverage html` (_optional_)
