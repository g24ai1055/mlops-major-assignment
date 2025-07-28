# Dockerfile

FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

# ✅ Explicitly copy model file if needed (redundant if inside src/)
# COPY src/model.joblib ./src/model.joblib

CMD ["python", "src/predict.py"]
