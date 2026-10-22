FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# eMudhra/emSign CA compromise (Oct 2026): pip < 26.2.2 keeps trusting the
# broken intermediate CAs via its own vendored certifi, regardless of what
# gets installed from requirements.txt — must upgrade pip itself first.
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
