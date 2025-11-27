import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv(r"C:\Users\Hp\predict_exam_scores\data\students_scores.csv")


# Train the model
X = df[['study_hours']]
y = df['exam_score']
model = LinearRegression()
model.fit(X, y)

# Streamlit interface
st.title("Predict Student Exam Scores")
st.write("Enter the number of study hours to predict the exam score:")

# Input
hours = st.number_input("Study Hours", min_value=0, max_value=24, value=5, step=1)

# Prediction
predicted_score = model.predict([[hours]])[0]
st.success(f"Predicted Exam Score: {predicted_score:.2f}")
