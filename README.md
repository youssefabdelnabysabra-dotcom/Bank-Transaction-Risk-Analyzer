Bank Transaction Risk and Anomaly Analyzer

This project is a console-based Python application that analyzes bank transaction
data to detect risky customers and suspicious transactions using statistical
techniques and rule-based logic.

The project is built using Object-Oriented Programming (OOP) principles and
follows a modular structure to make the code easy to understand and maintain.



Dataset
-------
The project uses the PaySim mobile money transaction dataset.
Each row represents a single transaction.

Main columns used:
- step: time step 
- type: transaction type
- amount: transaction amount
- nameOrig: sender ID
- oldbalanceOrg 
- newbalanceOrig
- nameDest: receiver ID
- oldbalanceDest
- isFrauD


Main Features
-------------
1. load large CSV files with optional row limits
2. clean data 
3. feature engineering:
   - transaction count per customer
   - average transaction amount
   - transaction day
   - balance error detection
4. risk scoring using Z-score (SciPy)
5. risk classification into:
   - Low
   - Medium
   - High
   - Critical
6. Rule-based suspicious transaction flagging
7. Export reports as CSV and text files


Risk Detection Logic
-------------------
- Statistical anomaly detection using Z-score on transaction amount
- Business rules to flag suspicious transactions:
  - Transaction type is TRANSFER or CASH_OUT
  - Sender balance becomes zero
  - Balance calculation inconsistency exists


Output Files
------------
After running the analysis, the following files are generated in the reports folder:
- flagged_transactions.csv
- customer_risk_summary.csv
- report.txt


How to Run
----------
1. save the dataset 
2. Open a terminal in the project root directory
3. Run the application:

   python main.py

4. Use the menu to run each step in order:
   1- Load dataset  
   2 - Clean data  
   3 -Build features  
   4 - Score risk  
   5-flag suspicious transactions  
   6- export reports  
   7- display summary  


Libraries Used
--------------
- pandas
- numpy
- scipy



