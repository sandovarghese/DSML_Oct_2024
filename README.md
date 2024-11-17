# Retail Sales Prediction with Machine Learning
 


Introduction

To be successful in today’s competent business world, retail store needs to forecast some attributes, so that they can maximize the sales and profit like inventory required, need to running campaigns and ads, financial planning, etc. Here, I am going to walk you through the process of setting up a forecasting model using machine learning to predict the sales. We’ll explore the data, do feature engineering, build a model and evaluate the same using python.

Project Goal

Our goal is to predict sales for retail stores based on historical data provided, with the help of various factors like store type, location, promotional activities, and trends (e.g., holidays, seasons). This will enable the management to make data-driven decisions on financial planning, inventory, marketing, and operations.

Data Overview

Data set provided consist of following features:

•	Store ID		: Unique ID for each store
•	Store Type		: Classification based on the type of store
•	Location Type	: Classification based on the type of location like cities, metro, etc.
•	Region Code		: Geographical region code for the store
•	Date			: Date of sales
•	Holiday		: Indicator of holiday or non-holiday
•	Discount		: Whether a discount was offered on a given day or whether   promotional activities were carried out on the given day
•	#Orders		: Number of orders received by the store
•	Sales			: Total sales amount for each day (Target)

Insight from Data Overview

1.	There are 188340 number of order data
2.	There are 4 Store types, 5 Locations, 4 regions in the Data
3.	The data starts from 01-01-2018 to 31-5-2019
4.	Most orders are from S1, L1, R1
5.	Highest sales value is 247215
6.	No duplicate values, hence removal of duplicate value step can be avoided
7.	No missing values in Data, hence missing value treatment step can be avoided


1.	Exploratory Data Analysis

Primary step is to understand the characteristics of data, and to identify features that influence sales
	
a.	Univariate Analysis
	We explored distributions for each feature, particularly Sales and #Orders, using histograms and box plots to check for outliers. Here’s what we found:
i.	Sales showed some high outliers, indicating that certain days had very high sales.
ii.	The distribution of #Orders suggested a positive correlation with Sales, which makes sense intuitively.
b.	Bivariate Analysis
	Using correlation matrices, we examined relationships between features:
i.	Discount and Sales: Sales were significantly higher on discount days.
ii.	Holiday and Sales: Surprisingly, sales tended to be lower on holidays.
c.	Feature Engineering

i.	New feature the derived from date column, which are day, month and year.
Note. Outliers are not removed because sales value outlier can be true and real as the trend on promotional regular day is high. 


2.	Hypothesis Testing
To check the statistical impact of promotional activities, holiday, store type, and region on sales, we have done hypothesis testing and found the following result:
a.	T- Test result for discounts on sales: 
•	 High T-statistic suggests mean sales on days with promotional activities are done is high.
•	P-value is below 0.05
b.	T- Test result for holidays on sales: 
•	 Low T-statistic suggests mean sales on holidays are less.
•	P-value is below 0.05
c.	ANOVA test result for sales by store type:
•	High F-statistic value suggest sale in some store is much higher compared to others.
•	P-value is below 0.05
d.	ANOVA test result for sales by region:
•	High F-statistic value suggest sale in some region is much higher compared to others.
•	P-value is below 0.05

3.	Machine Learning Model
From all of the above insights, we proceed to build a sales predicting model using ML
a.	Data Preprocessing
•	Extracting year, month, day from the Date to capture the trends.
•	Encoding and scaling - one-hot encoding is used for categorical variables (like store type) and scaled numerical features.

b.	Model Selection

We tried several models to predict the sales, like Linear regression, Random Forest, etc.
•	All the models performed well
•	XGBoost Regressor out preformed all with high accuracy.

c.	Model Evaluation 

Each model was evaluated using R Score, Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) on the test set. Here’s how the models performed:

•	Linear Regression: R2=0.54, MAE = 8681, RMSE = 12366
•	Random Forest: R2=0.71, MAE = 6730, RMSE = 9870
•	XGBoost: R2=0.71, MAE = 6922, RMSE = 9936

Random Forest and XGBoost gave the best R2 results, smallest error in prediction, capturing the nuances of the data better than the other models.

d.	Model Tuning

Model tuning is performed on both RF Model and XGBoost model. After the tuning models are evaluated, their results are:

•	Random Forest: R2=0.77, MAE = 6054, RMSE = 8650
•	XGBoost: R2=0.83, MAE = 5129, RMSE = 7420
		Hence, we are opting XGBoost model for prediction.
4.	Deployment

a.	Saving the Model
To deploy the model for prediction, we have to save the model. Here, we are using pickle for that.

b.	Web App
After saving the model, we can create a streamlit app to allow users to input the feature, so that model can predict the sales for given future date.

5.	Recommendations
	Since, data proves that discounts boost sales, as well as sales on holidays are on lower side, and some regions and store type contribute more to sales.
1.	Promotional activities – discounts and offers can be run on low sales non – holiday days
2.	Holiday days – management can more concentrate on other activities like maintenance work, upgradations, etc on these days
3.	Inventory - more inventory can be diverted to stores and region where there are more sales. Inter stock transfer of nearing to expiry goods can be done to store with high sale.

6.	Conclusion

This project demonstrates the power of machine learning in predicting retail sales. I have covered everything from EDA and hypothesis testing to model selection, evaluation, and deployment. The insights and recommendation provided can help retailers optimize inventory, staff efficiently, and plan targeted marketing campaigns, all of which contribute to better business outcomes.

Through this project, we saw how combining data science and domain knowledge can create a robust, data-driven sales forecasting solution, ready for practical implementation in the retail industry.

