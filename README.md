# WebWordSearch

[![](https://img.shields.io/badge/platforms-All_with_Python-orange.svg)](https://github.com/Zalexanninev15/WebWordSearch)
[![](https://img.shields.io/badge/release-v1.0-blue.svg)](https://github.com/Zalexanninev15/WebWordSearch)
[![](https://img.shields.io/github/last-commit/Zalexanninev15/WebWordSearch.svg)](https://github.com/Zalexanninev15/WebWordSearch/commits/master)
[![](https://img.shields.io/badge/license-GPLv3-ligthgreen.svg)](LICENSE)
[![](https://img.shields.io/badge/donate-QIWI-FF8C00.svg)](https://qiwi.com/n/ZALEXANNINEV15)
[![](https://img.shields.io/badge/donate-YooMoney-8B3FFD.svg)](https://yoomoney.ru/to/410015106319420)

## Description

A Python script for searching for a word or symbol on the sites specified in the text file. Outputs the number of matches on each page to the console, and also displays the total number of matches at the end of the search

## Usage

1. Insert links to search sites to file **urls.txt**
2. Do the following in terminal
```bash
pip install -r requirements.txt
python ./wws.py
```

## Used libraries

* [requests](https://pypi.org/project/requests) ([Apache-2.0 License](https://github.com/psf/requests/blob/master/LICENSE))
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup) ([MIT License](https://www.crummy.com/software/BeautifulSoup))
