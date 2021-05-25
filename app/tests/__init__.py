import unittest
from app import create_app
from app.models import db
from app.config import config


class BaseTestClass(unittest.TestCase):
    def setUp(self):
        environment = config['test']
        self.app = create_app(environment)
        self.client = self.app.test_client()

    def tearDown(self):
        with self.app.app_context():
            # Delete all database
            db.session.remove()
            db.drop_all()
