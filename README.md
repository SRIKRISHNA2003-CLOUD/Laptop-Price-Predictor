# 💻 Laptop Price Predictor

A machine learning web application that predicts the approximate price of a laptop based on its specifications such as brand, laptop type, RAM, weight, screen size, screen resolution, CPU, storage, GPU, operating system, touchscreen, and IPS display.

Several regression models were evaluated during the project. Random Forest was selected as the final model used in the Streamlit application, achieving an **R² score of approximately 0.887** on the test data.

## 🚀 Live Demo

https://srikrishna2003-cloud-laptop-price-predictor-app-92t5md.streamlit.app/


## 📌 Problem Statement

Laptop prices vary significantly depending on hardware specifications, brand, display characteristics, storage, processor, GPU, and other features.

The objective of this project is to build a machine learning model that can estimate the price of a laptop based on its specifications.

---

## 📊 Dataset

The project uses a laptop dataset containing information about laptop specifications and their prices.

**Dataset file:**

```text
laptop_data.csv
```

---

## 🔎 Exploratory Data Analysis

### 1. Univariate Analysis

The following visualizations were used to understand individual variables:

* Bar chart to analyze the number of laptop brands in the dataset
* Pie chart to analyze different laptop types such as Notebook, Gaming, Netbook, etc.
* KDE plot to understand the distribution of laptop screen sizes
* KDE plot to analyze the distribution of laptop prices

### 2. Bivariate Analysis

The following visualizations were used to study relationships between variables:

* Column chart to analyze price variation across different laptop companies
* Scatter plot to analyze the relationship between screen size and laptop price
* Column chart to analyze price variation across different CPU brands

---

## ⚙️ Feature Engineering

Several features were extracted and transformed before training the machine learning models.

### Data Cleaning

* Removed unnecessary units such as `GB` and `kg`
* Converted relevant columns into appropriate numerical formats
* Reduced and standardized memory/storage information

### Feature Extraction

From the `ScreenResolution` column:

* Extracted whether the laptop has a touchscreen
* Extracted whether the display has IPS
* Calculated **PPI (Pixels Per Inch)** from screen resolution and screen size

From the `CPU` column:

* Extracted important CPU categories such as:

  * Intel Core i3
  * Intel Core i5
  * Intel Core i7
  * AMD

From the `Memory` column:

* Extracted SSD storage
* Extracted HDD storage
* Extracted Hybrid storage
* Extracted Flash storage

From the `GPU` column:

* Extracted NVIDIA
* Extracted Intel
* Extracted AMD

From the `OS` column:

* Extracted Windows
* Extracted macOS
* Extracted Linux/Other

### Target Transformation

A logarithmic transformation was applied to the price variable to improve the behavior of the regression models.

---

## 🤖 Machine Learning Models & Performance

Multiple regression algorithms were evaluated.

| Model              | R² Score |    MAE |
| ------------------ | -------: | -----: |
| Linear Regression  |   0.8073 | 0.2102 |
| Lasso Regression   |   0.8072 | 0.2111 |
| Ridge Regression   |   0.8127 | 0.2093 |
| KNN                |   0.8018 | 0.1935 |
| Decision Tree      |   0.8345 | 0.1849 |
| SVM                |   0.8083 | 0.2024 |
| Random Forest      |   0.8873 | 0.1586 |
| Extra Trees        |   0.8754 | 0.1598 |
| AdaBoost           |   0.7998 | 0.2283 |
| Gradient Boosting  |   0.8828 | 0.1592 |
| XGBoost            |   0.8771 | 0.1626 |
| Stacking Regressor |   0.8805 | 0.1653 |
| Voting Regressor   |   0.8896 | 0.1570 |

### Final Model

Random Forest was selected for the final Streamlit application.

The model achieved:

```text
R² Score: 0.8873
MAE:      0.1586
```

The target variable was log-transformed during training, so the prediction is converted back to the original price scale using the exponential function.

---

## 🖥️ Streamlit Application

The application allows users to enter laptop specifications and receive an estimated laptop price.

### User Inputs

* Brand
* Laptop type
* RAM
* Weight
* Touchscreen
* IPS display
* Screen size
* Screen resolution
* CPU
* HDD storage
* SSD storage
* GPU
* Operating system

The application calculates PPI from the selected screen resolution and screen size before sending the features to the trained machine learning pipeline.

### Prediction

After clicking **Predict Price**, the application displays the estimated laptop price.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Pickle

---

## 📁 Project Structure

```text
Laptop-Price-Predictor/
│
├── app.py
├── pipe.pkl
├── df.pkl
├── laptop_data.csv
├── requirements.txt
├── runtime.txt
├── README.md
│
└── Laptop_price_predictor.ipynb
```

> Include only the files that actually exist in your repository. If `df.pkl` or `laptop_data.csv` is not required by the application, you can adjust the structure accordingly.

---

## ⚡ Installation

### 1. Clone the repository

```bash
git clone https://github.com/SRIKRISHNA2003-CLOUD/Laptop-Price-Predictor.git
```

```bash
cd Laptop-Price-Predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

## 📸 Screenshots

Add screenshots of:

1. Home page
2. Laptop specification inputs
3. Prediction result

Example:

```text
![Laptop Price Predictor](screenshots/home.png)
```

---

## 🔮 Future Improvements

* Add more recent and real-world laptop data
* Add laptop search and filtering
* Add additional laptop specifications
* Improve model performance with hyperparameter tuning
* Add model explainability
* Add price comparison between different laptop configurations
* Add a laptop recommendation feature

---

## 👨‍💻 Author

**Srikrishna Samanta**

GitHub:
`https://github.com/SRIKRISHNA2003-CLOUD`

---

## ⭐ If you find this project useful

Feel free to explore the repository and use the project as a reference for learning machine learning and Streamlit deployment.
