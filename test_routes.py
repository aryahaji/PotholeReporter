import os
import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
 
from PotHoleReporter import application as app, db, loginManager
 
class RouteTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
 
    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_createTicket(self):
        response = self.app.get('/newTicket', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.app.get('/contact', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.app.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Buffalo(self):
        response = self.app.get('/town/Buffalo/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Amherst(self):
        response = self.app.get('/town/Amherst/2', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Clarence(self):
        response = self.app.get('/town/Clarence/3', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_West_Seneca(self):
        response = self.app.get('/town/West_Seneca/4', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Cheektowaga(self):
        response = self.app.get('/town/Cheektowaga/5', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Tonawanda(self):
        response = self.app.get('/town/Tonawanda/6', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Eden(self):
        response = self.app.get('/town/Eden/7', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Grand_Island(self):
        response = self.app.get('/town/Grand_Island/8', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Lancaster(self):
        response = self.app.get('/town/Lancaster/9', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Williamsville(self):
        response = self.app.get('/town/Williamsville/10', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Hamburg(self):
        response = self.app.get('/town/Hamburg/11', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Orchard_Park(self):
        response = self.app.get('/town/Orchard_Park/12', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Depew(self):
        response = self.app.get('/town/Depew/13', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Kenmore(self):
        response = self.app.get('/town/Kenmore/14', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Angola(self):
        response = self.app.get('/town/Angola/15', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
if __name__ == "__main__":
    unittest.main()


    # def register(self, firstName, lastName, town, email, password):
    #     return self.app.post(
    #         '/register',
    #         data=dict(firstName = firstName, lastName=lastName, town=town, email=email, password=password), follow_redirects=True
    #     )

    # def test_register(self):
    #     response = self.register('test', 'test', 'Buffalo', 'test@gmail.com', 'test123')
    #     self.assertEqual(response.status_code, 200)