import re,urllib
from BeautifulSoup import BeautifulSoup

class youtube_content_search:
    def __init__(self):
        #self.youtube_service = gdata.youtube.service.YouTubeServce()
        #self.youtube_service.ssl = False
        self.result_list = []

    def search_video(self,query):
        youtube_query = re.sub(" ","+",query)
        url="http://gdata.youtube.com/feeds/api/videos?q="+youtube_query
        try:
            soup = BeautifulSoup(urllib.urlopen(url).read())
            video_id = re.split("/",soup.findAll('id')[1].string)[-1]
            video_title = soup.findAll('title')[1].string
            video_tag = """<iframe title="YouTube video player" width="240" height="145" src="http://www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>""" % video_id
            return video_tag
        except:
            return ''
