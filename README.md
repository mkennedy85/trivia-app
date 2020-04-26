# Full Stack API Final Project

## Full Stack Trivia

This full stack trivia app is designed to provide you with an easy way to play quick and fun trivia games. It includes and backend API and a frontend to play the game with. You will find 6 categories and the ability to add new questions to any of those 6 categories. Each round of the quiz, when started will ask 5 questions from the selected category, or from all categories if no category is selected. At the end of the round you will receive a score of 0-5 depending on how many quiz questions you answered correctly, with 5 being a perfect score. If the selected category has less than 5 questions available, you will simply be scored based on the number of available questions in that category.

## Development

To start and develop on this application there are some key components that must be run, and the envinronment must be set up. With this project there is also tests available to validate the response from each of the expected API endpoints, as well as expected failure scenarios.

### Prequisites

These are the prequisites for running and testing this application. While it is not required, it is recommended that you use `virtualenv` for the backend, but this will remain up to you as to how you would like to manage dependancy installations.

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**

#### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
./setup_db.sh
```

### Backend

#### Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server.

> _tip_: This frontend is designed to work with [Flask-based Backend](../backend). It is recommended you stand up the backend first, test using Postman or curl, update the endpoints in the frontend, and then the frontend should integrate smoothly.

#### Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

### Tests

#### Database Setup

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
./setup_test_db.sh
```

#### Running Tests

To execute the tests you will run the following, which will execute tests of the API endpoints, as well as expected error scenarios:

> _tip_: To run the tests it is expected that the database setup occur before each test in order to ensure the expected state.

```bash
python3 test_flaskr.py
```

## API Reference

### Getting Started

This project is currently configured for running in a local development environment using Flask, and therefore the base URL for all API requests is `http://127.0.0.1:5000/`.

### Error Handling

All errors have been configured to return JSON payloads to remain consistent with successful responses. An example of an error response is:

```bash
{
  "error": 404,
  "message": "Not Found",
  "success": false
}
```

The errors that will be returned are:
- 400: Bad Request
- 404: Not Found
- 405: Method Not Allowed
- 422: Unprocessable Entity

### Headers

The application expects a header of `Content-Type: application/json`

### Endpoints

#### GET /categories

- General:
    - Returns a list of categories and their associated ID.
- Sample: `curl http://127.0.0.1:5000/categories`
```bash
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```

#### GET /questions

- General:
    - Returns a list of questions.
    - Paginated with each page containing 10 results. Defaults to page 1 with other pages being returned by passing a page argument.
- Sample:
    `curl http://127.0.0.1:5000/questions`
    `curl http://127.0.0.1:5000/questions?page=2`
```bash
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "page": 2,
  "questions": [
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```

#### DELETE /questions/$id

- General:
    - Deletes a question by ID.
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/2`
```bash
{
  "message": "Question ID 2 has been deleted",
  "success": true
}
```

#### POST /questions/add

- General:
    - Adds a question with the data from the JSON payload.
- Sample: 
```bash
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/questions/add
```
- Body:
```bash
{
	"question": "What is my name?",
	"answer": "Mike",
	"category": 1,
	"difficulty": 1
}
```
- Response:
```bash
{
  "success": true
}
```

#### POST /questions

- General:
    - Searches questions using a case-insensitive fuzzy matching.
- Sample: 
```bash
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/questions
```
- Body:
```bash
{
    "searchTerm": "name"
}
```
- Response:
```bash
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "page": 1,
  "questions": [
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }
  ],
  "success": true,
  "total_questions": 2
}
```

#### GET /categories/$category_id/questions

- General:
    - Returns a list of questions.
    - Paginated with each page containing 10 results. Defaults to page 1 with other pages being returned by passing a page argument.
- Sample:
    `curl http://127.0.0.1:5000/categories/2/questions`
    `curl http://127.0.0.1:5000/categories/2/questions?page=2`
```bash
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": 2,
  "page": 1,
  "questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "success": true,
  "total_questions": 4
}
```

#### POST /quizzes

- General:
    - Requests questions to populate a quiz with up to 5 questions.
    - Defaults to questions randomly selected from all categories.
    - If `quiz_category` is provided then the results will come from that category only.
    - Expects that an array of previous questions be provided so that questions are not repeated.
- Sample: 
```bash
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/questions
```
- Body:
```bash
{
  "quiz_category": {
  	"id": 1
  },
  "previous_questions": [20,21]
}
```
- Response:
```bash
{
  "question": {
    "answer": "Blood",
    "category": 1,
    "difficulty": 4,
    "id": 22,
    "question": "Hematology is a branch of medicine involving the study of what?"
  },
  "success": true
}
```