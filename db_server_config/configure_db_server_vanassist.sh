#!/bin/sh

apt-get update
apt-get install -y mariadb-server

mysql -u root  < vanassist_config.sql
mysql -u root vanassist < vanassist_v5.sql
