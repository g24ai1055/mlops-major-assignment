import os
import sys
import pytest
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# ✅ Add src/ to sys.path so Python can find utils.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.utils import save_model, load_model


def main():
    # Load dataset
    print("📥 Loading California Housing dataset...")
    data = fetch_california_housing()
    X, y = data.data, data.target

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    print("🏋️‍♂️ Training Linear Regression model...")
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print(f"✅ R² Score: {r2:.4f}")
    print(f"📉 MSE Loss: {mse:.4f}")

    # Save model
    model_path = "src/model.joblib"
    save_model(model, model_path)
    print(f"💾 Model saved to {model_path}")

if __name__ == "__main__":
    main()
