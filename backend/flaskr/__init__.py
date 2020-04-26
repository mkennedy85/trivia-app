import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = list(map(Question.format, selection))
  current_questions = questions[start:end]

  return current_questions

def all_categories():
  categories = Category.query.all()
  formatted_categories = {category.id:category.type for category in categories}
  return formatted_categories

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  CORS(app)
  cors = CORS(app, resources={r"*": {"origins": "*"}})

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PUT, PATCH, DELETE, OPTIONS')
    return response

  @app.route('/categories')
  def get_categories():
    categories = all_categories()

    if len(categories) == 0:
      abort(404)

    result = {
      'success': True,
      'categories': categories
    }

    return jsonify(result)

  @app.route('/questions')
  def get_questions():
    selection = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)
    categories = all_categories()

    if len(current_questions) == 0:
      abort(404)

    result = {
      'success': True,
      'questions': current_questions,
      'total_questions': len(selection),
      'categories': categories,
      'current_category': None,
      'page': request.args.get('page', 1, type=int)
    }

    return jsonify(result)

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).first()
      question.delete()
    except:
      abort(404)
    finally:
      result = {
        'success': True,
        'message': f'Question ID {question_id} has been deleted'
      }

    return jsonify(result)

  @app.route('/questions/add', methods=['POST'])
  def add_question():
    data = {
      'question': request.get_json()['question'],
      'answer': request.get_json()['answer'],
      'category': request.get_json()['category'],
      'difficulty': request.get_json()['difficulty']
    }

    check_for_duplicate = Question.query.filter(Question.question == data['question']).all()
    if len(check_for_duplicate) > 0:
      abort(422)

    question = Question(**data)
    question.insert()
    
    result = {
      'success': True,
    }

    return jsonify(result)

  @app.route('/questions', methods=['POST'])
  def search_questions():
    selection = Question.query.filter(Question.question.ilike(f"%{request.get_json()['searchTerm']}%")).all()
    current_questions = paginate_questions(request, selection)
    categories = all_categories()

    if len(current_questions) == 0:
      abort(404)

    result = {
      'success': True,
      'questions': current_questions,
      'total_questions': len(selection),
      'categories': categories,
      'page': request.args.get('page', 1, type=int)
    }

    return jsonify(result)

  @app.route('/categories/<int:category_id>/questions')
  def get_questions_category(category_id):
    selection = Question.query.filter_by(category=category_id).all()
    current_questions = paginate_questions(request, selection)
    categories = all_categories()

    if len(current_questions) == 0:
      abort(404)

    result = {
      'success': True,
      'questions': current_questions,
      'total_questions': len(selection),
      'categories': categories,
      'current_category': category_id,
      'page': request.args.get('page', 1, type=int)
    }

    return jsonify(result)

  @app.route('/quizzes', methods=['POST'])
  def get_questions_for_quiz():
    if request.get_json()['quiz_category']['id'] == 0:
      selection = Question.query.all()
    else:
      selection = Question.query.filter_by(category=request.get_json()['quiz_category']['id']).all()
    questions = list(map(Question.format, selection))

    if len(questions) == 0:
      abort(404)

    for question in request.get_json()['previous_questions']:
      questions = list(filter(lambda i: i['id'] != question, questions))

    if questions:
      question = random.choice(questions)
    else:
      question = False

    result = {
      'success': True,
      'question': question,
    }

    return jsonify(result)

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': 'Bad Request'
    }), 400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': 'Not Found'
    }), 404

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message': 'Method Not Allowed'
    }), 405

  @app.errorhandler(422)
  def unprocessable_entity(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': 'Unprocessable Entity'
    }), 422
  
  return app