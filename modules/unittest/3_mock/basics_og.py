#https://medium.com/@yasufumy/python-mock-basics-674c33de1ced

#Example 1
import sys

from unittest import mock

requests = mock.Mock()
requests.get.return_value.status_code = 200

r = requests.get('https://api.github.com/user',auth=('user', 'pass'))
print(r.status_code)

#Example 2
from unittest import mock

requests = mock.Mock()
r = requests.get('https://api.github.com/user',auth=('user', 'pass'))

m = mock.Mock()
m.can.access.any.attribute = 1

m = mock.Mock()
m.can.accespt.any.call('with', 'any', 'argument', [1, 2, 3])


#Example 3
m = mock.Mock(return_value=42)
print(m())

print("here")
m = mock.Mock()
m.return_value = 42
print(m())

sys.exit()



m = mock.Mock(return_value=42)
print(m.any.method())

requests = mock.Mock()
requests.get.return_value.status_code = 200
r = requests.get('https://api.github.com/user',auth=('user', 'pass'))
print(r.status_code)

requests.get.return_value.status_code = 200

r = requests.get('invalid_url')
print(r.status_code)

m = mock.Mock(side_effect=lambda x: x % 2 == 0)
print(m(42))
print(m(11))



def return_status_code(url, *args, **kwargs):
    code = 200 if url == 'https://api.github.com/user' else 404
    m = mock.Mock()
    m.status_code = code
    return m

requests = mock.Mock()
requests.get.side_effect = return_status_code
print(requests.get('https://api.github.com/user',auth=('user', 'pass')).status_code)
print(requests.get('invalid_url').status_code)


requests = mock.Mock()
r = requests.get('https://api.github.com/user',auth=('user', 'pass'))
requests.mock_calls
print(requests.mock_calls[0])

call_info = requests.mock_calls[0]
print(call_info[0])
print(call_info[1])
print(call_info[2])

requests = mock.Mock()
r = requests.get('https://api.github.com/user',auth=('user', 'pass'))
requests.get.assert_called_once_with(
        'https://api.github.com/user', auth=('user', 'pass'))


m = mock.Mock()
#m['any_key_you_want']


m = mock.Mock()
for x in m:
    print(m)











requests = mock.MagicMock()
print(requests.unwanted_method())



import requests
mock_requests = mock.MagicMock(spec=requests)
print(mock_requests.unwanted_method())



import requests
mock_requests = mock.MagicMock(spec=requests)
r = mock_requests.Session()
r.unwanted_method()



import requests
mock_requests = mock.create_autospec(spec=requests)
r = mock_requests.Session()
r.unwanted_method()

sys.exit()

