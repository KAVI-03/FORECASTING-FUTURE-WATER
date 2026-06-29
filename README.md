# FORECASTING-FUTURE-WATER

# 🌊 Forecasting Future Water Requirements and Assessing Storage Capacities in Reservoirs


An end-to-end Machine Learning project for predicting 7-day ahead water levels across Chennai's four major reservoirs — built to support smarter water resource planning.




# 📌 Project Overview

Chennai, one of India's most water-stressed cities, depends heavily on four reservoirs — Poondi, Cholavaram, Red Hills, and Chembarambakkam — for its water supply. Erratic monsoons, rapid urbanization, and climate variability make accurate water-level forecasting critical for city planners, water boards, and disaster management teams.

This project applies supervised Machine Learning on 16 years of hydrological data (2004–2020) to:


Forecast total reservoir water levels 7 days into the future
Assess how close storage capacities are to their limits
Provide an interactive web app for real-time forecast queries



# 🎯 Objectives


Predict the combined 7-day-ahead water level (in MCft) across all four Chennai reservoirs
Identify which rainfall and historical level patterns most influence future storage
Compare multiple ML models and deploy the best-performing one
Visualize forecast results with actionable status indicators (critical / low / moderate / good / full)



# 🏗️ Project Architecture

├── Chennai_Reservoir_ML_Project_college.ipynb   ← Model training pipeline (Google Colab)
├── app.py                                        ← Streamlit web app (HydroSense dashboard)
├── best_model.pkl                                ← Trained model (generated after running notebook)
├── scaler.pkl                                    ← Fitted StandardScaler
├── chennai_reservoir_levels.csv                  ← Raw levels dataset (2004–2020)
├── chennai_reservoir_rainfall.csv                ← Raw rainfall dataset (2004–2020)
└── README.md

# 📊 Dataset

FileDescriptionchennai_reservoir_levels.csvDaily water levels (MCft) for all 4 reservoirschennai_reservoir_rainfall.csvDaily rainfall (mm) for all 4 reservoir catchment areas

Reservoirs covered: Poondi · Cholavaram · Red Hills · Chembarambakkam

Time span: 2004 – 2020 (~5,900+ daily records)

Source: Chennai Metropolitan Water Supply & Sewerage Board (CMWSSB)


# 🧠 Machine Learning Pipeline

1. Exploratory Data Analysis


Distribution plots for each reservoir's water level
Correlation heatmaps (levels vs. rainfall)
Time-series trend visualization of total storage


2. Feature Engineering

FeatureDescriptionTOTAL_LEVELSum of levels across all 4 reservoirsTOTAL_RAINFALLSum of rainfall across all 4 catchmentsLag_7_levelTotal water level 7 days agoLag_30_levelTotal water level 30 days agoRoll_7_rain_mean7-day rolling mean of rainfallRoll_30_rain_mean30-day rolling mean of rainfallRoll_7_level_std7-day rolling std of water levelMonth_sin / Month_cosCyclical seasonal encodingDay_sin / Day_cosCyclical day-of-year encodingYear, Quarter, DayOfYearCalendar features

3. Model Training & Comparison

The following models were trained and evaluated using a chronological 80/20 train-test split (no shuffle, respecting time-series order):

ModelTypeLinear RegressionBaselineRidge / LassoRegularized linearDecision TreeTree-basedRandom ForestEnsembleGradient BoostingEnsembleExtra TreesEnsembleXGBoostGradient BoostingSVRKernel-based

Evaluation Metrics: MAE · RMSE · R² Score

4. Best Model

The best-performing model is saved as best_model.pkl and used directly by the Streamlit app for live predictions.


# 🖥️ Web Application — HydroSense

The project ships with HydroSense, a fully interactive Streamlit dashboard for 7-day reservoir forecasting.

Features


Input current rainfall levels per reservoir via sliders
Input lag water levels and rolling averages
Instant 7-day forecast output with capacity percentage
Status indicator: 🔴 Critical → 🟠 Low → 🟡 Moderate → 🟢 Good → 💧 Full
Works in Demo Mode even without model files


# Run the App

bash# Install dependencies
streamlit 
scikit-learn 
xgboost 
joblib 
numpy 
pandas




# 🔁 How to Reproduce

Step 1 — Train the model (Google Colab)


Upload chennai_reservoir_levels.csv and chennai_reservoir_rainfall.csv to your Google Drive
Open Chennai_Reservoir_ML_Project_college.ipynb in Google Colab
Run all cells — the notebook will train all models, compare them, and export best_model.pkl + scaler.pkl


Step 2 — Run the web app (locally)


Place best_model.pkl, scaler.pkl, and app.py in the same folder
Run streamlit run app.py



# 📦 Dependencies

numpy
pandas
scikit-learn
xgboost
matplotlib
seaborn
streamlit
joblib

# Install all at once:

pip install numpy pandas scikit-learn xgboost matplotlib seaborn streamlit joblib


# 📈 Results Summary


Target variable: Total 7-day-ahead reservoir level (MCft)
Total reservoir capacity: ~320 MCft (combined across all 4 reservoirs)
Best model selected by lowest RMSE on the held-out chronological test set
Feature importance analysis reveals lag features and rolling rainfall averages as top predictors



# 🏫 Academic Context

FieldDetailProject TitleForecasting Future Water Requirements and Assessing Storage Capacities in ReservoirsBatchIII AIML – A (2028 Batch)DomainHydrology · Water Resource Management · Machine LearningStackPython · Scikit-learn · XGBoost · StreamlitData Period2004 – 2020


# 🔮 Future Scope


Integrate real-time data from CMWSSB APIs for live forecasts
Extend to LSTM / Transformer-based deep learning for longer-horizon predictions
Add multi-output forecasting (individual reservoir levels instead of total)
Build a mobile-friendly PWA version of HydroSense
Deploy on cloud (AWS / GCP / Hugging Face Spaces)


# 🚀 Live Demo


Try the app here: https://forecasting-future-water-fiatv6gcczwgqgchnvhb8m.streamlit.app/
