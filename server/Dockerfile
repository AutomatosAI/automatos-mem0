FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# eMudhra/emSign CA compromise (Oct 2026): pip < 26.2.2 keeps trusting the
# broken intermediate CAs via its own vendored certifi, regardless of what
# gets installed from requirements.txt — must upgrade pip itself first.
# Hash-pinned so the upgrade download itself isn't trusting the very CA
# chain it's fixing.
RUN printf 'pip==26.2.2 --hash=sha256:fd7f4dfa8190e014013b9f08f3e973f4e4c26ffd179a204895533a7254813a70\n' > /tmp/pip-boot.txt \
    && pip install --no-cache-dir --require-hashes -r /tmp/pip-boot.txt \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
