import urllib.request as urllib2

URL = "https://stbank.by/private_client/currency_exchange_operations/"


def getHtml():
    req = urllib2.Request(URL)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')
    response = urllib2.urlopen(req)
    content = response.read()
    return content