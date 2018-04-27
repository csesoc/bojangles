FROM python:3

WORKDIR /app

RUN pip install pipenv

# Install dependencies into their own layer so they are cached between code changes
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY . .

EXPOSE 8080

CMD ["gunicorn", "-c", "gunicorn.py", "wsgi:app"]
