import requests
res = requests.get("https://gutenberg.org/cache/epub/42985/pg42985.txt")
res.raise_for_status()
playfile = open("Social Problems in Porto Rico", "wb")
for chunk in res.iter_content(100000):
    playfile.write(chunk)
playfile.close()