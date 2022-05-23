#https://medium.com/@yasufumy/python-mock-basics-674c33de1ced
print("HW")
sys.exit()

from unittest import mock

requests = mock.Mock()
requests.get.return_value.status_code = 200

r = requests.get('https://api.github.com/user',auth=('user', 'pass'))
print(r.status_code)


sys.exit()



from unittest import mock


requests = mock.Mock()
r = requests.get('https://api.github.com/user',
                     auth=('user', 'pass'))


m = mock.Mock()
m.can.access.any.attribute


m = mock.Mock()
m.can.accespt.any.call('with', 'any', 'argument', [1, 2, 3])


requests = mock.Mock()
r = requests.get('https://api.github.com/user',
                     auth=('user', 'pass'))
r
<Mock name='mock.get()' id='4843843480'>
r.status_code
<Mock name='mock.status_code' id='4844769744'>



m = mock.Mock(return_value=42)
m()
42



m = mock.Mock(return_value=42)
m.any.method()
<Mock name='mock.any.method()' id='4559789192'>




requests = mock.Mock()
requests.get.return_value.status_code = 200
r = requests.get('https://api.github.com/user',
                     auth=('user', 'pass'))
r.status_code
200



requests.get.return_value.status_code = 200


requests.get.return_value.status_code = 200
r = requests.get('invalid_url')
r.status_code
200


m = mock.Mock(side_effect=lambda x: x % 2 == 0)
m(42)
True
m(11)
False



def return_status_code(url, *args, **kwargs):
...     code = 200 if url == 'https://api.github.com/user' else 404
...     m = Mock()
...     m.status_code = code
...     return m
...
requests = mock.Mock()
requests.get.side_effect = return_status_code
requests.get('https://api.github.com/user',
                 auth=('user', 'pass')).status_code
200
requests.get('invalid_url').status_code
404


requests = mock.Mock()
r = requests.get('https://api.github.com/user',
                     auth=('user', 'pass'))
requests.mock_calls
[call.get('https://api.github.com/user', auth=('user', 'pass'))]




call_info = requests.mock_calls[0]
call_info[0]  # the method name
'get'
call_info[1]  # the positonal arguments
('https://api.github.com/user',)
call_info[2]  # the keyword arguments
{'auth': ('user', 'pass')}
method, args, kwargs = call_info




requests = mock.Mock()
r = requests.get('https://api.github.com/user',
                     auth=('user', 'pass'))
requests.get.assert_called_once_with(
        'https://api.github.com/user', auth=('user', 'pass'))








mm = mock.MagicMock()
mm['any_key_you_want']
<MagicMock name='mock.__getitem__()' id='4382933288'>
for x in mm:
...     ...
...
>>>

requests = mock.MagicMock()
requests.unwanted_method()
<MagicMock name='mock.unwanted_method()' id='5155967104'>



import requests
mock_requests = mock.MagicMock(spec=requests)
mock_requests.unwanted_method()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/path/to/python/unittest/mock.py", line 580, in __getattr__
raise AttributeError("Mock object has no attribute %r" % name)
AttributeError: Mock object has no attribute 'unwanted_method'




import requests
mock_requests = mock.MagicMock(spec=requests)
r = mock_requests.Session()
r.unwanted_method()
<Mock name='mock.Session().unwanted_method()' id='4602617192'>




import requests
mock_requests = mock.create_autospec(spec=requests)
r = mock_requests.Session()
r.unwanted_method()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/path/to/python/unittest/mock.py", line 580, in __getattr__
raise AttributeError("Mock object has no attribute %r" % name)
AttributeError: Mock object has no attribute 'unwanted_method'





