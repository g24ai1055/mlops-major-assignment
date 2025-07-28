import joblib
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

def quantize_array(arr, min_val, max_val):
    """Normalize and quantize float array to uint8"""
    scaled = (arr - min_val) / (max_val - min_val)
    quantized = (scaled * 65535).astype(np.uint16)
    return quantized

def dequantize_array(qarr, min_val, max_val):
    """Convert uint8 back to float array"""
    scaled = qarr.astype(np.float32) / 65535.0

    return scaled * (max_val - min_val) + min_val

def main():
    # Load test data
    print("📥 Loading California Housing dataset...")
    data = fetch_california_housing()
    X, y = data.data, data.target
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Load trained model
    print("📦 Loading trained model from model.joblib...")
    model = joblib.load("src/model.joblib")

    # Extract original weights
    weights = model.coef_
    intercept = model.intercept_

    # Save raw parameters
    joblib.dump({"weights": weights, "intercept": intercept}, "src/unquant_params.joblib")
    print("💾 Saved raw model parameters to unquant_params.joblib")

    # Quantization (manual)
   
    w_min, w_max = weights.min(), weights.max()

    i_min, i_max = intercept - 1.0, intercept + 1.0

    q_weights = quantize_array(weights, w_min, w_max)
    q_intercept = quantize_array(np.array([intercept]), i_min, i_max)[0]

    # Save quantized params + scale info
    quant_data = {
        "q_weights": q_weights,
        "q_intercept": q_intercept,
        "w_min": w_min,
        "w_max": w_max,
        "i_min": i_min,
        "i_max": i_max
    }
    joblib.dump(quant_data, "src/quant_params.joblib")
    print("💾 Saved quantized model parameters to quant_params.joblib")

    # Dequantization
    dq_weights = dequantize_array(q_weights, w_min, w_max)
    dq_intercept = dequantize_array(np.array([q_intercept]), i_min, i_max)[0]

    # Inference with dequantized weights
    y_pred = np.dot(X_test, dq_weights) + dq_intercept
    r2 = r2_score(y_test, y_pred)

    print("\n🎯 Quantized Model Evaluation")
    print(f"✅ R² Score (quantized): {r2:.4f}")
    print("\n🔍 Sample Predictions (first 5):")
    for i in range(5):
        print(f"Actual: {y_test[i]:.2f} | Predicted: {y_pred[i]:.2f}")

if __name__ == "__main__":
    main()
