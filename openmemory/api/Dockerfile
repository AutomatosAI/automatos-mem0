FROM python:3.12-slim

LABEL org.opencontainers.image.name="mem0/openmemory-mcp"

WORKDIR /usr/src/openmemory

COPY requirements.txt .
# eMudhra/emSign CA compromise (Oct 2026): pip < 26.2.2 keeps trusting the
# broken intermediate CAs via its own vendored certifi, regardless of what
# gets installed from requirements.txt — must upgrade pip itself first.
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY config.json .
# Includes automatos_logging.py + automatos_metrics.py for observability
COPY . .

EXPOSE 8765
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8765"]
