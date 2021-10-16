#!C:/Users/Rithikshan/Documents/python

# Import modules for CGI handling 
# Import modules for CGI handling 
import cgi, cgitb 
import random
import json
import requests
import os
import hashlib
from datetime import datetime
import hmac
import binascii
import sys
import urllib.request
import urllib
from requests_html import HTMLSession
from urllib.parse import urljoin
from urllib.request import urlopen
import bz2
from requests.exceptions import HTTPError
from json.decoder import JSONDecoder 
from json.encoder import JSONEncoder 
import webbrowser
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
Name = form.getvalue('Name')
AMOUNT  = form.getvalue('AMOUNT')
Mobile = form.getvalue('Mobile')
EMail  = form.getvalue('EMail')
Address  = form.getvalue('Address')
userReference=form.getvalue('userReference')

bala={'MerchantCode':'IN3809','authKey':'NTTZfpzWys22tZSY','currency':'INR','pc':'All','tunnel':'','amount':4,'doConvert':'','sourceCurrency':'','description':'','referenceID':4,
    'timeStamp':'12','language':'en','callbackURL':'https://hooghlypay.com/portal/Dashboard/CheckOutReturn','userReference':123456789,
    'hash':'290F1E86C85B9BEFE8A2CF73FC2E00D2355ED735D1E46EF29CE07515072E62BD','cid':'','billingDetails':{'fName':'Bala','lName':'','mobile':7338912115,
    'email':'kprbalamurugan@gmail.com','city':'chennai','pincode':'','state':'','address1':'trichy','address2':'',},'vendorDetails':[{'payoutReferenceID':0,'payoutAmount':0,'payoutName':'','payoutBankAccount':'','payoutIFSCcode':'','payoutPurpose':'','payoutEmail':'','payoutPhone':''}]}
# Create your views here.

format = '%Y/%m/%d %I:%M:%S %p'
bala['timeStamp']=datetime.today().strftime(format)
bala['referenceID']=random.randint(100000000000000,999999999999999)
bala['amount'] = AMOUNT
bala['userReference']=userReference
bala['billingDetails']['fName']=Name
#bala['fName']='bala'
bala['billingDetails']['mobile']= Mobile
bala['billingDetails']['email']=EMail
bala['billingDetails']['address1']=Address
hk='$'
bi=str(bala['amount'])
bi2='NTTZfpzWys22tZSY'
bi3='INR'
bi4='IN3809'
bi5='All'
bi6=str(bala['referenceID'])
bi7={}
bi8=str(bala['timeStamp'])
bi9=str(bala['userReference'])
secretKey = "hHqpXCwtF4EOB9KQ"
hk1=hk+bi+bi2+bi3+bi4+bi5+bi6+bi8+bi9+';'
key='hHqpXCwtF4EOB9KQ'
my =hk1 
byte_key = bytes(key, 'UTF-8')  # key.encode() would also work in this case
message = my.encode()
h = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
bala['hash']=h

headers={'Content-type':'application/json','Accept':'application/json'}

#serializer = SnippetSerializer(bala
payload = json.dumps(bala,indent = 2) 

API_ENDPOINT="https://hooghlypay.com/API/api/GenToken/Validate"
r = requests.post(url = API_ENDPOINT, data = payload,headers=headers)
s=r.json() 
si=s['result']['redirectURL']

webbrowser.open(si,new=0)
#webbrowser.open_new_tab(si)
#urllib.request.urlopen(si)

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Welocome to the payment Page</title>")
print ("</head>")
print ("<body>")
print ("</body>")
print ("</html>")