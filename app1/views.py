from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Create your views here.
def index(request):
    if request.method == 'POST':
        data = pd.read_csv("static/diabetes.csv")
        x = data.drop('Outcome',axis=1)
        y = data['Outcome']
        X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2)
        model = LogisticRegression()
        model.fit(X_train,Y_train)
        pregnancies = float(request.POST['Pregnancies'])
        glucose = float(request.POST['Glucose'])
        bp = float(request.POST['BP'])
        st = float(request.POST['ST'])
        insulin = float(request.POST['Insulin'])
        bmi = float(request.POST['BMI'])
        dpf = float(request.POST['DPF'])
        age = float(request.POST['Age'])
        prediction = model.predict([[pregnancies,glucose,bp,st,insulin,bmi,dpf,age]])
        if prediction==[1]:
            result = 'Positive'
        else:
            result = 'Negative'
        return render(request, 'index.html', {'result' : result})
    
    else:
        return render(request, 'index.html')