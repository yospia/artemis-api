"""Script para instalar o projeto no ambiente local

Nao requer instalacao de dependencias

Uso:
```bash
pip install -e .
```
"""


from setuptools import setup, find_packages

setup(
    name='artemis_api',
    version='1.0.0',
    packages=find_packages()
)