import pandas as pd
import numpy as np
import pickle
import pkgutil


from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle.load(open('dt_modl.pkl','rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')
    # return "SUCCESS"

@app.route('/interest_rate', methods = ['POST','GET'])
def interest_rate():

    data = request.form
    vector = np.zeros(72)

    Loan_Purpose = data['Loan_Purpose']
    print(Loan_Purpose)
    Loan_Purpose_list = columns.get('columns')[10:24].tolist()
    print(Loan_Purpose_list)
    Loan_Purpose_index = Loan_Purpose_list.index(Loan_Purpose)
    print(Loan_Purpose_index)
        
    Home_Ownership = data['Home_Ownership']
    print(Home_Ownership)
    Home_Ownership_list = columns.get('columns')[24:27].tolist()
    print(Home_Ownership_list)
    Home_Ownership_index = Home_Ownership_list.index(Home_Ownership)
    print(Home_Ownership_index)

    State = data['State']
    print(State)
    State_list = columns.get('columns')[27:].tolist()
    print(State_list)
    State_index = State_list.index(State)
    print(State_index)


    vector[Loan_Purpose_index] == 1
    vector[Home_Ownership_index] == 1
    vector[State_index] == 1        
       
    vector[0] = data['Amount_Requested']
    vector[1] = data['Amount_Funded_By_Investors']
    vector[3] = data['Loan_Length']
    vector[4] = data['Debt_To_Income_Ratio']
    vector[5] = data['Monthly_Income']
    vector[6] = data['FICO_Range']
    vector[7] = data['Open_CREDIT_Lines']
    vector[8] = data['Revolving_CREDIT_Balance']
    vector[9] = data['Inquiries_in_the_Last_6_Months']
    vector[10] = data['Employment_Length']



    input = [vector]

    prediction = model.predict(input)
    
    # result = model.predict([[Loan_Purpose,Home_Ownership,State,Amount_Requested,Amount_Funded_By_Investors,
    #                          Loan_Length,Debt_To_Income_Ratio,Monthly_Income,FICO_Range,Open_CREDIT_Lines,
    #                          Revolving_CREDIT_Balance,Inquiries_in_the_Last_6_Months,Employment_Length]])
    print(prediction[0])
    
    return render_template('index.html',prediction = prediction[0])


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0' , port=8080)
