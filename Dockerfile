FROM python:3.11-bookworm

WORKDIR /workspace

COPY . .

RUN pip install --no-cache-dir --upgrade -r server/requirements.txt


EXPOSE 8080

CMD ["python3", "server/app.py", "--log-level=DEBUG"]
