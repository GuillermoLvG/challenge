FROM tiangolo/uvicorn-gunicorn:python3.8
COPY src/ /app/
COPY Pipfile /app
COPY Pipfile.lock /app
#RUN ls -la /app/*
WORKDIR /app
RUN apt-get update -y
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
# Install production dependencies.
RUN pip install Flask gunicorn
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 main:app
