# -*- coding: utf-8 -*-
import os

GUNICORN_WORKERS = int(os.getenv("GUNICORN_WORKERS", 2))
GUNICORN_THREADS = int(os.getenv("GUNICORN_THREADS", 10))
GUNICORN_MAX_REQUESTS = int(os.getenv("GUNICORN_MAX_REQUESTS", 10240))


wsgi_app = "app:app"
bind = "0.0.0.0:8080"

proc_name = "demo-app"

daemon = False
reuse_port = True

# https://docs.gunicorn.org/en/latest/settings.html#logging
accesslog = None
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = "-"


# https://docs.gunicorn.org/en/latest/settings.html#workers
workers = GUNICORN_WORKERS
worker_class = "sync"
threads = GUNICORN_THREADS
worker_connections = 1024
max_requests = GUNICORN_MAX_REQUESTS
