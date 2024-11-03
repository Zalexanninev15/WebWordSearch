# WebWordSearch

[![](https://img.shields.io/badge/written_on-Python-%233776AB.svg?logo=python)](https://github.com/Zalexanninev15/WebWordSearch)
[![](https://img.shields.io/badge/release-v1.0.2-blue.svg)](https://github.com/Zalexanninev15/WebWordSearch)
[![](https://img.shields.io/github/last-commit/Zalexanninev15/WebWordSearch.svg)](https://github.com/Zalexanninev15/WebWordSearch/commits/main)
[![](https://img.shields.io/github/stars/Zalexanninev15/WebWordSearch.svg)](https://github.com/Zalexanninev15/WebWordSearch/stargazers)
[![](https://img.shields.io/github/forks/Zalexanninev15/WebWordSearch.svg)](https://github.com/Zalexanninev15/WebWordSearch/network/members)
[![](https://img.shields.io/github/issues/Zalexanninev15/WebWordSearch.svg)](https://github.com/Zalexanninev15/WebWordSearch/issues?q=is%3Aopen+is%3Aissue)
[![](https://img.shields.io/github/issues-closed/Zalexanninev15/WebWordSearch.svg)](https://github.com/Zalexanninev15/WebWordSearch/issues?q=is%3Aissue+is%3Aclosed)
[![](https://img.shields.io/badge/license-GPLv3-ligthgreen.svg)](LICENSE)
[![](https://img.shields.io/badge/Donate-FFDD00.svg?logo=buymeacoffee&logoColor=black)](https://z15.neocities.org/donate)

## Description

Script for searching for a word or symbol on the sites specified in the text file. Outputs the number of matches on each page to the console, and also displays the total number of matches at the end of the search.

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