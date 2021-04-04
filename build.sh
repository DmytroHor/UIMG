#!/bin/bash

set -e

source venv/bin/activate

pip install -r requirements.txt

./manage.py migrate  --no-input --traceback
./manage.py collectstatic --no-input --traceback
# ./manage.py runserver 0.0.0.0:8888  # for local env api
