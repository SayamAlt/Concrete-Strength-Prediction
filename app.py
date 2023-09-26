from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

pipeline = joblib.load('pipeline.pkl')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        superplasticizer = float(request.form['superplasticizer'])
        water = float(request.form['water'])
        coarse_aggregate = float(request.form['coarse_aggregate'])
        blast_furnace_slag = float(request.form['blast_furnace_slag'])
        cement = float(request.form['cement'])
        data = [[age,superplasticizer,water,coarse_aggregate,blast_furnace_slag,cement]]
        data = pd.DataFrame(data,columns=['Age', 'Superplasticizer', 'Water', 'Coarse Aggregate', 'Blast Furnace Slag','Cement'])
        pred = round(pipeline.predict(data)[0],2)
        return render_template('index.html',prediction_text=f"The concrete strength based on the specified values is {pred}.")
    

if __name__ == '__main__':
    app.run(port=8080)