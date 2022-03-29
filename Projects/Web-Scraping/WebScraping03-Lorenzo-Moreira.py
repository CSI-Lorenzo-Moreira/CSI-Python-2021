import requests
import bs4
res = requests.get("https://www.sanignacio.pr/sobre-csi/historia-del-colegio")
res.raise_for_status()
sanignaciopr = bs4.BeautifulSoup(res.text, 'html.parser')
elems = sanignaciopr.select('p')
print(elems[2].getText() + elems[3].getText())