#! python3
# lucky.py - Opens several Google search results.
# call with "lucky.py #searchword#"

import requests, sys, webbrowser, bs4, re

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
#res = requests.get('http://google.com/search?q=test123')
res.raise_for_status()


# TODO: Retrieve top search result links.

#soup = bs4.BeautifulSoup(res.text, "lxml")
soup = bs4.BeautifulSoup(res.text)

#print(soup)

# TODO: Open a browser tab for each result.
#linkElems = soup.select('.r a')
linkElems = soup.select('div#main > div > div > div > a')
#linkElems = soup.select('.a', attrs={'href': re.compile("^http://")})
#print(linkElems)


numOpen = min(5, len(linkElems))
#print(numOpen)
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    