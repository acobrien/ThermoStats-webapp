To Run:

Install Python: https://www.python.org/downloads/release/python-3132/

Install Node.js: https://nodejs.org/

cd backend

(first time only) py -m venv venv

venv\Scripts\activate

(first time only) pip install fastapi uvicorn

uvicorn main:app --reload

Visit http://localhost:8000

(only if in the backend folder in terminal) cd ..

cd frontend

(first time only) npm install 

npm run serve

Visit http://localhost:8080
