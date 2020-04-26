import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            'question': 'What is my name?',
            'answer': 'Mike',
            'category': 1,
            'difficulty': 1
        }

        self.search = {
            'searchTerm': 'name'
        }

        self.quiz = {
            'previous_questions': [],
            'quiz_category': {
                'id': 0
            }
        }

    def tearDown(self):
        """Executed after each test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # Defining an order for the tests to ensure that dependancy is accounted for
    def make_orderer():
        order = {}

        def ordered(f):
            order[f.__name__] = len(order)
            return f

        def compare(a, b):
            return [1, -1][order[a] < order[b]]

        return ordered, compare

    ordered, compare = make_orderer()
    unittest.defaultTestLoader.sortTestMethodsUsing = compare  
    
    @ordered
    def test_add_question(self):
        res = self.client().post('/questions/add', json=self.new_question)
        self.assertEqual(res.status_code, 200)

    @ordered
    def test_422_add_question(self):
        res = self.client().post('/questions/add', json=self.new_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
    
    @ordered
    def test_get_questions(self):
        res = self.client().get('/questions')
        self.assertEqual(res.status_code, 200)

    @ordered
    def test_search_questions(self):
        res = self.client().post('/questions', json=self.search)
        self.assertEqual(res.status_code, 200)

    @ordered
    def test_get_question_by_categories(self):
        res = self.client().get('/categories/1/questions')
        self.assertEqual(res.status_code, 200)

    @ordered
    def test_delete_question(self):
        res = self.client().delete('/questions/2')
        data = json.loads(res.data)
        self.assertEqual(data['message'], 'Question ID 2 has been deleted')
        self.assertEqual(res.status_code, 200)

    @ordered
    def test_404_get_questions(self):
        res = self.client().delete('/questions/10000')
        self.assertEqual(res.status_code, 404)

    @ordered
    def test_get_categories(self):
        res = self.client().get('/categories')
        self.assertEqual(res.status_code, 200)

    @ordered
    def test_405_delete_categories(self):
        res = self.client().delete('/categories')
        self.assertEqual(res.status_code, 405)

    @ordered
    def test_post_quiz(self):
        res = self.client().post('/quizzes', json=self.quiz)
        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()