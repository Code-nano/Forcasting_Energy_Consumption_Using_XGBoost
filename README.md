# Hourly Energy Consumption Forecasting

This is a project which aims to forecast hourly energy consumption based on a dataset obtained from [Kaggle](https://www.kaggle.com/robikscube/hourly-energy-consumption). 

The project can be broken down into the following main steps:

1. **Data collection:** This involves installing all necessary dependencies, importing libraries, setting up paths, and downloading the dataset via the Kaggle API.

2. **Data preprocessing:** This step involves reading the data, setting 'Datetime' as the index, checking the data type for the index and verifying for empty or null values. 

3. **Exploratory Data Analysis (EDA):** This includes visualizing the data to find any abnormalities, creating histograms to visualize data distribution, and querying specific subsets of data. This step also includes the creation of new features based on time such as hour, day, month, year, and day of the week.

4. **Modelling and forecasting:** This involves manually splitting the data into a training and test set, modelling the data using XGBoost, a gradient boosting library designed for speed and performance, and then forecasting energy consumption based on the model.

5. **Time series cross validation:** This involves removing the previous merge, visualizing the time series split, creating lag features and performing cross validation using TimeSeriesSplit for better model performance.

6. **Final forecasting and visualization:** The final model is used to forecast future energy consumption and the results are visualized for better understanding. 

## Prerequisites
This project requires a basic understanding of Python, Pandas, NumPy, Seaborn, Matplotlib, SQL, XGBoost and sklearn libraries. 

You need to have Python (version 3.x) installed on your system. The following Python libraries are also needed: 
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

To install the necessary libraries, you can use pip:

pip install pandas seaborn pansql xgboost scikit-learn ydata-profiling matplotlib numpy zipfile os subprocess

You also need to have the Kaggle API set up on your system for data downloading. You can follow this [guide](https://towardsdatascience.com/downloading-datasets-from-kaggle-for-your-ml-project-b9120d405ea4) to set up the Kaggle API.

## Usage
After you have cloned the project and installed the prerequisites, you can open the Python script in your preferred IDE or notebook environment (Jupyter notebook, PyCharm, VS Code, etc.) and then run the script.

If you're using Jupyter notebook, you can run the script by clicking on 'Cell' and then 'Run All'.


## Acknowledgments
* Special thanks to [Kaggle](https://www.kaggle.com/) for providing the dataset.
* This project uses the XGBoost library. Special thanks to the creators of [XGBoost](https://xgboost.readthedocs.io/). 
