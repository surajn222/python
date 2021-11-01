#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()
config.read('db.ini')

#Method 1
host = config['mysql']['host']
user = config['mysql']['user']
passwd = config['mysql']['passwd']
db = config['mysql']['db']

host2 = config['postgresql']['host']
user2 = config['postgresql']['user']
passwd2 = config['postgresql']['passwd']
db2 = config['postgresql']['db']

#Method 2
parser = configparser.ConfigParser()
parser.read('db.ini')
for sect in parser.sections():
   print('Section:', sect)
   for k,v in parser.items(sect):
      print(' {} = {}'.format(k,v))
   print()

#Method 3
config = configparser.ConfigParser()
config.read("db.ini")
username = config.get('mysql', 'user')
hostname = config.get('mysql', 'host')
print(username)

#To write a config file
import configparser
parser = configparser.ConfigParser()
parser.add_section('Manager')
parser.set('Manager', 'Name', 'Ashok Kulkarni')
parser.set('Manager', 'email', 'ashok@gmail.com')
parser.set('Manager', 'password', 'secret')
fp=open('test.ini','w')
parser.write(fp)
fp.close()