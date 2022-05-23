import sys
from unittest import mock

#MagicMock
m = mock.Mock()
#m['any_key_you_want']
#This won't work

m = mock.Mock()
#for x in m:
#    print(m)
#This won't work either


requests = mock.MagicMock()
print(requests.unwanted_method())
#This will work



#Now, the way mock works, is that once you create a mock object(which is the duplicate function), it can call any function, even fake functions (the one that are not in the original function)
#To avoid this, we use spec in MagicMock
import requests
mock_requests = mock.MagicMock(spec=requests)
print(mock_requests.unwanted_method())
#This will fail, because get is not a function of the requests module.
print(mock_requests.get("abcd"))
#This will work, because get is a function of requests module
