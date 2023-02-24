# Flask

### How to install flask

```bash
pip install Flask

```

### How to verify that flask was installed

```bash
pip freeze
```

### Save installed libraries in requirements.txt

```
pip freeze > requirements.txt
```

### How to install from requirements.txt

```bash
pip install -r requirements.txt
```



### How to Install a Virtual Environment using Venv

```bash
mkdir webapp
cd webapp

python -m venv venv

touch .gitignore
  env/
```

### How to Activate the Virtual Environment

```bash
source env/Scripts/activate # Windows

source env/bin/activate # Linux, Mac
```

**Note:** Since Python 3.3, a subset of it has been integrated into the standard library under the venv module.

### Some addicional commands

```bash
pip list
pip freeze > requirements.txt
pip install -r requirements.txt
```


### How to Deactivate a Virtual Environment

```bash
deactivate
```


**Addicional links:**
- https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/
- https://flask.palletsprojects.com/en/2.2.x/installation/