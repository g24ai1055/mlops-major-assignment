import joblib
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

def main():
    print("✅ Starting predict.py")

    print("📥 Loading dataset...")
    data = fetch_california_housing()
    X, y = data.data, data.target

    # ❗ Do NOT discard values using `_`, explicitly assign all 4
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("📦 Loading trained model...")
    model = joblib.load("src/model.joblib")

    print("🔍 Running predictions on test set...")
    y_pred = model.predict(X_test)

    print("\n📊 Sample Predictions:")
    for i in range(5):
        print(f"Actual: {y_test[i]:.2f} | Predicted: {y_pred[i]:.2f}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error occurred: {e}")
