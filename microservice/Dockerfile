FROM python:3.10

RUN python -m pip install flask flask_restful gunicorn pandas numpy==1.23.5 \
    joblib==1.3.2 scikit-learn==1.3.0 catboost sqlalchemy psycopg2

WORKDIR /app

ADD api_model.py api_model.py
ADD model_cbr.pkl model_cbr.pkl
ADD start.sh start.sh

RUN chmod +x start.sh

EXPOSE 5000

CMD ["/bin/bash", "./start.sh"]

