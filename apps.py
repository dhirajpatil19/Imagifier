from flask import Flask,render_template,url_for,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    file1 = request.files['inputfile']
    return file1.filename

if __name__ == '__main__':
    app.run(debug=True)