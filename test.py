from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
app.config['DEBUG'] = True
app.run(debug = True)

@app.route('/')
def landing():
    # this is where we want to put our landing page (in t1.html, for example)
    return render_template("t1.html", name = "Dhruv")

@app.route('/input', methods=['GET', 'POST'])
def user_input():
    # if we are loading the form without any submissions, simply show the form
    if request.method == "GET":
        return render_template("input.html")

    # if there is something user(s) submitted, process the input
    else:
        # print(request.form)
        userFile = request.files["fileUpload"]

        # the uploaded file is saved as roomPic.jpg in the current directory
        userFile.save("./roomPic.jpg")

        res = process("./roomPic.jpg")

        return render_template("input.html", fooResponse = res)

def process(fPath: str):
    print(f"{fPath} is the path to the user's input photo")
    dataAfterProcessing = fPath
    # do something
    return dataAfterProcessing

@app.route('/results')
def results():
    return "RESULTS"