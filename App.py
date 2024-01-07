from flask import Flask , render_template
app = Flask(__name__)
if __name__=="__main__":
    with app.app_context():
        app.run(debug=True)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/about')
def about():
    return 'This is a about page'