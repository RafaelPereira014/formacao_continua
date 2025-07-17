from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)