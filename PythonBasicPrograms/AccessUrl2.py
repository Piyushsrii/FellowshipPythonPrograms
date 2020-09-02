from http.client import HTTPConnection
class AccessUrl2:
    def getUrlContent(self, url):
        conn = HTTPConnection(url)
        conn.request("GET", "/")
        resOfUrl = conn.getresponse()
        contents = resOfUrl.read()
        print("Content : ", contents)

url = input("Enter The Url To Access Content : ")
getUrl = AccessUrl2()
getUrl.getUrlContent(url)

