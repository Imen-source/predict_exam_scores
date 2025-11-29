import requests

# URL of your API
BASE_URL = "http://127.0.0.1:8000"

def predict_exam_score(study_hours):
    """Call the API and get the predicted exam score"""
    try:
        response = requests.get(f"{BASE_URL}/predict", params={"study_hours": study_hours})
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        print(f"Study Hours: {data['study_hours']}, Predicted Exam Score: {data['predicted_score']}")
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")

if __name__ == "__main__":
    # Example: predict for 5 study hours
    predict_exam_score(5)
    
    # You can also predict for multiple values
    for hours in [2, 4, 6, 8]:
        predict_exam_score(hours)
