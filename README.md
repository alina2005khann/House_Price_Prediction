# House Price Prediction

A machine learning application that estimates Bengaluru house prices from property details. The project includes the data-cleaning and exploratory-analysis notebooks, the trained prediction model, and a Streamlit interface for interactive predictions.

## Live Demo

Try the deployed Streamlit app:

[Open the House Price Prediction app](https://alina-house-price-app.streamlit.app/)

## Dashboard Preview

![House Price Prediction dashboard](dashboard.png.png)

## Features

- Predicts an estimated house price in Indian lakh (`₹ Lakh`)
- Interactive Streamlit dashboard
- Uses saved machine learning model artifacts for fast predictions
- Supports property inputs for:
  - Area type
  - Availability
  - Location
  - BHK size
  - Total area in square feet
  - Number of bathrooms
  - Number of balconies
- Includes notebooks covering data cleaning, preprocessing, EDA, and model interface development

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook
- Pickle model and feature artifacts

## Project Structure

```text
.
├── 1.Data cleaning .ipynb
├── 2.Data preprocessing.ipynb
├── 3.perform EDA.ipynb
├── 4.House_price_prediction_ml_interface.ipynb
├── app_stream.py                         # Streamlit application
├── app.py                                # Gradio application
├── model_Final.pkl                       # Trained model
├── locations.pkl                         # Location options
├── area_type.pkl                         # Area type options
├── avalibility.pkl                       # Availability options
├── Module 2 Bengaluru_House_Data.csv     # Raw dataset
├── House_Cleaned_data.csv                # Cleaned dataset
├── data_preprocess_for_ml.csv            # Model-ready dataset
├── dashboard.png.png                     # Dashboard screenshot
└── requirements.txt
```

## Run Locally

1. Clone or download this repository and open a terminal in the project directory.

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Streamlit application:

   ```bash
   streamlit run app_stream.py
   ```

5. Open the local URL displayed by Streamlit, usually `http://localhost:8501`.

## How It Works

The application loads the trained model and the saved categorical-value lists from the `.pkl` files. After the user enters the property details, the values are assembled into a Pandas DataFrame with the same feature names used during training. The model then generates an estimated price, which is displayed in Indian lakh.

## Data and Model Workflow

1. Clean the Bengaluru house-price dataset.
2. Explore the data and identify useful property features.
3. Preprocess the data for machine learning.
4. Train and save the prediction model and categorical feature artifacts.
5. Use the Streamlit interface to make predictions interactively.

## Notes

- The prediction is an estimate and should not be treated as a formal property valuation.
- The model expects the saved `.pkl` files to remain in the same directory as `app_stream.py`.
- The Streamlit app is the recommended entry point for this project.
