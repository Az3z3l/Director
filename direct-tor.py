import requests as reqs
from requests_html import HTMLSession
import re
import os
session=HTMLSession()
i=0
f = open("directories.txt", "w+")

u=input('Enter The Url:')
req = session.get(u)
'''
s=req.text
s=s.split()
p=['script','https:','span','class','<','{','}','(',')','type','<','http','href','<script>' ]
for i in s:
	if '/' in i:
		if i not in p:
			print(i)
	'''
http="http:"
print("\n------------------------------ IN-PAGE LINKS ---------------------------")
links=[]
links=req.html.links
for i in links:
	f.write(i+'\n')
f.close() 
f = open("directories.txt", "r")
fl =f.readlines()
for i in fl:
	print(i)

print("\n------------------------------ ROBOTS ---------------------------")
req = session.get(u+'robots.txt')
s=req.text
print(s)
