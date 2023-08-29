from convert import Numerical
from flask import Flask,request,render_template
import pickle
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check',methods=['GET','POST'])
def check():
    if request.method=='POST':
        name=request.form.get('name')
        gender=request.form.get('gender')
        married=request.form.get('married')
        dependents=request.form.get('dependents')
        education=request.form.get('education')
        self_employed=request.form.get('self-employed')
        applicant_income=request.form.get('applicant-income')
        coapplicant_income=request.form.get('coapplicant-income')
        loan_amount=request.form.get('loan-amount')
        loan_term=request.form.get('loan-term')
        credit_history=request.form.get('credit-history')
        property_ar=request.form.get('property-area')
        nt=Numerical()
        g=nt.converted('Gender',gender)
        m=nt.converted('Married',married)
        d=int(dependents)
        e=nt.converted('Education',education)
        s=nt.converted('Self_Employed',self_employed)
        if credit_history=='Yes':
            c=1
        else:
            c=0
        p=nt.converted('Property_Area',property_ar)
        with open('model.pickle','rb') as model:
            ml=pickle.load(model)
        pred=ml.predict([[g,m,d,e,s,applicant_income,coapplicant_income,loan_amount,loan_term,c,p]])
        if pred[0]==1:
            status="Loan Approved"
        else:
            status="Loan Rejected"
        return render_template("message.html",status=status) 
        
    else:
        return render_template('check.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)