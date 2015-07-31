from StringIO import StringIO
import gzip
import urllib2
import urllib

url="http://api.syosetu.com/novelapi/api/"

get={}
get["gzip"]=5
get["out"]="json"
get["of"]="t-s-w"
get["lim"]=500
get["type"]="er"

url_values = urllib.urlencode(get)

request = urllib2.Request(url+"?"+url_values)
response = urllib2.urlopen(request)

if response.info().get('Content-Type') == 'application/x-gzip':
    buf = StringIO( response.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
else:
    data = response.read()


f = open('text.txt', 'w')
f.write(data)
f.close()

print(data)