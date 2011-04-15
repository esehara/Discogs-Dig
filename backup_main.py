import cgi
import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import webapp

import re,urllib
from BeautifulSoup import BeautifulSoup

from xml.etree.ElementTree import ElementTree
from urllib import urlopen

testdata = 'http://www.discogs.com/label/Planet+mu?f=xml&api_key=d53806d9a9'

class MainPage(webapp.RequestHandler):
    def __init__():
        self.artists = xmlperse.dataopen(testdata)
        #self.ytb = youtube_content_search
        
    def get(self):
        self.response.out.write("""
        <html>
            <body>
            """)
        for artist in self.artists:
            self.response.out.write("<p>%s</p>" % arist)
        self.response.out.write("""
                <form action="/url" method="post">
                    <div><textarea name="url" rows="3" cols="60"></textarea></div>
                    <div><input type="submit" value="Get"></div>
                </form>
            </body>
        </html>""")
    
class persexml:
    def __init__(self):
        self.artists = []

    def dataopen(self,url):
        perser=ElementTree(file=urlopen(url))
        element=perser.findall("//artist")
        for elem in element:
            check_artist = False        
            for check in self.artists:
                if check == elem.text:
                    check_artist = True
            if not check_artist:
                self.artists.append(elem.text)
        return self.artists
        
class youtube_content_search:
    def __init__(self):
        #self.youtube_service = gdata.youtube.service.YouTubeServce()
        #self.youtube_service.ssl = False
        self.result_list = []

    def search_video(self,query):
        youtube_query = re.sub(" ","+",query)
        url="http://gdata.youtube.com/feeds/api/videos?q="+youtube_query
        soup = BeautifulSoup(urllib.urlopen(url).read())
        video_id = re.split("/",soup.findAll('id')[1].string)[-1]
        video_title = soup.findAll('title')[1].string
        video_tag = """<iframe title="YouTube video player" width="240" height="145" src="http://www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>""" % video_id
        return video_tag

application = webapp.WSGIApplication(
    [('/',MainPage)]
    ,debug=True)
        
def main():
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
