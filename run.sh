#!/bin/bash

source ~/.virtualenvs/sysmon/bin/activate
cd "$(dirname "$0")"
exec gunicorn -c gunicorn.conf.py main:__hug_wsgi__
