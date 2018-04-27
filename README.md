# Bojangles

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

## Secrets management

Secrets will be managed through git-crypt.
