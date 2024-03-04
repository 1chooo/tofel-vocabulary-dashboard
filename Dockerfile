FROM python:3.10-slim-buster

COPY ./requirements.txt /app/

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN useradd -m tofel

COPY . /app/

RUN chown -R tofel:tofel /app

USER tofel

CMD ["uvicorn", "Tofel.App.App:app", "--host", "0.0.0.0", "--port", "5002"]
