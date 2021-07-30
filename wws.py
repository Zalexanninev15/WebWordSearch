# A Python script for searching for a word or symbol on the sites specified in the text file
# Copyright (C) 2021 Zalexanninev15

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import requests
from bs4 import BeautifulSoup

print('''WebWordSearch  Copyright (C) 2021  Zalexanninev15
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
''')
with open("urls.txt") as file:
    url_list = [row.strip() for row in file]
the_word = input('WebWordSearch v1.0.1 by Zalexanninev15\nWord for search: ')
total_words = []
for url in url_list:
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.content.lower(), 'html.parser')
    words = soup.find_all(text=lambda text: text and the_word.lower() in text)
    count = len(words)
    words_list = [ ele.strip() for ele in words ]
    for word in words:
        total_words.append(word.strip())
    print('\nURL: {}\nMatches: {}'.format(url, count))
    print('\nTotal matches: {}'.format(len(total_words)))