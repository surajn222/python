from unittest import TestCase, mock
from worker import Worker, Helper

class TestWorkerModule(TestCase):

    def test_patching_class(self):
        with mock.patch('worker.Helper') as MockHelper:
            MockHelper.return_value.get_path.return_value = 'testing'
            worker = Worker()
            MockHelper.assert_called_once_with('db')
            self.assertEqual(worker.work(), 'testing')