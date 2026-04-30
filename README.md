# 🌊 Flood Warning System (Early Detection)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-XGBoost%20%7C%20RandomForest-green)](https://github.com/Mustafa2397)

## 📝 Project Overview
This project aims to develop a robust **Early Flood Warning System** using historical meteorological time-series data. The system analyzes factors like precipitation and temperature to predict flood risk levels, helping in disaster mitigation and early response.

## 🚀 Key Features
*   **Time-Series Analysis:** Processing daily weather data from 1971 to 2095.
*   **Advanced Data Cleaning:** Handling outliers in temperature and precipitation records.
*   **Feature Engineering:** Implementation of derived metrics like Temperature Range.
*   **Multi-Model Comparison:** Evaluated several ML algorithms to find the most accurate predictive model.

## 📊 Dataset Description
The dataset contains **913,488 records** with the following features:
*   `Precipitation_mm`: Daily rainfall.
*   `Tasmax_C`, `Tasmin_C`, `Tasmean_C`: Temperature variations.
*   `Flood_Risk`: The target variable (0: No Risk, 1: Moderate, 2: High).

## 📈 Model Performance
| Model | Accuracy |
| :--- | :--- |
| **XGBoost** | **92.71%** |
| **Random Forest** | **92.70%** |
| **Logistic Regression** | **92.50%** |
| **Decision Tree** | **87.32%** |

## 🛠️ Tech Stack
*   **Language:** Python
*   **Libraries:** Pandas, NumPy, Scikit-Learn, XGBoost, Matplotlib, Seaborn.

## 👨‍💻 Author
**Mustafa Zalam**  
*AI & Data Scientist*  
[LinkedIn](https://www.linkedin.com/in/mustafa-zalam) | [GitHub](https://github.com/Mustafa2397)
