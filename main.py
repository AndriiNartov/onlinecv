from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv')
def show_cv():
    return render_template('about.html')

@app.route('/projects')
def show_projects():
    return render_template('work.html')

if __name__ == '__main__':
    app.run(debug=True)
