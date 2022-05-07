from unittest import mock

m = mock.Mock()
assert isinstance(m.foo, mock.Mock)
assert isinstance(m.bar, mock.Mock)
assert isinstance(m(), mock.Mock)
assert m.foo is not m.bar is not m()


#Configuring mock
m.foo = 'bar'
assert m.foo == 'bar'

m.configure_mock(bar='baz')
assert m.bar == 'baz'



m.return_value = 42
assert m() == 42

m.side_effect = ['foo', 'bar', 'baz']
assert m() == 'foo'
assert m() == 'bar'
assert m() == 'baz'
try:
    m()
except StopIteration:
    assert True
else:
    assert False

m.side_effect = RuntimeError('Boom')
try:
    m()
except RuntimeError:
    assert True
else:
    assert False