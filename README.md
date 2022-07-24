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

## Current Leagues
- Baseball
  - MLB

- Basketball
  - NBA
  - WNBA
  - NCAAM

- Football
  - NFL
  - NCAAF

- Hockey
  - NHL

## Future Plans
- Rating Systems
  - Add ELO
  - Add BRR
  - Add Colley Matrix Method
  - Add MJS

- Leagues
  - NCAAW
  - MLS
  - NWSL


MLS, NCAAW, NWSL appear to be out of the ordinary for the other systems of scores. Additional resarch needed to find better layouts

Dealing with "eras", or team movements, by league.

## Caveats
Non FBS team games are ignored in NCAAF, which will slightly alter vs "true" versions of those algorithms.
Some teams have moved cities. If a time period before the current location is used, the team is dropped from calculations.