# Hourly Energy Consumption Forecasting

This project aims to forecast hourly energy consumption using a dataset from [Kaggle](https://www.kaggle.com/robikscube/hourly-energy-consumption). 
The dataset
![image](https://github.com/Code-nano/Forcasting_Energy_Consumption_Using_XGBoost/assets/83939407/7590f003-207a-4e38-b637-fc5a0c5f825e)
TimeSeriesSplit
![image](https://github.com/Code-nano/Forcasting_Energy_Consumption_Using_XGBoost/assets/83939407/73d889a9-e200-4771-86d7-e5dace7e24bf)
Forecast for the next year
![image](https://github.com/Code-nano/Forcasting_Energy_Consumption_Using_XGBoost/assets/83939407/c8c275f3-fa4a-4006-97bd-0325d980d9ea)


The project can be broken down into the following main steps:

1. **Data collection:** This involves installing all necessary dependencies, importing libraries, setting up paths, and downloading the dataset via the Kaggle API.

2. **Data preprocessing:** This step involves reading the data, setting 'Datetime' as the index, checking the data type for the index and verifying for empty or null values. 

3. **Exploratory Data Analysis (EDA):** This includes visualising the data to find any abnormalities, creating histograms to visualise data distribution, and querying specific subsets of data. This step also consists of creating new features based on time, such as hour, day, month, year, and day of the week.

4. **Modelling and forecasting:** This involves manually splitting the data into a training and test set, modelling the data using XGBoost, a gradient boosting library designed for speed and performance, and then forecasting energy consumption based on the model.

5. **Time series cross-validation:** This involves removing the previous merge, visualising the time series split, creating lag features and performing cross-validation using TimeSeriesSplit for better model performance.

6. **Final forecasting and visualisation:** The final model is used to forecast future energy consumption, and the results are visualised for better understanding. 

Note: New features need to be added, as well as the implementation for the automation for the XGBoost model hyperparameter tuning for a more accurate model. 
Such as temporal factors: time of day, seasons and weather, dayofweek
or special events and holidays
and even macroeconomic factors

## Prerequisites
This project requires a basic understanding of Python, Pandas, NumPy, Seaborn, Matplotlib, SQL, XGBoost and sklearn libraries. 

You'll need to install Python (version 3. x) on your system. The following Python libraries are also required: 
* pandas
* seaborn
* pansql
* xgboost
* scikit-learn
* ydata-profiling
* matplotlib
* NumPy
* zipfile
* os
* subprocess

To install the necessary libraries, you can run the .ipynb or use pip:
'''bash
pip install pandas seaborn pansql xgboost scikit-learn ydata-profiling matplotlib numpy zipfile os subprocess
'''
You also need to set up the Kaggle API on your system for data downloading. You can follow this [guide](https://towardsdatascience.com/downloading-datasets-from-kaggle-for-your-ml-project-b9120d405ea4) to set up the Kaggle API.

## Usage
After you have cloned the project and installed the prerequisites, you can open the 

If you're using Jupyter notebook, you can run the script by clicking on 'Cell' and then 'Run All'.


## Acknowledgments
* Special thanks to [Kaggle](https://www.kaggle.com/) for providing the dataset.
* This project uses the XGBoost library. Special thanks to the creators of [XGBoost](https://xgboost.readthedocs.io/). 
