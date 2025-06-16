#!/bin/bash
sleep 2
gunicorn --bind 0.0.0.0:5000 api_model:app
