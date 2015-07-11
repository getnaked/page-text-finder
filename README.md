# page-text-finder
Find words on webpages and mark URL's

Add URL's in urls.txt:
http://www.mvideo.ru/
http://www.eldorado.ru/
http://euroset.ru/
http://yandex.ru/
http://mvahahahahaha.ru

Run script:
python search.py "Asus Nexus"

Result:
http://www.mvideo.ru/;no
http://www.eldorado.ru/;no
http://euroset.ru/;yes
http://yandex.ru/;no
http://mvahahahahaha.ru;error
