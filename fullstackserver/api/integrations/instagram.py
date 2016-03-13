# use public available rss feeds

import requests
import xml.etree.ElementTree as ET
import re

try:
    from .utils import *
    from .googlesearch import *
except SystemError:
    from utils import *
    from googlesearch import *


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
        count = 0
        for item in root.iter('item'):
            text = item.find('title').text
            time = timeToStr(item.find('pubDate').text)
            url = item.find('link').text
            imageUrl = item.find('description').text
            images = re.findall(r'https:\/\/.*cdninsta.*?(?=\')', imageUrl)
            imageUrl = images[0]
            ret.append({
                'content': text,
                'time': time,
                'imageurl': imageUrl,
                'url': url
            })
            count += 1
            if count > 10:
                break
        return ret

def getLinks(searchterm):
    links = googleSearchLinks('site:instagram.com ' + searchterm + ' - instagram', r'http.*?\/\/[^\/]*?instagram\.com\/[^\/]+\/?$')
    return links

def getNames(links):
    names = []
    for i in links:
        names.append(getName(i))
    return names

def getName(link):
    name = re.sub(r'.*instagram.com\/', '', link)
    name = name.replace('/', '')
    return name

if __name__ == '__main__':
    # x = InstagramFeed('aviaryan123')
    # x.getFeeds()
    links = getLinks('Modern Life')
    names = getNames(links)
    print(names)