import requests

url = "https://imgs.xkcd.com/s/a899e84.jpg"

r = requests.get(url)
with open('comic.png', mode='wb') as mf:
    mf.write(r.content)