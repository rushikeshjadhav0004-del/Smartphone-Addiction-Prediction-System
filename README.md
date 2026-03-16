# 📱 Smartphone Addiction Prediction System

## 📌 Project Overview

The **Smartphone Addiction Prediction System** is a Machine Learning based application that analyzes smartphone usage behavior and predicts whether a user is at **high risk of smartphone addiction**.

The project uses behavioral metrics such as screen time, social media usage, gaming hours, sleep patterns, notifications, and stress levels to detect addiction risk.

A **Streamlit-based interactive web application** allows users to input their daily smartphone usage habits and instantly receive a prediction.

---

## 🚀 Features

* Predicts smartphone addiction risk using Machine Learning
* Interactive web interface for user input
* Real-time prediction results
* Behavioral feature analysis
* Clean and simple dashboard using Streamlit
* End-to-end ML workflow (data preprocessing → model training → deployment)

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Serialization using Pickle
8. Deployment using Streamlit

---

## 📊 Dataset Features

The model uses the following behavioral features:

* Age
* Gender
* Daily Screen Time (hours)
* Social Media Usage (hours)
* Gaming Hours
* Work / Study Hours
* Sleep Hours
* Notifications Per Day
* App Opens Per Day
* Weekend Screen Time
* Stress Level
* Academic / Work Impact

Target Prediction:

* Smartphone Addiction Risk (High / Low)

---

## 🛠 Technologies Used

| Technology           | Purpose                |
| -------------------- | ---------------------- |
| Python               | Core Programming       |
| Pandas               | Data Processing        |
| NumPy                | Numerical Operations   |
| Scikit-learn         | Machine Learning Model |
| Streamlit            | Web Application        |
| Matplotlib / Seaborn | Data Visualization     |
| Pickle               | Model Serialization    |

---

## 📂 Project Structure

```
Smartphone-Addiction-Prediction/
│
├── app.py
├── addiction_model.pkl
├── Smartphone_Usage_And_Addiction_Analysis_7500_Rows.csv
├── Smartphone_usage_and_Addiction.ipynb
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/smartphone-addiction-prediction.git
```

### 2️⃣ Navigate to Project Folder

```
cd smartphone-addiction-prediction
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```
streamlit run app.py
```

---

## 💻 Application Interface

The application allows users to enter their smartphone usage details such as:

* Screen time
* Social media hours
* Gaming hours
* Sleep hours
* Notifications per day
* Stress level

The system then predicts the **risk level of smartphone addiction**.

---

## 📈 Future Improvements

* Deploy the application on cloud platforms
* Add advanced ML models for higher accuracy
* Implement user analytics dashboard
* Add real-time usage tracking
* Mobile responsive interface

---

## 🎯 Project Objective

The main goal of this project is to **analyze smartphone usage patterns and identify addiction risk using data-driven insights**, helping users become aware of their digital habits.

---

## 👨‍💻 Author

**Rushikesh Jadhav**

Aspiring Data Scientist | Machine Learning Enthusiast
