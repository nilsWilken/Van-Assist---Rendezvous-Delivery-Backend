FROM vanassistubuntu:1.0
WORKDIR /usr/src/app
ENV SUMO_HOME=/usr/share/sumo
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . .
WORKDIR ./venv
EXPOSE 8000
CMD ["gunicorn3", "-b 0.0.0.0:8000", "--threads=25", "--workers=1", "--worker-tmp-dir=/dev/shm", "--worker-class=gthread", "--timeout=1000", "--log-level=debug", "startUpFile:app"]


