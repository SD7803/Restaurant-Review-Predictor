# 🍽️ Restaurant Review & Rating Predictor

### 📖 Overview
The **Restaurant Review Predictor** is a data analysis and machine learning project that explores restaurant data to understand key factors affecting ratings and predicts the **aggregate rating** of a restaurant based on features like **average cost**, **online delivery**, **table booking**, and **price range**.

This project combines **Exploratory Data Analysis (EDA)** with **Machine Learning** techniques to derive business insights and build a predictive model for restaurant ratings.

---

### 🎯 Objective
To analyze restaurant data and develop a model that can **predict restaurant ratings** based on service and pricing attributes, helping businesses understand how different factors influence customer satisfaction.

---

### 📂 Dataset
- **Source:** Zomato restaurant dataset (`data.csv`)  
- **Features used:**
  - `Average Cost for two`
  - `Has Table booking`
  - `Has Online delivery`
  - `Price range`
  - `Aggregate rating`
  - `Rating text`
  - `Votes`
  - `City`
  - `Cuisines`

---

### 🧩 Project Workflow

#### 1️. Data Understanding
- Imported dataset using **Pandas**
- Displayed general info (`.info()`, `.describe()`)
- Checked for missing and duplicate values

#### 2️. Exploratory Data Analysis (EDA)
- **City-wise Average Cost** — visualized using bar plots  
- **Cuisine Votes** — analyzed which cuisines attract more customer votes  
- **Pairplot Analysis** — explored relationships between cost, rating, and votes  
- **Pie Charts** — distribution of online delivery availability and rating text categories  

#### 3️. Data Cleaning
- Removed “Not rated” entries  
- Encoded categorical variables like `Has Table booking` and `Has Online delivery` using **LabelEncoder**

#### 4️. Feature Scaling
- Scaled numerical data using **StandardScaler** for uniformity

#### 5️. Model Building
- Split data into **training** and **testing sets** using `train_test_split`
- Implemented regression models (details can be found in the notebook)
- Used `Aggregate rating` as the target variable (`y`)

#### 6️. Model Evaluation
- Evaluated performance using metrics like **R² Score**, **MAE**, and **RMSE**
- Compared predicted and actual ratings

---
#### 7. Streamlit Web App
Built an interactive **Streamlit dashboard** where users can:
- Input:
  - Average Cost for Two  
  - Price Range (1–4)  
  - Online Delivery (Yes/No)  
  - Table Booking (Yes/No)  
- Get **predicted restaurant rating** as output.

---


### 📊 Key Insights
- Cities with higher average dining costs often received **better ratings**.  
- Restaurants offering **online delivery** and **table booking** tended to have **higher aggregate ratings**.  
- Strong correlation observed between **votes** and **aggregate ratings** — more votes generally indicate higher customer engagement.  

---

### ⚙️ Tech Stack
**Language:** Python  
**Libraries:**  
`pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

---


### 🚀 How to Run Locally

```bash
# Clone this repository
git clone https://github.com/<your-username>/restaurant-rating-predictor.git
cd restaurant-rating-predictor

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

# Run the notebook
jupyter notebook analysis.ipynb
