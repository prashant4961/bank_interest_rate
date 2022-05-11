# bank_interest_rate
intrest rate detection regression model,this Dataset
Use the data set to find the parameters affecting the loan interest rates for applicants based on their personal information

# Column Description
* ID>customer ID

* Amount.Requested > Loan amount requested by the customer

* Amount.Funded.By.Investors > Loan amount sanctioned by the bank for the customers

* Loan.Length > Loan tenure period

* Loan.Purpose > purpose of the loan

* Debt.To.Income.Ratio > ratio of total debts for the customer based on his/her total income

* State > State in which the customer resides

* Home.Ownership > Status of the home owned by the customer

* Monthly.Income > Monthly income of the customer

* FICO range > customer's credit score range

* Open.Credit.Lines > number of parallel debts that the customers have

* Revolving.Credit.Balance > total debt balance considering all the open credit lines

* Inquiries.in.last.6.months > number of esquires by the customer regarding the loan

* Employment.Length > work experience of the customers

# TARGET COLUMN
* Interest.Rates > The interest rate fixed by the bank for each customer




# EDA part on columns
1. ID         >>> Dropped id column as it contains unique values
2. Amount_Requested >>>>  
    * it had . values and na value replaced it with median value .... 
    * no need to remove outliers as it is in range

3. Amount_Funded.By.Investors
    * changed data type from object
    *  no need to replace outliers as it is in range

4. Target column (Interest_Rate)
    * replaced % sign and converted to float.

5. Loan_Length
    * just reploaced values 

6. Loan_Purpose
    * created dummy data freame  as it wad having 14 unique values and were of great importance
    * merged it with original dataframe

7. Debt_To_Income_Ratio
    * removed % and changed dtype to float
