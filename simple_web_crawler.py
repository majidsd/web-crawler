import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import hashlib
import re
import os
import sys


def crawl(seeds):
  frontier = seeds
  visited_urls = set()

  for crawl_url in frontier:
    print("Crawling : ", crawl_url)
    visited_urls.add(crawl_url)
  
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
crawl(myUrls)
