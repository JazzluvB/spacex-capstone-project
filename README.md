[github_repository_readme.md](https://github.com/user-attachments/files/34394922/github_repository_readme.md)
# 🚀 SpaceX Falcon 9 First Stage Landing Prediction
### IBM Applied Data Science Capstone Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)
![Plotly Dash](https://img.shields.io/badge/Plotly_Dash-Interactive_Dashboard-008080.svg)
![Folium](https://img.shields.io/badge/Folium-Geospatial_Analysis-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database_Analysis-003B57.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

---

## 📌 Executive Summary
SpaceX advertises Falcon 9 rocket launches on its website with a cost of **$62 million**; other providers cost upward of **$165 million** each. Much of the savings is due to SpaceX's ability to reuse the first stage. Therefore, determining if the first stage will land successfully allows us to calculate the actual cost of a launch. 

This project applies an end-to-end Data Science pipeline—from raw data extraction via APIs and Web Scraping to interactive dashboards and machine learning models—to predict whether the Falcon 9 first stage will land successfully.

---

## 🛠️ Data Science Workflow & Methodology

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Data Collection │ ──►│ Data Wrangling  │ ──►│       EDA       │
│ (API & Scraping)│    │ & Preprocessing │    │  (SQL & Pandas) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
┌─────────────────┐    ┌─────────────────┐             ▼
│ Machine Learning│ ◄──│ Dashboards      │ ◄──┌─────────────────┐
│ (83.33% Acc.)   │    │ (Plotly Dash)   │    │ Spatial Maps    │
└─────────────────┘    └─────────────────┘    │ (Folium Maps)   │
                                              └─────────────────┘
```

### 1. Data Collection & Preprocessing
* **API Extraction:** Pulled historic launch data from the official SpaceX API (`https://api.spacexdata.com/v4/launches/past`).
* **Web Scraping:** Scraped Wikipedia's Falcon 9 launch history tables using `BeautifulSoup` to validate payload capacity and mission details.
* **Data Wrangling:** Filtered records strictly for Falcon 9 cores, handled missing values in `PayloadMass` by imputing column means, and engineered the target binary label `Class` (1 = successful recovery, 0 = failed landing/unrecovered).

### 2. Exploratory Data Analysis (EDA) & SQL
* **Visual Analysis (Seaborn/Matplotlib):** Evaluated correlations between `FlightNumber`, `PayloadMass`, `LaunchSite`, and target `Orbit`.
* **SQL Aggregation (SQLite):** Calculated summary statistics including total payload mass transported for specific customers (e.g., NASA CRT = 45,596 kg), launch frequency per site, and success rates across booster versions.

### 3. Geospatial Analysis (Folium)
* Mapped all operational launch sites (`CCAFS LC-40`, `KSC LC-39A`, `VAFB SLC-4E`, `CCAFS SLC-40`) with interactive markers and clusters using `MarkerCluster`.
* Calculated geodesic distances to nearby coastlines, railways, and highways, establishing that launch sites are strategically located within **1.5 km of the coast** for public safety.

### 4. Interactive Dashboard (Plotly Dash)
* Built a dynamic web application containing:
  * A `dcc.Dropdown` selector to filter global launches vs. specific sites.
  * A `dcc.RangeSlider` to filter payloads from 0 kg to 10,000 kg.
  * Reactive `@app.callback` components rendering live Pie Charts and Payload vs. Outcome Scatter Plots.

### 5. Machine Learning & Predictive Modeling
* Standardized features using `StandardScaler` after One-Hot Encoding categorical features (expanding to 80 feature columns).
* Split dataset into training and testing sets (80/20 ratio: **18 test samples**).
* Hyperparameter optimization conducted via 10-fold cross-validation (`GridSearchCV`).

---

## 📊 Machine Learning Model Evaluation Results

All four classification algorithms yielded strong performance on the unseen testing set (`Y_test`), achieving a **83.33% accuracy score**.

| Classification Model | Best Hyperparameters | CV Train Accuracy | Test Accuracy |
| :--- | :--- | :---: | :---: |
| **Decision Tree Classifier** | `criterion: 'gini'`, `splitter: 'best'` | **84.82%** | **83.33%** |
| **Support Vector Machine (SVM)** | `kernel: 'rbf'`, `C: 1.0` | **84.82%** | **83.33%** |
| **Logistic Regression** | `C: 0.01`, `penalty: 'l2'` | **84.64%** | **83.33%** |
| **K-Nearest Neighbors (KNN)** | `n_neighbors: 4`, `algorithm: 'auto'` | **84.82%** | **83.33%** |

### 🔍 Confusion Matrix Highlights (Test Set - 18 Samples)
* **True Positives (TP):** 12 successful landings correctly predicted.
* **True Negatives (TN):** 3 landing failures correctly predicted.
* **False Positives (FP):** 3 landing failures predicted as success.
* **False Negatives (FN):** 0 missed landings (100% Sensitivity/Recall for successful landings).

---

## 📁 Repository File Structure

```
.
├── Data/
│   ├── dataset_spacex_api.csv          # Raw data collected via API
│   ├── dataset_spacex_web_scraped.csv  # Raw data collected via BeautifulSoup
│   └── dataset_falcon9_cleaned.csv     # Wrangled final dataset
├── Notebooks/
│   ├── 1_SpaceX_Data_Collection_API.ipynb
│   ├── 2_SpaceX_Web_Scraping.ipynb
│   ├── 3_SpaceX_Data_Wrangling.ipynb
│   ├── 4_SpaceX_EDA_SQL.ipynb
│   ├── 5_SpaceX_EDA_Visualizations.ipynb
│   ├── 6_SpaceX_Folium_Geospatial_Maps.ipynb
│   └── 7_SpaceX_Machine_Learning_Prediction.ipynb
├── Dash_App/
│   └── spacex_dash_app.py              # Interactive Plotly Dash python script
├── Reports/
│   └── Presentacion_Final_SpaceX.pdf   # Complete Presentation PDF for Capstone Submission
├── README.md                           # Project Overview
└── requirements.txt                    # Python environment dependencies
```

---

## ⚙️ How to Run locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JazzluvB/spacex-capstone-project.git
   cd spacex-capstone-project
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Plotly Dash Application:**
   ```bash
   python Dash_App/spacex_dash_app.py
   ```
   *Open your browser and navigate to `http://127.0.0.1:8050/`*

---

## 👨‍💻 Author
**Carlos Palacios Betancourt**  
*Data & AI Professional*  
GitHub: [@JazzluvB](https://github.com/JazzluvB)  
Certified: **IBM Applied Data Science Capstone**
