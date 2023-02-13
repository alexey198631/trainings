"""
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Bailley.html
Find the link at position 18 (the first name is 1). Follow that link.
Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: I
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/known_by_Bailley.html'
count = 7
position = 18

while count > 0:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position - 1].get('href', None)
    count -= 1

print('The last name:', url.split('_')[-1].split('.')[0])