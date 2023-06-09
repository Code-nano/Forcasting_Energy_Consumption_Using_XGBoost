# Energy Consumption Forecasting Using XGBoost

This project aims to forecast hourly energy consumption using a dataset from [Kaggle](https://www.kaggle.com/robikscube/hourly-energy-consumption). 

### The dataset is Hourly Power Consumption Statistics from PJM
PJM Interconnection LLC (PJM), a key Regional Transmission Organization (RTO) within the United States, forms an integral part of the Eastern Interconnection grid. It administers an electric transmission system that caters to various parts or the entirety of several states and territories, including Delaware, Illinois, Indiana, Kentucky, Maryland, Michigan, New Jersey, North Carolina, Ohio, Pennsylvania, Tennessee, Virginia, West Virginia, and the District of Columbia.

The hourly power consumption data comes from PJM's website and are in megawatts (MW)

The dataset
![image](https://github.com/Code-nano/Forcasting_Energy_Consumption_Using_XGBoost/assets/83939407/7590f003-207a-4e38-b637-fc5a0c5f825e)

TimeSeriesSplit
![image](https://github.com/Code-nano/Forcasting_Energy_Consumption_Using_XGBoost/assets/83939407/73d889a9-e200-4771-86d7-e5dace7e24bf)

Sample of 1 year span energy consumption
![image](https://github.com/Code-nano/Forcasting_Energy_Consumption_Using_XGBoost/assets/83939407/5fa7be86-ba72-47ce-b2ab-3866da719d7c)

Forecast for the next year after the end of dataset
![image](https://github.com/Code-nano/Forcasting_Energy_Consumption_Using_XGBoost/assets/83939407/c8c275f3-fa4a-4006-97bd-0325d980d9ea)


## The project can be broken down into the following main steps:

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
```bash
pip install pandas seaborn pansql xgboost scikit-learn ydata-profiling matplotlib numpy zipfile os subprocess
```
You also need to set up the Kaggle API on your system for data downloading. You can follow this [guide](https://towardsdatascience.com/downloading-datasets-from-kaggle-for-your-ml-project-b9120d405ea4) to set up the Kaggle API.

## Usage
After you have cloned the project and installed the prerequisites, you can open the Jupyter notebook and run the notebook

## Acknowledgments
*  I'd also like to thank Rob Mulla for the foundational knowledge and basic techniques used for this project's time series forecasting
*  This project uses the XGBoost library. Special thanks to the creators of [XGBoost](https://xgboost.readthedocs.io/). 
* Dataset from 
Rob Mulla. 2018. Hourly Energy Consumption, Version 1. Retrieved May 2023 from https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption.
