To Run:

Install Python: https://www.python.org/downloads/release/python-3132/

Install Node.js (CLICK ADD TO PATH IN INSTALLER): https://nodejs.org/

RUN IDE IN ADMINISTRATOR MODE

cd backend

(first time only) py -m venv venv

venv\Scripts\activate

(first time only) pip install fastapi uvicorn

NECESSARY python libraries:
    pip install ordered_set

uvicorn main:app --reload

Visit http://localhost:8000

(only if in the backend folder in terminal) cd ..

cd frontend

(first time only) npm install

npm run serve

Visit http://localhost:8080
