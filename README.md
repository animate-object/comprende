# ¿Comprende?
What if you had to read an article before you commented on it?
Generating efficient reading recall tests and basic understanding (topics, authorship, etc).


## Installation

### Pre-reqs
* > python 3.8 (might work with lower pythons, ymmv)
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
