import sys
import os

# Add the 'src' folder to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


import pytest
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from utils import save_model, load_model


@pytest.fixture(scope="module")
def data():
    X, y = fetch_california_housing(return_X_y=True)
    return train_test_split(X, y, test_size=0.2, random_state=42)

def test_data_loaded(data):
    X_train, X_test, y_train, y_test = data
    assert X_train.shape[0] > 0
    assert y_train.shape[0] > 0

def test_model_instance():
    model = LinearRegression()
    assert isinstance(model, LinearRegression)

def test_model_trained(data):
    X_train, X_test, y_train, y_test = data
    model = LinearRegression()
    model.fit(X_train, y_train)
    assert hasattr(model, "coef_")

def test_r2_score_threshold(data):
    X_train, X_test, y_train, y_test = data
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    assert r2 > 0.5
