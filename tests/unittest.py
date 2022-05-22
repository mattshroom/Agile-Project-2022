import unittest, os, tempfile, pytest
from app import app, db
from app.models import User, Result, Logo
from datetime import datetime

class UserModelCase(unittest.TestCase):
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI']=\
            'sqlite:///'+os.path.join(basedir,'test.db')
        self.app = app.test_client()                        # create a virtual testing env
        db.create_all()
        u1 = User(id='1',username='Test',email='Case@unittest.com')
        u2 = User(id='2',username='Another',email='test@unittest.com')
        l1 = Logo(logo_id='1',logoname='testlogo',logolink='https://global-uploads.webflow.com/5e157547d6f791d34ea4e2bf/6087f2b060c7a92408bac811_logo.svg')
        r1 = Result(result_id='1',score='100000',guesses='1',time='0')
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(l1)
        db.session.add(r1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hash(self):
        u = User.query.get('1')
        u.set_password('test')
        self.assertFalse(u.check_password('case'))
        self.assertTrue(u.check_password('test'))

    def test_user_result_link(self):
        r1 = Result.query.get('1')
        u1 = User.query.get('1')
        r1.user_id = u1.id
        print(f'\nThis is the score of result 1: {r1.score}')

        r2 = Result(score='50000',guesses='1',time='60000')
        db.session.add(r2)
        db.session.commit()

        print(f'{u1.id} vs {r1.user_id}')

        print(f'This is the score of result 2: {r2.score}')

        print(f'Following tests on which user owns which result: \n')
        self.assertFalse(r1.user_id ==2)
        self.assertTrue(r1.user_id  ==1)

    def test_results_date(self):
        today= datetime.utcnow().date()
        print(today)
        r1 = Result.query.get('1')
        print(r1.timestamp)
        self.assertTrue(today == r1.timestamp.date())

    



if __name__=='__main__':
    unittest.main()