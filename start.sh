#!/bin/bash
cd /home/ubuntu/livestream
source ./venv/bin/activate
cd stream
python3 manage.py runserver 0.0.0.0:8000
