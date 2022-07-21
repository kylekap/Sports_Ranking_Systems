# Overview of useful python resources & common commands.

## Resources
- [PEP-8](https://realpython.com/python-pep8/)
- [Writing Structure](https://docs.python-guide.org/writing/structure/)
- [Google's Python Writing Guide](https://google.github.io/styleguide/pyguide.htm)


## Common Commands
To create virtual environment:
>   py -m venv env

To activate
>   env\Scripts\activate

To install
>   py -m pip install .
>   py -m pip install .[dev]

Advanced flake8
>   flake8 src --exit-zero --format=html --htmldir reports/flake8 --statistics --tee --output-file reports/flake8/flake8stats.txt

Coverage
>   py -m coverage run -m pytest
>   coverage xml -o reports/coverage/coverage.xml

For genbadge (must do both those modules (ie flake8/coverage) commands first)
>   genbadge flake8 --output-file ./reports/flake8/badge.svg
>   genbadge coverage --output-file ./reports/coverage/badge.svg  


Pre-commit setup
>   pre-commit install

>   pre-commit run --all-files

>   pre-commit autoupdate
