# EduPredict AI — Student Performance Analytics & Prediction

**Student:** Sanket Shantaram Tarle  
**Course:** BCS / B.Sc. Computer Science — Third Year  
**College:** K. K. Wagh Arts, Commerce, Science and Computer Science College, Chandori  
**Internship:** AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026 | BharatCares

## 1. Project Overview

EduPredict AI is a Python-based data analytics and machine-learning application that analyzes student performance factors and predicts a student's final grade (G3) on a 0–20 scale.

The project combines:
- Data cleaning and exploratory analysis
- Numerical and categorical preprocessing
- Random Forest regression
- Model evaluation using MAE, RMSE and R²
- Flask web dashboard
- Student-level prediction form
- Analytics visualizations

## 2. Dataset

The bundled `data/student_performance.csv` contains **649 synthetic, offline-ready demonstration records**. Its feature structure is inspired by the public **UCI Student Performance** dataset.

Reference dataset:
https://archive.ics.uci.edu/dataset/320/student%2Bperformance

Important: the bundled CSV is **not a copy of the UCI dataset**. It was generated for reproducible offline testing. If the real UCI CSV is used, the notebook can be adapted and the model retrained.

## 3. Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Matplotlib
- Jupyter Notebook
- Joblib
- HTML/CSS/JavaScript

## 4. Project Structure

```text
Sanket_Tarle_Student_Performance_AI/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── student_performance.csv
├── models/
│   └── student_performance_model.joblib
├── notebooks/
│   └── Sanket_Student_Performance_Analysis.ipynb
├── templates/
│   └── index.html
└── static/
    ├── style.css
    ├── script.js
    └── charts/
```

## 5. Setup

### Windows

```bash
cd Sanket_Tarle_Student_Performance_AI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

### Jupyter Notebook

```bash
jupyter notebook
```

Open `notebooks/Sanket_Student_Performance_Analysis.ipynb`.

## 6. Model

The project uses a **Random Forest Regressor**. Categorical features are one-hot encoded and numerical features are standardized through a Scikit-learn `Pipeline`.

Evaluation on the bundled demonstration dataset using an 80/20 train-test split (random_state=42):
- MAE: **0.72**
- RMSE: **0.91**
- R²: **0.759**

These metrics describe this bundled demonstration dataset only; they should not be interpreted as performance on the real UCI dataset.

## 7. Key Features

1. Dataset summary cards
2. Final-grade distribution
3. G2 vs G3 relationship visualization
4. Study-time analysis
5. Model feature-importance visualization
6. Student profile input form
7. Final-grade prediction
8. Simple risk indicator
9. Offline-ready bundled data and trained model

## 8. Limitations

- The bundled dataset is synthetic for offline reproducibility.
- A predicted grade is an estimate, not a guaranteed academic outcome.
- Real deployment would require validation on a real, representative dataset and appropriate privacy controls.

## 9. Future Enhancements

- Connect to a real institutional dataset with permission
- Add SQL database storage
- Add login and role-based access
- Add Power BI integration
- Add model comparison and hyperparameter tuning
- Add explainable-AI methods such as SHAP
- Add automated model monitoring

## 10. Author

**Sanket Shantaram Tarle**  
Third-year BCS / B.Sc. Computer Science student  
K. K. Wagh Arts, Commerce, Science and Computer Science College, Chandori