import requests
with mock.patch('__main__.requests', autospec=True):
...     requests.get('https://api.github.com/user',
...                  auth=('user', 'pass')
...     requests.get.assert_called_once_with(
...         'https://api.github.com/user', auto=('user', 'pass'))






with mock.patch('__main__.requests', autospec=True) as mock_requests:
...     mock_requests.get('https://api.github.com/user',
...                       auth=('user', 'pass')
...     mock_requests.get.assert_called_once_with(
...         'https://api.github.com/user', auto=('user', 'pass'))
...     assert mock_requests == requests





@mock.patch('__main__.requests', autospec=True)
... def test_requests_get(requests):
...     requests.get('https://api.github.com/user',
...                  auth=('user', 'pass')
...     requests.get.assert_called_once_with(
...         'https://api.github.com/user', auto=('user', 'pass'))
test_requests_get()





patcher = mock.patch('__main__.requests', autospec=True)
patcher.start()
requests.get('https://api.github.com/user',
...              auth=('user', 'pass'))
requests.get.assert_called_once_with(
...     'https://api.github.com/user', auth=('user', 'pass'))
patcher.stop()




with mock.patch('requests.get', autospec=True) as mock_get:
...     mock_get('https://api.github.com/user',
                 auth=('user', 'pass'))
...     mock_get.assert_called_once_with(
...         'https://api.github.com/user', auth=('user', 'pass'))






with mock.patch('pickle.dumps', autospec=True) as mock_dumps:
...     mock_dumps('object_to_save')
...     mock_dumps.assert_called_once_with('object_to_save')






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
...  print("42")
...
>>>
m.some_attribute.return_value = print_answer
m.some_attribute()
<function print_answer at 0x7f8df1e3f400>


m.some_attribute.side_effect = ValueError('A custom value error')
m.some_attribute()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.4/unittest/mock.py", line 902, in __call__
    return _mock_self._mock_call(*args, **kwargs)
  File "/usr/lib/python3.4/unittest/mock.py", line 958, in _mock_call
    raise effect
ValueError: A custom value error


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
...     print("42")
m.some_attribute.side_effect = print_answer
m.some_attribute()


def print_number(num):
...     print("Number:", num)
...
m.some_attribute.side_effect = print_number
m.some_attribute.side_effect(5)
Number: 5


class Number(object):
...     def __init__(self, value):
...         self._value = value
...     def print_value(self):
...         print("Value:", self._value)
...
m.some_attribute.side_effect = Number
n = m.some_attribute.side_effect(26)
n
<__main__.Number object at 0x7f8df1aa4470>
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


In [4]: animals()
cow
dog
Out[4]: {'cow': 'moo', 'dog': 'bark', 'pig': 'oink'}


In [5]: def test_cow():
   ...:     assert cow() == {'cow': 'moo'}


In [6]: test_cow()
cow


In [7]: def test_dog():
   ...:     assert dog() == {'dog': 'bark'}
   ...:
In [8]: test_dog()
dog


In [9]: def test_animals():
   ...:     assert animals() == {'dog': 'bark', 'cow': 'moo', 'pig': 'oink'}
   ...:
In [10]: test_animals()
cow
dog


In [17]: from unittest.mock import patch
In [18]: @patch('__main__.cow')
    ...: @patch('__main__.dog')
    ...: def test_animals(patched_dog, patched_cow):
    ...:     data = animals()
    ...:     assert patched_dog.called is True
    ...:     assert patched_cow.called is True
    ...:


In [19]: test_animals()



In [20]: def animals():


In [43]: @patch('__main__.cow')
    ...: @patch('__main__.dog')
    ...: def test_animals(patched_dog, patched_cow):
    ...:     patched_cow.return_value = {'c': 'm'}
    ...:     patched_dog.return_value = {'d': 'b'}
    ...:     data = animals()
    ...:     assert patched_dog.called is True
    ...:     assert patched_cow.called is True
    ...:     assert 'pig' in data

In [45]: test_animals()



#Another example

In [59]: import requests
In [60]: def is_valid_url(url):
    ...:     try:
    ...:         response = requests.get(url)
    ...:     except Exception:
    ...:         return False
    ...:     return response.status_code == 200


In [69]: def test_is_valid_url():
    ...:     assert is_valid_url('http://agiliq.com') is True
    ...:     assert is_valid_url('http://agiliq.com/eerwweeee') is False # We want False in 404 pages too
    ...:     assert is_valid_url('http://aeewererr.com') is False
In [70]: test_is_valid_url()



In [71]: @patch('__main__.requests')
    ...: def test_is_valid_url(patched_requests):
    ...:     patched_requests.get.return_value = Mock(status_code=200)
    ...:     assert is_valid_url('http://agiliq.com') is True
    ...:     patched_requests.get.return_value = Mock(status_code=404)
    ...:     assert is_valid_url('http://agiliq.com/eerwweeee') is False # We want False in 404 pages too
    ...:     patched_requests.get = Mock(side_effect=Exception())
    ...:     assert is_valid_url('http://aeewererr.com') is False
    ...:
In [72]: test_is_valid_url()


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

