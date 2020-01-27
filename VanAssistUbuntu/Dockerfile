FROM ubuntu:18.04
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:sumo/stable
RUN apt-get update && apt-get install -y \
	python3.7 \
	python3-pip \
	gunicorn3 \
	gunicorn \
	mariadb-server \
	libmariadbclient-dev \
	sumo
RUN pip3 install \
	firebase-admin \
	Flask \
	Flask-SQLAlchemy \
	gunicorn \
	geopy \
	lxml \
	SQLAlchemy \
	mysqlclient \
	oauthlib \
	pip \
	protobuf \
	pytz \
	pyxdg \
	PyYAML \
	urllib3 \
	httplib2 \
	greenlet \
	Jinja2 \
	pyserial \
	grpcio \
	CacheControl \
	futures \
	Click \
	itsdangerous \
	MarkupSafe \
	Werkzeug \
	pyproj
ENV SUMO_HOME=/usr/share/sumo