import urllib.request
response = urllib.request.urlopen("https://www.codingdojo.com")
html = response.read()
# print(html)
print(dir(urllib.request))