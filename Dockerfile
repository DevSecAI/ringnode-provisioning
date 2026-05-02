# RNG-IAC-004: runs as root, no HEALTHCHECK.
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ringnode/ ./ringnode/
EXPOSE 5000
CMD ["python", "-m", "ringnode.app"]
