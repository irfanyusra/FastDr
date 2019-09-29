from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)

dict ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964}


testdata = ["Hospital 1", "Hospital 2", "Hospital 3"]
testdata2 = [4.3, 5.2, 6.3]
testdata3 = [7.1, 8.7, 9.5]
#testdata = {["Hospital 1", "Hospital 2", "Hospital 3"], [4.3, 5.2, 6.3], [7.1, 8.7, 9.5]}

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/findAHospital.html/')
def about():
    #if request.method == "GET":
        #return render_template("findAHospital.html", testdata=testdata)
    return render_template('findAHospital.html', testdata=testdata, testdata2=testdata2, testdata3=testdata3)


@app.route('/text', methods=['GET', 'POST'])
def text(comments=[]):
    #if request.method == "GET":
    return render_template("index.html", testdata=testdata, testdata2=testdata2, testdata3=testdata3)
    #return redirect(url_for('text'))


if __name__ == '__main__':
    app.run(debug=True)
