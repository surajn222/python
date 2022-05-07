from main import get_operating_system
#from pytest import mocker
from unittest import mock

def test_get_operating_system():
    assert get_operating_system() == 'Windows'

#mock_object = mock.Mock()
#@mock.patch('main.is_windows', return_value=True)
def test_get_operating_system(mocker):
    # Mock the slow function and return True always
    mocker.patch('main.main2.is_windows', return_value=True)
    assert get_operating_system() == 'Windows'

