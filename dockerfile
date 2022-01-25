FROM python:3.9.1

RUN pip install pandas psycopg2 sqlalchemy

WORKDIR /app
COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python","ingest_data.py" ]