FROM python:3.8.5-slim-buster

COPY . /python-backend

WORKDIR /python-backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.api.server:app", "--host=0.0.0.0", "--reload"]