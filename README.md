# ZaifBot
:chart_with_upwards_trend: trading bot for zaif exchange

[![Python version](https://img.shields.io/badge/python-3.4%2C%203.5%2C%203.6-blue.svg)]([zaifpypi])
[![PyPI version](https://badge.fury.io/py/zaifbot.svg)](https://badge.fury.io/py/zaifbot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


ZaifBot is a Pythonic algorithmic trading library running within [Zaif Exchange]([zaifen]).  
It is developed using Python 3.5.3 and tested in Python 3.4, 3.5, 3.6.

## Features

* Easy to use: Zaifbot is library for trading beginners, so designed simple.
* Support all currency pairs dealt with  [Zaif Exchange]([zaifen])
* Technical indicators like SMA, EMA, Bollinger Bands, RSI, ADX
* You don't have to prepare market data. Zaifbot internal get data from [zaif API]([zaifapi])

To get started with Zaifbot take a look at the [tutorial](notyet) and the [full documentation](notyet).  
[日本語ドキュメントはこちら](notyet)

**Note:** ZaifBot is unofficial library of [Tech Bureau, Inc.](http://techbureau.jp/) Please use it at your own risk.  

## Installation

### instaling with pip

After activating an isolated Python environment,

```bash
$ pip install zaifbot
```

currently supported platforms includes:

* Linux 64-bits
* OSX 64-bits
* Windows 64-bits

**Note:** if you use **OSX**, we assume [homebrew](https://brew.sh/index.html) is installed.

## Setup

After installing Zaifbot, run

```bash
$ init_database
```

===

When `init_database` command is run,  
`db/zaifbot.db` is created for SQLite and schema is migrated.  
Your Trade records will be saved in this file.


## Quick Start

See our [getting started tutorial](https://techbureau.github.io/zaifbot)

the following code implements a simple trading algorithm using zaifbot

```pyhon
some code
```

## Feedback

if you have a question, or find a bug, feel free to open an issue.

## Contributing
Any kind of contributions are welcome.
See the file [CONTRIBUTING.md](https://github.com/techbureau/zaifbot/blob/master/CONTRIBUTING.md)


[zaifen]: https://zaif.jp/?lang=en  
[zaifapi]: http://techbureau-api-document.readthedocs.io/ja/latest/index.html
[zaifpypi]: https://pypi.python.org/pypi/zaifbot