import requests
with mock.patch('__main__.requests', autospec=True):
    requests.get('https://api.github.com/user',auth=('user', 'pass')
    #requests.get.assert_called_once_with('https://api.github.com/user', auto=('user', 'pass'))

with mock.patch('__main__.requests', autospec=True) as mock_requests:
    mock_requests.get('https://api.github.com/user',auth=('user', 'pass')
    #mock_requests.get.assert_called_once_with('https://api.github.com/user', auto=('user', 'pass'))
    #assert mock_requests == requests





@mock.patch('__main__.requests', autospec=True)
def test_requests_get(requests):
     requests.get('https://api.github.com/user',auth=('user', 'pass')
     requests.get.assert_called_once_with('https://api.github.com/user', auto=('user', 'pass'))
test_requests_get()





patcher = mock.patch('__main__.requests', autospec=True)
patcher.start()
requests.get('https://api.github.com/user',auth=('user', 'pass'))
requests.get.assert_called_once_with('https://api.github.com/user', auth=('user', 'pass'))
patcher.stop()




with mock.patch('requests.get', autospec=True) as mock_get:
    mock_get('https://api.github.com/user',auth=('user', 'pass'))
    mock_get.assert_called_once_with('https://api.github.com/user', auth=('user', 'pass'))



with mock.patch('pickle.dumps', autospec=True) as mock_dumps:
    mock_dumps('object_to_save')
    mock_dumps.assert_called_once_with('object_to_save')



import os
import requests
def download(url):
    r = requests.get(url)
    filename = os.path.basename(url)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(r.text)



from unittest import mock
from download.core import download
@mock.patch('download.core.open', new_callable=mock.mock.open)
@mock.patch('download.core.requests.get', autospec=True)
def test_download(mock_get, mock_open):
    url = 'https://example.com/sample.txt'
    download(url)
    mock_get.assert_called_once_with(url)
    mock_open.assert_called_once_with(
        'sample.txt', 'w', encoding='utf-8')



@mock.patch('download.core.open', new_callable=mock.mock.open)
@mock.patch('download.core.requests.get', autospec=True)



url = 'https://example.com/sample.txt'
download(url)



mock_get.assert_called_once_with(url)
mock_open.assert_called_once_with(
    'sample.txt', 'w', encoding='utf-8')

#https://www.thedigitalcatonline.com/blog/2016/03/06/python-mocks-a-gentle-introduction-part-1/

from unittest import mock
import mock

m = mock.Mock()

dir(m)

m.some_attribute

dir(m)
m.some_attribute
m.some_attribute()

m.some attribute.return_value = 42

m.some attribute()

def print_answer():
    print("42")

m.some_attribute.return_value = print_answer
m.some_attribute()

m.some_attribute.side_effect = ValueError('A custom value error')
m.some_attribute()


m.some_attribute.side_effect = range(3)
m.some_attribute()
0
m.some_attribute()
1
m.some_attribute()
2
m.some_attribute()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.4/unittest/mock.py", line 902, in __call__
    return _mock_self._mock_call(*args, **kwargs)
  File "/usr/lib/python3.4/unittest/mock.py", line 961, in _mock_call
    result = next(effect)
StopIteration



def print_answer():
    print("42")
m.some_attribute.side_effect = print_answer
m.some_attribute()


def print_number(num):
    print("Number:", num)

m.some_attribute.side_effect = print_number
m.some_attribute.side_effect(5)

sys.exit()






class Number(object):
    def __init__(self, value):
        self._value = value
    def print_value(self):
        print("Value:", self._value)

m.some_attribute.side_effect = Number
n = m.some_attribute.side_effect(26)
n
n.print_value()


mkdir mockplayground
cd mockplayground
virtualenv venv3 -p python3
source venv3/bin/activate
pip install --upgrade pip
pip install pytest
echo "[pytest]" >> pytest.ini
echo "norecursedirs=venv*" >> pytest.ini
mkdir tests
touch myobj.py
touch tests/test_mock.py
PYTHONPATH="." py.test


from unittest import mock
import myobj

def test_instantiation():
    external_obj = mock.Mock()
    myobj.MyObj(external_obj)
    external_obj.connect.assert_called_with()


class MyObj():
    def __init__(self, repo):
        repo.connect()


def test_setup():
    external_obj = mock.Mock()
    obj = myobj.MyObj(external_obj)
    obj.setup()
    external_obj.setup.assert_called_with(cache=True, max_connections=256)


class MyObj():
    def __init__(self, repo):
        self._repo = repo
        repo.connect()

    def setup(self):
        self._repo.setup(cache=True)



https://towardsdatascience.com/when-and-how-to-use-python-mock-b626e5f9bf7

animals()

def test_cow():
   assert cow() == {'cow': 'moo'}


test_cow()


def test_dog():
    assert dog() == {'dog': 'bark'}

test_dog()

def test_animals():
    assert animals() == {'dog': 'bark', 'cow': 'moo', 'pig': 'oink'}

test_animals()


from unittest.mock import patch
@patch('__main__.cow')
@patch('__main__.dog')
def test_animals(patched_dog, patched_cow):
    data = animals()
    assert patched_dog.called is True
    assert patched_cow.called is True
 

test_animals()

def animals():


@patch('__main__.cow')
@patch('__main__.dog')
def test_animals(patched_dog, patched_cow):
    patched_cow.return_value = {'c': 'm'}
    patched_dog.return_value = {'d': 'b'}
    data = animals()
    assert patched_dog.called is True
    assert patched_cow.called is True
    assert 'pig' in data

test_animals()

import requests
def is_valid_url(url):
 try:
     response = requests.get(url)
 except Exception:
     return False
 return response.status_code == 200






def test_is_valid_url():
    assert is_valid_url('http://agiliq.com') is True
    assert is_valid_url('http://agiliq.com/eerwweeee') is False # We want False in 404 pages too
    assert is_valid_url('http://aeewererr.com') is False
test_is_valid_url()



@patch('__main__.requests')
def test_is_valid_url(patched_requests):
    patched_requests.get.return_value = Mock(status_code=200)
    assert is_valid_url('http://agiliq.com') is True
    patched_requests.get.return_value = Mock(status_code=404)
    assert is_valid_url('http://agiliq.com/eerwweeee') is False # We want False in 404 pages too
    patched_requests.get = Mock(side_effect=Exception())
    assert is_valid_url('http://aeewererr.com') is False
test_is_valid_url()








#Patch



https://medium.com/analytics-vidhya/mocking-in-python-with-pytest-mock-part-i-6203c8ad3606

pip install pytest-mock

# application.py
from time import sleep
def is_windows():
    # This sleep could be some complex operation instead
    sleep(5)
    return True
def get_operating_system():
    return 'Windows' if is_windows() else 'Linux'



# test_application.py

from application import get_operating_system

def test_get_operating_system():
    assert get_operating_system() == 'Windows'


$ pytest


mocker.patch('application.is_windows', return_value=True)

# 'mocker' fixture provided by pytest-mock
def test_get_operating_system(mocker):
    # Mock the slow function and return True always
    mocker.patch('application.is_windows', return_value=True)
    assert get_operating_system() == 'Windows'

$ pytest

def test_operation_system_is_linux(mocker):
    mocker.patch('application.is_windows', return_value=False) # set the return value to be False
    assert get_operating_system() == 'Linux'



#https://medium.com/@durgaswaroop/writing-better-tests-in-python-with-pytest-mock-part-2-92b828e1453c




# application1.py

from time import sleep

def is_windows():
    # This sleep could be some complex operation instead
    sleep(5)
    return True


def get_operating_system():
    return 'Windows' if is_windows() else 'Linux'





# test_application1.py

from application1 import get_operating_system

# mocker is a fixture  provided by "pytest-mock"
def test_get_operating_system(mocker):
    mocker.patch('application1.is_windows', return_value=True)
    assert get_operating_system() == 'Windows'




# windows_utils.py

from time import sleep

def is_windows():
    # This sleep could be some complex operation instead
    sleep(5)
    return True


# application2.py

from windows_utils import is_windows

def get_operating_system():
    return 'Windows' if is_windows() else 'Linux'


mocker.patch('windows_utils.is_windows', return_value=True)


# test_application2.py

from application2 import get_operating_system

def test_get_operation_system(mocker):
    mocker.patch('application2.is_windows', return_value=True)
    assert get_operating_system() == 'Windows'


# application3.py

import windows_utils

def get_operating_system():
    return 'Windows' if windows_utils.is_windows() else 'Linux'


# test_application3.py

from application3 import get_operating_system

def test_get_operation_system(mocker):
    mocker.patch('application3.windows_utils.is_windows', return_value=True)
    assert get_operating_system() == 'Windows'