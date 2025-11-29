from fastapi import FastAPI, HTTPException, Query
import joblib
import os

app = FastAPI(
    title="Student Exam Score Predictor API",
    description="Predict exam scores based on study hours using a linear regression model.",
    version="1.0.0"
)

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), "..", "src", "linear_regression_model.pkl")
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    raise RuntimeError(f"Model file not found at {model_path}. Train and save your model first.")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Exam Score Predictor API!"}

@app.get("/predict")
def predict(study_hours: float = Query(..., ge=0, le=24, description="Number of study hours (0-24)")):
    """
    Predicts the exam score for a given number of study hours.
    - **study_hours**: float, number of hours studied
    """
    try:
        predicted_score = model.predict([[study_hours]])[0]
        return {"study_hours": study_hours, "predicted_score": round(predicted_score, 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
