# Football SOS

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Flake8 Status](./reports/flake8/badge.svg)](./reports/flake8/index.html)
[![Coverage Status](./reports/coverage/badge.svg)](./reports/coverage/badge.svg)
[![pre-commit enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylekap/Football_SRS.svg)](https://github.com/kylekap/Football_SRS/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylekap/Football_SRS.svg)](https://github.com/kylekap/Football_SRS/pulls)
[![Python](https://img.shields.io/pypi/pyversions/cookiecutter-hypermodern-python-instance)](https://www.python.org/downloads/release/python-3100/)

## About
Generates:
- Strength of Schedule (SOS)
- Strength of Victory (SOV)
- Simple Rating System (SRS)
- Pythagorean Expectation (Expected win %)
- Comparative Performance Index (CPI)
- Rating Percentage Index (RPI)
- Square Gear rating


Can be used for NFL & NCAA teams in a given season


## Contents
- [Project](#football-sos)
  - [About](#about)
  - [Contents](#contents)


## Future Plans
- Add ELO
- Add BRR
- Add Colley Matrix Method
- Add MJS

Possible to add additional sports to this as well? But would need more research into effective ways of getting those scores, and would be expansion of the scope of the project.
NCAAM / NCAAW
NBA / WNBA

## Caveats
Non FBS team games are ignored in NCAAF, which will slightly alter vs "true" versions of those algorithms.  