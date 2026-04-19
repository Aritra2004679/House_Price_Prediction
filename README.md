# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project aims to predict house prices using Machine Learning techniques. It involves data preprocessing, model training, evaluation, and deployment using a web-based interface.

The model is trained on real-world housing data and deployed using Streamlit to provide real-time predictions based on user input.

---

## 🚀 Features

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Multiple model training and comparison
* High-accuracy prediction using XGBoost
* Feature importance analysis
* Interactive web application using Streamlit
* Real-time price prediction in USD and INR

---

## 🧠 Technologies Used

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* XGBoost
* Streamlit

---

## 📊 Model Performance

| Model             | MAE        | R² Score  |
| ----------------- | ---------- | --------- |
| Linear Regression | 21,230     | 0.848     |
| Random Forest     | 17,512     | 0.900     |
| **XGBoost**       | **16,178** | **0.915** |

👉 XGBoost achieved the best performance and was selected for deployment.

---

## 📁 Project Structure

```
HOUSE_PRICE_PREDICTION/
│
├── data/
│   ├── dataset.csv
│   └── cleaned_dataset.csv
│
├── notebooks/
│   ├── eda.ipynb
│   └── model.ipynb
│
├── model/
│   └── house_price_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone <your-repo-link>
cd HOUSE_PRICE_PREDICTION
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the application

```
streamlit run app.py
```

---

## 🖥️ Usage

* Enter house feature values in the sidebar
* Click on **Predict Price**
* The app will display:

  * Estimated price in USD 💵
  * Converted price in INR 🇮🇳

---

## 📈 Feature Importance

Feature importance analysis was performed using XGBoost to understand which factors influence house prices the most.

Key influential features include:

* Overall Quality
* Living Area (GrLivArea)
* Garage Capacity
* Basement Area

---

## 🎓 Learning Outcomes

* Practical implementation of ML algorithms
* Data preprocessing and feature engineering
* Model evaluation using MAE and R² score
* Model deployment using Streamlit
* Building end-to-end ML applications

---

## 🔮 Future Enhancements

* Improve UI with dropdowns and sliders
* Hyperparameter tuning for better accuracy
* Deployment on cloud platforms
* Integration with real-time data APIs

---

## 👨‍💻 Author

**Aritra Chakraborty**

---

## 📜 License

This project is for educational purposes.
