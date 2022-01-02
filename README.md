# Bojangles

NOTE - this project is now dead in favour of [Notangles](https://github.com/csesoc/notangles)

## Getting your environment setup

We will be using Docker eventually to automate this process, and to reduce environment inconsistencies, but to get this setup properly on an external system:

Note: this assumes virtualenv has been enabled, and python3.6 (preferably) is available.

```sh
pipenv python run.py
```

### Installing a dependency

```sh
pipenv install my-cool-dependency
```

### Entering the virtual environment

```sh
pipenv --shell
```
