FROM docker.io/yaxin/demo-app-runtime:latest

COPY --chown=root:root . /app/

WORKDIR /app/

ENTRYPOINT ["/entrypoint.sh"]

CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]
