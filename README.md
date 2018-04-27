# Bojangles

## Getting your environment setup

We will be using Docker eventually to automate this process, and to reduce environment inconsistencies, but to get this setup properly on an external system:

Note: this assumes virtualenv has been enabled, and python3.6 (preferably) is available.

```shell
virtualenv env --python=`which python3`
. env/bin/activate

pip install -r requirements.txt
pip install -e .

python run.py
```
