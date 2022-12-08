#!/bin/bash

source ~/.pyenv/versions/sysmon/bin/activate
cd "$(dirname "$0")"
exec gunicorn -c gunicorn.conf.py main:__hug_wsgi__
