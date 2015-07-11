# coding=utf-8
import sys
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-EN,en;q=0.8,ru;q=0.6,de;q=0.4',
    'Accept-Encoding': 'gzip,deflate,sdch',
}

urls = open('urls.txt', 'r').read().splitlines()

if len(sys.argv) != 2:
    print('Usage: python search.py "keywords to search"')
    exit()

f = open('results/' + sys.argv[1], 'w')
f.close()

for url in urls:
    t_url = url.replace('http://', '')
    try:
        response = requests.get('http://' + t_url, headers=headers)
        if response.text.find(sys.argv[1]) >= 0:
            f = open('results/' + sys.argv[1], 'a')
            f.write(url + ';yes\n')
            f.close()
            print(url + ';yes')
        else:
            f = open('results/' + sys.argv[1], 'a')
            f.write(url + ';no\n')
            f.close()
            print(url + ';no')
    except requests.RequestException:
        f = open('results/' + sys.argv[1], 'a')
        f.write(url + ';error\n')
        f.close()
        print(url + ';error')
