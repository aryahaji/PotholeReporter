import os
import unittest

from PotHoleReporter import application as app
 
class RouteTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
 
    def tearDown(self):
        pass

    def register(self, firstName, lastName, town, email, password):
        return self.app.post(
            '/register',
            data=dict(firstName = firstName, lastName=lastName, town=town, email=email, password=password), follow_redirects=True
        )

    def test_register(self):
        response = self.register('test', 'test', 'Buffalo', 'test@gmail.com', 'test123')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()