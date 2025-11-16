from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

display_map = {
    "unacc": "❌ Unacceptable",
    "acc": "👍 Acceptable",
    "good": "✅ Good",
    "vgood": "🌟 Very Good"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
       
        buying = request.form['buying']
        maint = request.form['maint']
        doors = request.form['doors']
        persons = request.form['persons']
        lug_boot = request.form['lug_boot']
        safety = request.form['safety']

        
        inputs = [
            label_encoders['buying'].transform([buying])[0],
            label_encoders['maint'].transform([maint])[0],
            label_encoders['doors'].transform([doors])[0],
            label_encoders['persons'].transform([persons])[0],
            label_encoders['lug_boot'].transform([lug_boot])[0],
            label_encoders['safety'].transform([safety])[0]
        ]

        
        pred_num = model.predict([inputs])[0]
        pred_label = label_encoders['class'].inverse_transform([pred_num])[0]
        prediction = display_map.get(pred_label, pred_label)


    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
