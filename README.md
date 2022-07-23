# Sports Ranking Systems

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Flake8 Status](./reports/flake8/badge.svg)](./reports/flake8/index.html)
[![Coverage Status](./reports/coverage/badge.svg)](./reports/coverage/badge.svg)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

[![pre-commit enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Travis CI Build Status](https://travis-ci.com/kylekap/Sports_Ranking_Systems.svg?branch=main)](https://travis-ci.com/kylekap/Sports_Ranking_Systems)

[![GitHub Issues](https://img.shields.io/github/issues/kylekap/Sports_Ranking_Systems.svg)](https://github.com/kylekap/Sports_Ranking_Systems/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylekap/Sports_Ranking_Systems.svg)](https://github.com/kylekap/Sports_Ranking_Systems/pulls)


## About
Generates:
- Strength of Schedule (SOS)
- Strength of Schedule (BCS version)
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
  - [Future Plans](#future-plans)
  - [Caveats](#caveats)  


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