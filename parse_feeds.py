import feedparser
import time
import json
import sys
from url_list import url_list

import pdb

def feedelemextract(feed_obj):

    elems = {'title':feed_obj.title,
             'description':feed_obj.description,
             'publish_dt':feed_obj.published,
             'link':feed_obj.link,
            }

    return elems


def feed_gen(json_file_output):
    feed_hold = {}
    now = time.gmtime()
    for url in url_list:
        d = feedparser.parse(url)
    
        print url
        
        feed_hold[d.feed.title]=[]
        for entry in d.entries[0:5]:
            dt = entry['published_parsed']  
    
            if time.mktime(now) - time.mktime(dt) < 3*24*3600.0:
                feed_hold[d.feed.title].append(feedelemextract(entry))
    
    with open(json_file_output, 'w') as fout:
        json.dump(feed_hold, fout)
    

if __name__ == "__main__":
    json_output = 'fr4nkfeed.json'
    feed_gen(json_output)
