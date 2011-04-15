import cgi
import wsgiref.handlers
import xmlperse
import youtube_search

from google.appengine.api import users
from google.appengine.ext import webapp

import re,urllib
from BeautifulSoup import BeautifulSoup

from xml.etree.ElementTree import ElementTree
from urllib import urlopen

#testdata = 'http://www.discogs.com/label/Planet+mu?f=xml&api_key=d53806d9a9'
    
class MainPage(webapp.RequestHandler):
    def get(self):
        
        response = cgi.escape(self.request.get('label'))

        if response == '':
            response = "planet mu"
        
        response = re.sub(" ","+",response)

        persexml = xmlperse.persexml()
        youtube = youtube_search.youtube_content_search()

        url='http://www.discogs.com/label/'+response+'?f=xml&api_key=d53806d9a9'
        self.artists = persexml.dataopen(url)

        self.response.out.write(u"""
        <html>
            <body>
            <p><a href="http://www.discogs.com/">Discogs</a> Label Search (ex."Planet Mu")</a>
                <form action="./" method="get">
                    <div><input type="text" name="label"></div>
                    <div><input type="submit" value="Get"></div>
                </form>
             """)
        a = 0
        for artist in self.artists:
            a += 1
            self.response.out.write("<p>%s</p>" % artist)
            self.response.out.write("<p>%s</p>" % youtube.search_video(artist))
            if a > 25:
                break

        self.response.out.write("""
           </body>
        </html>""")

application = webapp.WSGIApplication(
    [('/',MainPage)]
    ,debug=True)
                
def main():
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
