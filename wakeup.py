import requests
import filecmp
import os
import time
import datetime

'''
curl 
-A "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36" 
-e http://geocachewakeup.byethost7.com/?ckattempt=1 
-b "__test=a7f64c693f5755629af2d2c71aa06d2a;referrer=" 
-o wakeup%TS%.png 
-H "Cache-Control: no-cache" 
http://geocachewakeup.byethost7.com/image.php
'''
headers = {'referer': 'http://geocachewakeup.byethost7.com/?ckattempt=1',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
           'pragma': 'no-cache',
           'cache-control': 'no-cache'}

cookies = {'__test': 'a7f64c693f5755629af2d2c71aa06d2a', 'referrer': ''}

i = 1

while True:
    print('Trial {0}'.format(i))
    res = requests.get('http://geocachewakeup.byethost7.com/image.php', cookies=cookies, headers=headers)
    res.raise_for_status()
    imagefile = open('uil.png', 'wb')
    for chunk in res.iter_content(1000):
        imagefile.write(chunk)
    imagefile.close()
    if not filecmp.cmp('howlsleep.png', 'uil.png', shallow=False):
        os.rename('uil.png', 'uil_{:%Y%m%d_%H%M%S}.png'.format(datetime.datetime.now()))

    filecmp.clear_cache()
    i += 1
    time.sleep(15)



