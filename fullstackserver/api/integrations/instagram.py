# use public available rss feeds

import requests
import xml.etree.ElementTree as ET
import re
import dateparser
try:
    from .utils import *
except SystemError:
    from utils import *


class InstagramFeed:

    name = 'aviaryan123'

    def __init__(self, name):
        self.name = name

    def getFeeds(self):
        return self.getUnofficialFeeds()

    def getUnofficialFeeds(self):
        url = 'http://iconosquare.com/feed/' + self.name
        r = requests.get(url)
        tree = ET.fromstring(r.content.decode(encoding='utf-8'))
        root = tree
        #tree = ET.parse('instagram.xml')
        #root = tree.getroot()
        ret = []
        for item in root.iter('item'):
            text = item.find('title').text
            time = timeToStr(item.find('pubDate').text)
            url = item.find('link').text
            imageUrl = item.find('description').text
            images = re.findall(r'https:\/\/.*cdninsta.*?(?=\')', imageUrl)
            imageUrl = images[0]
            ret.append({
                'text': text,
                'time': time,
                'imageUrl': imageUrl,
                'url': url
            })
        return ret

if __name__ == '__main__':
    x = InstagramFeed('aviaryan123')
    x.getFeeds()