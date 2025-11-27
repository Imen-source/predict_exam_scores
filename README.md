# Predict Student Exam Scores

## Project Overview
This project demonstrates a **full machine learning workflow** using Python.  
It predicts student exam scores based on the number of study hours using **linear regression**.

Even though the dataset is small, the project showcases:

- Data preparation
- Model training and evaluation
- Visualization
- Interactive deployment using Streamlit

---

## Dataset
- Generated a dataset of 30 students with:
  - `study_hours` (1–10 hours)
  - `exam_score` (0–100)
- Linear relationship with random noise: `exam_score = study_hours * 8 + noise`
- Stored in `data/students_scores.csv`

---

## Technical Stack
- Python 3
- Libraries:
  - `numpy`, `pandas` (data manipulation)
  - `scikit-learn` (linear regression, train/test split, evaluation)
  - `matplotlib` (visualization)
  - `Streamlit` (interactive app)

---

## Project Structure

```
predict_exam_scores/
│
├── data/                # Dataset CSV
├── notebooks/           # Jupyter Notebook for exploration, training, evaluation, visualization
├── app/                 # Streamlit interactive app
├── src/                 # Source modules (data preparation, model, evaluation, visualization)
├── .gitignore           # Optional (sample below)
└── README.md
```

---

## Usage

### 1. Jupyter Notebook
1. Open `notebooks/predict_scores.ipynb`
2. Run cells sequentially:
   - Load dataset
   - Explore data
   - Train linear regression model
   - Evaluate model (MSE, R²)
   - Visualize results (scatter + regression line)

### 2. Streamlit App
1. Make sure you have Streamlit installed:

```bash
pip install streamlit
```

2. Run the app:

```bash
streamlit run app/streamlit_app.py
```

Enter study hours and see the predicted exam score in real-time.

## Screenshots
- Scatter plot + regression line
- Streamlit app interface

Replace placeholders below with your actual screenshots if you want to include images.

---

## Key Learnings

- Implemented linear regression from start to finish
- Trained and evaluated the model using proper metrics (MSE, R²)
- Visualized results to understand model behavior
- Built an interactive app to showcase predictions
- Learned project structuring for GitHub portfolios

## Next Steps / Extensions

- Add more features (attendance, assignments, study environment)
- Try more complex models (Ridge, Lasso, Random Forest)
- Scale to larger datasets
- Add user authentication and advanced Streamlit features

---

## Optional: .gitignore (suggested)

```gitignore
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
```

---

If you'd like, I can also add a small `requirements.txt` or update the `notebooks/predict_scores.ipynb` with a short usage cell — tell me which you'd prefer.
