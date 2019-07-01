import urllib,urllib2

url = 'https://www.baidu.com/s?wd=python'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
request = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(request)
print(response.read())



