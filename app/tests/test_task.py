import json
from . import BaseTestClass


URL = '/api/v1/tasks'
GOOD_URL = '/api/v1/tasks/1'
BAD_URL = '/api/v1/tasks/2'


class TaskTest(BaseTestClass):

    def test_index(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)

    def test_index_post(self):
        res = self.client.post('/')
        self.assertEqual(405, res.status_code)

    def test_get_tasks(self):
        res = self.client.get('/api/v1/tasks')
        self.assertEqual(200, res.status_code)

    def test_get_task(self):
        res = self.client.get('/api/v1/tasks/1')
        self.assertEqual(200, res.status_code)

    def test_create_task(self):
        new_task = {
            'title': 'New task',
            'description': 'First task',
            'start_date': '2021-05-05',
            'due_date': '2021-05-25',
            'priority': 'alta'
        }
        res = self.client.post('/api/v1/tasks', data=json.dumps(new_task), content_type='application/json')
        self.assertEqual(200, res.status_code)




