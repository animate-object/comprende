# ¿Comprende?
What if you had to read an article before you commented on it?
Generating efficient reading recall tests and basic understanding (topics, authorship, etc).


## Installation

### Pre-reqs
* `> python 3.8` (might work with lower pythons, ymmv)
* pipenv

1. clone the repo

2. install pythond deps
```bash
pipenv install
```

3. download nltk data, edit `NLTK_DATA` var in .env to configure path
```
pipenv run init_corpora
```

## Run tests
```
pipenv run test
```

## CLI
This ships with a cli module, easily accessible via pipenv:
```sh
➜ pipenv run cli -h
Loading .env environment variables…
usage: cli.py [-h] [-l] [-m {important_words} [{important_words} ...]] [-c COUNT] [-d] file

positional arguments:
  file                  the file to analyze

optional arguments:
  -h, --help            show this help message and exit
  -l, --local           look for the file in comprende/tests/data
  -m {important_words} [{important_words} ...], --modules {important_words} [{important_words} ...]
                        specify which question modules to run for this file
  -c COUNT, --count COUNT
                        specify how many questions to generate
  -d, --debug           enable additional debug output
```

example usage:
```sh
➜ pipenv run cli proprietary/nyt/one_district -dl -c2 | jq
Loading .env environment variables…
[
  {
    "prompt": "Which of these key phrases was mentioned in this document?",
    "correct_options": [
      "high-needs students"
    ],
    "module_name": "important_words",
    "additional_option": [],
    "subtype": "least",
    "debug": {
      "freq": 1
    }
  },
  {
    "prompt": "Which of these key phrases was mentioned often in this document?",
    "correct_options": [
      "mr. miyashiro"
    ],
    "module_name": "important_words",
    "additional_option": [],
    "subtype": "most",
    "debug": {
      "freq": 10
    }
  }
]
```
