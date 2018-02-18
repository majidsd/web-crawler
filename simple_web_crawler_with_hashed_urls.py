import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import hashlib
import re
import os
import sys


def crawl(seeds, limit=10):
  frontier = seeds
  visited_urls = set()

  p = re.compile('.*.harding.edu')
  
  if not os.path.exists('pages'):
    os.makedirs('pages')  

  for crawl_url in frontier:
    if limit == 0 : break
    if(p.match(crawl_url)):
      print("Crawling : ", crawl_url)
      fileName = 'pages/' + hashlib.md5(crawl_url.encode()).hexdigest() + '.html'
      makedFile = open(fileName, 'w+')
      makedFile.close()
      visited_urls.add(crawl_url)
      limit = limit - 1
    else:
      print("Can not crawl this %s URl"%crawl_url)
      
  
    try:
      resp = urllib.request.urlopen(crawl_url)
    except:
      print("Cloud not access : ", crawl_url)
      continue

    content_type = resp.info().get('Content-Type')
    if not content_type.startswith('text/html'):
      print("Skipping %s content" % content_type)
      continue

    contents = str(resp.read(), encoding='utf8')
    soup = BeautifulSoup(contents)


    discovered_urls = set()
    links = soup('a')
    for link in links:
      if('href' in dict(link.attrs)):
        url = urljoin(crawl_url, link['href'])
        if(url[0:4] == 'http' and url not in visited_urls and url not in discovered_urls and url not in frontier):
          discovered_urls.add(url)

    frontier += discovered_urls
    time.sleep(2)


myUrls = ['https://www.harding.edu']

args = len(sys.argv)
try:
  val = int(sys.argv[1])
  crawl(myUrls, val)
  
except:
  print ("Ooooops! The Limit must be integer number, so we will use the default as 10")
  crawl(myUrls)
