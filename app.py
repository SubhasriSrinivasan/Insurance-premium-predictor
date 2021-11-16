from flask import Flask,request,render_template
import numpy as np
import pickle
app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def showFile():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    data = []
    if request.form.to_dict()['region'] == 'southwest':
        data.extend([0,0,0,1])
    elif request.form.to_dict()['region'] == 'southeast':
        data.extend([0,0,1,0])
    elif request.form.to_dict()['region'] == 'northwest':
        data.extend([0,1,0,0])
    elif request.form.to_dict()['region'] == 'northeast':
        data.extend([1,0,0,0])
    data.extend([int(request.form.to_dict()['age']),int(request.form.to_dict()['sex'] == 'male'),float(request.form.to_dict()['bmi']),int(request.form.to_dict()['children']),int(request.form.to_dict()['smoker'] == 'yes')])
    print(data)
    newdata = [np.array(data)]
    prediction = model.predict(newdata)
    return render_template('index.html',info=f"Your Premium amount in Rs. : {prediction[0]:.2f}")

if __name__ == '__main__':
    app.run()