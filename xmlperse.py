from xml.etree.ElementTree import ElementTree
import urllib
import urllib2

class persexml:
    def __init__(self):
        self.artists = []

    def dataopen(self,url):

        headers = {'Accept-Encoding': 'gzip', 'User-Agent': 'MyDiscogsClient/1.0 +http://mydiscogsclient.org'}
        request = urllib2.Request(url, None, headers)
        u = urllib2.urlopen(request)
        perser=ElementTree(file=u)
        element=perser.findall(".//artist")

        for elem in element:
            check_artist = False        
            for check in self.artists:
                if check == elem.text:
                    check_artist = True
            if not check_artist:
                self.artists.append(elem.text)
        return self.artists
