import urllib.request
class AccessUrl:
    def getUrlContent(self,url):
        webUrl = urllib.request.urlopen(url)
        print("Result code: " + str(webUrl.getcode()))
        data = webUrl.read()
        print(data)


url = input("Enter The Url To Access Content : ")
getUrl = AccessUrl()
getUrl.getUrlContent(url)
