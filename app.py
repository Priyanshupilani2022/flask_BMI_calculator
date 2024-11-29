from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods =['POST','GET'])

def index():
    weight=""
    height=""
    bmi=""
    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
        weight= float(request.form.get('weight'))
        height= float(request.form.get('height'))
        bmi= (weight/(height*2))
    return render_template('index.html',
                            weight = weight,
                            height = height,
                            bmi=bmi)

app.run(debug=True)
