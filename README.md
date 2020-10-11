# [Transaction Monitoring - An Anti-Money Laundering System](https://youtu.be/MUWR2QZlUnk)

## Problem

Money laundering is the illegal process of concealing the origins of money obtained illegally by passing it through a complex sequence of banking transfers or commercial transactions. The estimated amount of money laundered globally in one year is 2 - 5% of global GDP, or $800 billion - $2 trillion in current US dollars. It calls for more equipped monitoring system to monitor transactions. 

Anti-money laundering (AML) transaction monitoring software allows banks and other financial institutions to monitor customer transactions on a daily basis or in real-time for risk. Our solution will automate the whole process of detecting a suspected money laundering case.

![](images/ML.png)

## Implementation:

1. Identification of the dataset.
2. Cleaning the dataset to remove redundant data.
3. Training the Machine Learning model and building a rule based algorithm.
4. A system created by integrating both the Rule Based System and Machine Learning, will flag the transactions into different categories.
5. Potential fraudulent transactions will be identified.
6. Whole backend will be integrated with a fontend platform.
7. User can upload the data of daily transactions and can get potential fraudulent transactions.

## Application

By combining these information with analysis of customers’ historical information and account profile, the software can provide financial institutions with a “whole picture” analysis of a customer’s profile, risk levels, and predicted future activity, and can also generate reports and create alerts to suspicious activity.

## Instructions

1. Clone this repository using `git clone https://github.com/UtkarshChaurasia/Transaction-Monitoring.git`
2. Install python using `sudo apt-get install python3.6`
3. Switch to repository folder. 
3. Install all the required libraries using `pip install -r requirements.txt`
4. Run app.py file using `streamlit run app.py`
5. Open the localhost link in your favourite browser.
6. Now you can upload the Dummy Transaction Dataset and click the Predict button to know the potential Money Laundering cases.

## Future Prospects:

With increasing crony capitalism and corruption due to the slightest of inefficiencies and people’s urges to make the most money in the shortest period of time, even not considering the legal implications, it is almost certain that we will see an increase in the amount of money being laundered in the global economy, without an interference by major players like financial institutions, consulting firms etc. A notification system will be integrated as well which will notify the person via email whose transactions are flagged as money laundering case. To make our project self sustainable and ever adapting according to the market scenario, an integration of a simple Artificial neural network will be done to the model created, so that, as datasets become larger, the efficiency does not take a hit, and the model learns from itself, just like all of us.

