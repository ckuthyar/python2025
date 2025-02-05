import urllib.request
response=urllib.request.urlopen("https://www.bbc.com/news")
info1=response.read().decode("utf-8")
print(info1[0:500])



