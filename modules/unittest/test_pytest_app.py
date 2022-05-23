import sys
sys.path.append("/Users/snathani/PycharmProjects/python/modules")
from unittest import TestCase, mock
from pytest_app.app_functions import execute_query_database_1
from pytest_app.app_functions import work_on

class TestWorkMockingModule(TestCase):
    def test_using_magicmock(self):
            #print(mock.patch('pytest_app.app_functions.execute_query_database_2'))
            # mocked_obj = mock.patch('pytest_app.app_functions.execute_query_database_2')
            mocked_obj = mock.patch(target = 'pytest_app.app_functions.execute_query_database_2')
            execute_query_database_1()
            # app_functions.execute_query_database_2("sql_1")
            # mocked_obj.execute_query_database_2("sql_1")
            #mocked_obj.execute_query_database_2("sql_1")
            print("macgicmock")
            print(mocked_obj)
            mocked_obj.assert_called_once()

    def test_using_context_manager_2(self):
        with mock.patch('pytest_app.app_functions.execute_query_database_2') as mocked_obj:
            execute_query_database_1()
            # app_functions.execute_query_database_2("sql_1")
            # mocked_obj.execute_query_database_2("sql_1")
            #mocked_obj.execute_query_database_2("sql_1")
            print("patch")
            print(mocked_obj)
            mocked_obj.assert_called_once()

    @mock.patch('pytest_app.app_functions.execute_query_database_2')
    def test_using_decorator_2(self, mocked_obj):
            execute_query_database_1()
            print(mocked_obj)
            # app_functions.execute_query_database_2("sql_1")
            # mocked_obj.execute_query_database_2("sql_1")
            #mocked_obj.execute_query_database_2("sql_1")
            mocked_obj.assert_called_once()

    def test_using_context_manager(self):
        with mock.patch('pytest_app.app_functions.os') as mocked_os:
            print(mocked_os)
            work_on()
            mocked_os.getcwd.assert_called_once()

    @mock.patch('pytest_app.app_functions.os')
    def test_using_decorator(self, mocked_os):
        work_on()
        mocked_os.getcwd.assert_called_once()

    def test_using_return_value(self):
        """Note 'as' in the context manager is optional"""
        with mock.patch('work.os.getcwd', return_value='testing'):
            assert work_on() == 'testing'
