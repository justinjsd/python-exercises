import urllib.request

my_request = urllib.request.urlopen("https://helsinki.fi")
print(my_request.read())