# app.py
# Train a tiny sklearn model (Iris) and serve predictions via Flask.
import os
import joblib
from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

MODEL_PATH = "model.pkl"
app = Flask(__name__)

def train_and_save():
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train, y_train)
    acc = clf.score(X_test, y_test)
    joblib.dump(clf, MODEL_PATH)
    print(f"Trained RandomForest; test acc={acc:.3f}; model saved to {MODEL_PATH}")
    return clf

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    else:
        return train_and_save()

model = load_model()

@app.route("/")
def index():
    return "ML-Ops demo: RandomForest Iris model. POST /predict with json {'features': [..4 values..]}"

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json()
    if not payload or "features" not in payload:
        return jsonify({"error": "provide JSON with key 'features' (list of 4 numbers)"}), 400
    features = payload["features"]
    try:
        pred = model.predict([features]).tolist()
        proba = model.predict_proba([features]).tolist()
        return jsonify({"prediction": pred[0], "proba": proba[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/retrain", methods=["POST"])
def retrain():
    global model
    model = train_and_save()
    return jsonify({"status": "retrained", "model_path": MODEL_PATH})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
