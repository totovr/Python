# To create a distro of a package in Python

Create a file called setup.py, this script must be in the main path of the folder that we are working: 

```python
from setuptools import setup

setup(
    name="package",
    version="0.1",
    description="This is an example of a package",
    author="Antonio Vega",
    author_email="a.vegaramirez76@gmail.com",
    url="https://totovr.github.io/",
    scripts=[],
    package=["package", "package.bye", "package.hello"]
)

```

Then open terminal and run:

```terminal
python setup.py sdist
```

This will generate a folder called ***dist***, in terminal change to this folder:

```terminal
cd dist
```

Then install the package that we generate with 

```terminal
pip3 install "name-of-the-package"
```

We can check if our package is installed with:

```terminal
pip3 list
```

/anaconda3/bin/pip