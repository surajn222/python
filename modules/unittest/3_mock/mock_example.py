from unittest.mock import Mock

mock = Mock()
print(mock)

import json
print(dir(json))
data = json.dumps({'a':1})
print(data)

json = Mock()
print(dir(json))
data = json.dumps({'a':1})
print(data)


print("Assert statements of mock:")
print("Check if json.dumps was called:")
print(json.dumps.assert_called())
print("Check if json.dumps was called once:")
print(json.dumps.assert_called_once())
print("Check if json.dumps was called with:")
print(json.dumps.assert_called_with({'a':1}))
print("Print arguments that were called:")
print(json.dumps.call_args)
print("Print count of number of times of the argument:")
print(json.dumps.call_count)
print("Print method calls:")
print(json.method_calls)

from datetime import datetime
datetime = Mock()
datetime.today.return_value = datetime(year=2019,month=22,day=1)
print(dir(datetime.today))
today_value = datetime.today
print(today_value)
