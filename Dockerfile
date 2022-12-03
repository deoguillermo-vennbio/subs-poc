FROM python:3.10

COPY entrypoint.sh /srv
RUN chmod +x /srv/entrypoint.sh

COPY requirements.txt /srv
RUN python -m venv /srv/venv
ENV PYTHONPATH=/srv/venv/bin:/srv
RUN pip install -r /srv/requirements.txt

COPY ./app /srv/app

EXPOSE 8000

WORKDIR /srv
ENTRYPOINT [ "bash",  "/srv/entrypoint.sh" ]
