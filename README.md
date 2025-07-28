Got it — the current `README.md` directory structure is rendering **in one line**, which breaks clarity.

Here’s a **refined, correctly formatted `README.md`** that uses code blocks and markdown lists to make the project structure readable and beautiful.

---

### ✅ Final Cleaned `README.md`

```markdown
# 🧠 MLOps: Linear Regression with Quantization

[![CI Status](https://github.com/g24ai1055/mlops-major-assignment/actions/workflows/ci.yml/badge.svg)](https://github.com/g24ai1055/mlops-major-assignment/actions)

A simple end-to-end MLOps project that:

- Trains a Linear Regression model on the California Housing dataset
- Performs manual quantization
- Runs unit tests
- Builds a Docker container and tests predictions inside it
- Automates the pipeline via GitHub Actions

---

## 📁 Project Structure

```

mlops-major-assignment/
├── src/
│   ├── train.py              # Training and saving model
│   ├── quantize.py           # Manual quantization logic
│   ├── predict.py            # Predict using trained model
│   ├── utils.py              # Utility functions
│   ├── model.joblib          # Trained model (generated after training)
│   └── quant\_params.joblib   # Quantized parameters (generated)
│
├── tests/
│   └── test\_utils.py         # Unit tests for utilities
│
├── .github/workflows/
│   └── ci.yml                # GitHub Actions CI workflow
│
├── Dockerfile                # Docker build script
├── requirements.txt          # Python dependencies
└── README.md

````

---

## 🚀 How to Run

### 💻 Locally

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Train the model
python src/train.py

# Apply quantization
python src/quantize.py

# Run prediction
python src/predict.py
````

---

### 🐳 Using Docker

```bash
# Build Docker image
docker build -t mlops-lr .

# Run prediction in container
docker run --rm mlops-lr
```

---

## ⚙️ GitHub Actions Pipeline

This project uses GitHub Actions to automate:

* ✅ Unit Tests via `pytest`
* ✅ Model Training & Saving
* ✅ Parameter Quantization
* ✅ Docker Build & Prediction Test

> Automatically runs on every push to `main`.

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 📝 Sample Output

```
📥 Loading California Housing dataset...
🏋️‍♂️ Training Linear Regression model...
✅ R² Score: 0.5758
📉 MSE Loss: 0.5559
💾 Model saved to src/model.joblib

📊 Sample Predictions:
Actual: 0.48 | Predicted: 0.72
Actual: 0.46 | Predicted: 1.76
...
```

---

## 👨‍💻 Author

* GitHub: ANIL KUAMR  IIT JODHPUR

---

## 📄 License

This project is licensed under the **MIT License**.

```

---


```
