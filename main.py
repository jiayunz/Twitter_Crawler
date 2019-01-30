# coding: utf-8
from crawler import Crawler
import json
from datetime import datetime
import sys

def get_screen_names(rpath):
    twitter_ids = []
    with open(rpath, 'r') as rf:
        for line in rf.readlines():
            twitter_ids.append(line.strip())
    return twitter_ids

def main(token_id, screen_name_path, wpath):
    start_time = datetime.now()
    print 'Started at:', start_time
    crawler = Crawler(token_id=token_id)
    screen_names = get_screen_names(screen_name_path)
    count = 0
    with open(wpath, 'a') as wf:
        for sn in screen_names:
            try:
                user = crawler.get_user(sn)
                wf.write(json.dumps(user) + '\n')
                count += 1
                print count, 'users got.'
            #except tweepy.RateLimitError:
            #    print 'Exceeds rate limit, waiting...'
            #    time.sleep(120)
            except KeyboardInterrupt:
                end_time = datetime.now()
                print 'Ended at:', end_time
                print 'Duration:', (end_time - start_time).total_seconds() / 3600., 'hours'
                exit()
            except Exception, ex:
                print ex

if __name__ == '__main__':
    #main(token_id=int(sys.argv[1]), screen_name_path=int(sys.argv[2]), wpath=int(sys.argv[3]))
    main(token_id=1, screen_name_path='twitter_id.txt', wpath='test.json')