To Run:

Install Python: https://www.python.org/downloads/release/python-3132/

Install Node.js (CLICK ADD TO PATH IN INSTALLER): https://nodejs.org/

RUN IDE IN ADMINISTRATOR MODE

cd backend

py -m venv venv

venv\Scripts\activate

pip install fastapi uvicorn ordered_set scikit-learn scipy pandas quantile-forest

uvicorn main:app --reload

NEW TERMINAL TAB

cd frontend

npm install

npm run serve

Visit http://localhost:8080
